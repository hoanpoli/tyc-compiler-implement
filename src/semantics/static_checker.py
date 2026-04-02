"""
Static Semantic Checker for TyC Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the TyC procedural programming language. It performs type checking,
scope management, type inference, and detects all semantic errors as
specified in the TyC language specification.
"""

from functools import reduce
from typing import (
    Dict,
    List,
    Set,
    Optional,
    Any,
    Tuple,
    NamedTuple,
    Union,
    TYPE_CHECKING,
)
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode,
    Program,
    StructDecl,
    MemberDecl,
    FuncDecl,
    Param,
    VarDecl,
    IfStmt,
    WhileStmt,
    ForStmt,
    BreakStmt,
    ContinueStmt,
    ReturnStmt,
    BlockStmt,
    SwitchStmt,
    CaseStmt,
    DefaultStmt,
    Type,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    BinaryOp,
    PrefixOp,
    PostfixOp,
    AssignExpr,
    MemberAccess,
    FuncCall,
    Identifier,
    StructLiteral,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    ExprStmt,
    Expr,
    Stmt,
    Decl,
)

# Type aliases for better type hints
TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]
from .static_error import (
    StaticError,
    Redeclared,
    UndeclaredIdentifier,
    UndeclaredFunction,
    UndeclaredStruct,
    TypeCannotBeInferred,
    TypeMismatchInStatement,
    TypeMismatchInExpression,
    MustInLoop,
)


class StaticChecker(ASTVisitor):
    def __init__(self):
        # Stack of scopes, each scope is a list of AST nodes (declarations)
        self.scopes: List[List[Union[VarDecl, FuncDecl, StructDecl, Param]]] = [[]]
        self.loop_depth = 0
        self.in_switch = False
        self.current_func_ty = None  # Expected return type of current function
        self.current_func_node = None # Current FuncDecl node being visited
        self.current_func_vars: List[VarDecl] = [] # Track local auto vars for inference check
        self._add_builtins()

    def _add_builtins(self):
        # Built-ins are added as simulated FuncDecl nodes (no body)
        builtins = [
            FuncDecl(IntType(), "readInt", [], BlockStmt([])),
            FuncDecl(FloatType(), "readFloat", [], BlockStmt([])),
            FuncDecl(StringType(), "readString", [], BlockStmt([])),
            FuncDecl(VoidType(), "printInt", [Param(IntType(), "arg")], BlockStmt([])),
            FuncDecl(VoidType(), "printFloat", [Param(FloatType(), "arg")], BlockStmt([])),
            FuncDecl(VoidType(), "printString", [Param(StringType(), "arg")], BlockStmt([])),
        ]
        for b in builtins:
            self.define(b)

    def enter_scope(self):
        self.scopes.append([])

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def define(self, node: Union[VarDecl, FuncDecl, StructDecl, Param], global_scope: bool = False):
        if global_scope:
            self.scopes[0].append(node)
        else:
            self.scopes[-1].append(node)

    def lookup(self, name: str) -> Optional[Union[VarDecl, FuncDecl, StructDecl, Param]]:
        for scope in reversed(self.scopes):
            for node in scope:
                if node.name == name:
                    return node
        return None

    def contains_locally(self, name: str) -> bool:
        for node in self.scopes[-1]:
            if node.name == name:
                return True
        return False
    def check_program(self, node: Program):
        return self.visit(node, None)

    def is_same_type(self, t1: Optional[TyCType], t2: Optional[TyCType]) -> bool:
        if t1 is None or t2 is None:
            return False
        if type(t1) is not type(t2):
            return False
        if isinstance(t1, StructType) and isinstance(t2, StructType):
            return t1.struct_name == t2.struct_name
        return True

    def unify(self, node: Expr, expected_ty: TyCType) -> TyCType:
        """Try to infer type of node from expected_ty if node has unknown type."""
        actual_ty = self.visit(node, expected_ty)
        if actual_ty is None:
            # We must have an Identifier that was inferred from expected_ty
            # Let's re-visit it to make sure it's updated
            actual_ty = self.visit(node, expected_ty)
            if actual_ty is None:
                if isinstance(node, Identifier):
                    raise TypeCannotBeInferred(node.name)
                raise TypeMismatchInExpression(node)
        return actual_ty

    def visit_program(self, node: Program, o: Any = None):
        for decl in node.decls:
            self.visit(decl, o)
        return "Static checking passed"

    def visit_struct_decl(self, node: StructDecl, o: Any = None):
        if self.contains_locally(node.name):
            raise Redeclared("Struct", node.name)
        
        # Check member names unique and types valid
        member_names = set()
        for member in node.members:
            if member.name in member_names:
                raise Redeclared("Variable", member.name)
            member_names.add(member.name)
            
            m_ty = self.visit(member.member_type, o)
            if isinstance(m_ty, StructType):
                if not self.lookup(m_ty.struct_name):
                    raise UndeclaredStruct(m_ty.struct_name)
                    
        self.define(node, global_scope=True)

    def visit_member_decl(self, node: MemberDecl, o: Any = None):
        # Handled in visit_struct_decl
        pass

    def visit_func_decl(self, node: FuncDecl, o: Any = None):
        if self.contains_locally(node.name):
            raise Redeclared("Function", node.name)
        
        # Check return type if explicitly specified
        ret_ty = self.visit(node.return_type, o) if node.return_type else None
        if isinstance(ret_ty, StructType):
            if not self.lookup(ret_ty.struct_name):
                raise UndeclaredStruct(ret_ty.struct_name)

        # Process parameters
        param_names = set()
        for p in node.params:
            if p.name in param_names:
                raise Redeclared("Parameter", p.name)
            param_names.add(p.name)
            
            p_ty = self.visit(p.param_type, o)
            if isinstance(p_ty, StructType):
                if not self.lookup(p_ty.struct_name):
                    raise UndeclaredStruct(p_ty.struct_name)
            
        # Define function in global scope
        self.define(node, global_scope=True)
        
        # Check body
        self.enter_scope()
        self.current_func_node = node
        self.current_func_ty = ret_ty # Might be None (auto)
        old_vars = self.current_func_vars
        self.current_func_vars = []
        
        for p in node.params:
            self.define(p)
            
        self.visit(node.body, o)
        
        # Check if any local variables still have no type (TypeCannotBeInferred)
        for var_node in self.current_func_vars:
            if var_node.var_type is None:
                raise TypeCannotBeInferred(var_node.name)
        
        # If return type was auto and was NOT inferred, it must be Void
        if node.return_type is None and self.current_func_ty is None:
            node.return_type = VoidType()
            
        self.exit_scope()
        self.current_func_vars = old_vars
        self.current_func_node = None
        self.current_func_ty = None

    def visit_param(self, node: Param, o: Any = None):
        return self.visit(node.param_type, o)

    # Type system
    def visit_int_type(self, node: IntType, o: Any = None):
        return IntType()

    def visit_float_type(self, node: FloatType, o: Any = None):
        return FloatType()

    def visit_string_type(self, node: StringType, o: Any = None):
        return StringType()

    def visit_void_type(self, node: VoidType, o: Any = None):
        return VoidType()

    def visit_struct_type(self, node: StructType, o: Any = None):
        if not self.lookup(node.struct_name):
            raise UndeclaredStruct(node.struct_name)
        return StructType(node.struct_name)

    # Statements
    def visit_block_stmt(self, node: BlockStmt, o: Any = None):
        self.enter_scope()
        for stmt in node.statements:
            self.visit(stmt, o)
        self.exit_scope()

    def visit_var_decl(self, node: VarDecl, o: Any = None):
        if self.contains_locally(node.name):
            raise Redeclared("Variable", node.name)
            
        var_ty = self.visit(node.var_type, o) if node.var_type else None
        
        if node.init_value:
            # Special case for auto with initialization
            # If auto, var_ty is None
            rhs_ty = self.visit(node.init_value, var_ty) # Pass expected type for struct literals
            
            if var_ty is None:
                # auto x = expr;
                if rhs_ty is None:
                    raise TypeCannotBeInferred(node.name)
                var_ty = rhs_ty
                node.var_type = var_ty # Update node for auto
            else:
                # Type x = expr;
                if not self.is_same_type(var_ty, rhs_ty):
                    raise TypeMismatchInStatement(node)
        
        if node.var_type is None:
            self.current_func_vars.append(node)
            
        self.define(node)

    def visit_if_stmt(self, node: IfStmt, o: Any = None):
        cond_ty = self.visit(node.condition, o)
        if not isinstance(cond_ty, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

    def visit_while_stmt(self, node: WhileStmt, o: Any = None):
        cond_ty = self.visit(node.condition, o)
        if not isinstance(cond_ty, IntType):
            raise TypeMismatchInStatement(node)
        self.loop_depth += 1
        self.visit(node.body, o)
        self.loop_depth -= 1

    def visit_for_stmt(self, node: ForStmt, o: Any = None):
        self.enter_scope() # To handle for(auto i = 0; ...)
        if node.init:
            self.visit(node.init, o)
        if node.condition:
            cond_ty = self.visit(node.condition, o)
            if not isinstance(cond_ty, IntType):
                raise TypeMismatchInStatement(node)
        if node.update:
            self.visit(node.update, o)
            
        self.loop_depth += 1
        self.visit(node.body, o)
        self.loop_depth -= 1
        self.exit_scope()

    def visit_switch_stmt(self, node: SwitchStmt, o: Any = None):
        expr_ty = self.visit(node.expr, o)
        if not isinstance(expr_ty, IntType):
            raise TypeMismatchInStatement(node)
            
        old_in_switch = self.in_switch
        self.in_switch = True
        for case in node.cases:
            self.visit(case, o)
        if node.default_case:
            self.visit(node.default_case, o)
        self.in_switch = old_in_switch

    def visit_case_stmt(self, node: CaseStmt, o: Any = None):
        case_ty = self.visit(node.expr, o)
        if not isinstance(case_ty, IntType):
            raise TypeMismatchInExpression(node.expr)
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_default_stmt(self, node: DefaultStmt, o: Any = None):
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_break_stmt(self, node: BreakStmt, o: Any = None):
        if self.loop_depth == 0 and not self.in_switch:
            raise MustInLoop(node)

    def visit_continue_stmt(self, node: ContinueStmt, o: Any = None):
        if self.loop_depth == 0:
            raise MustInLoop(node)

    def visit_return_stmt(self, node: ReturnStmt, o: Any = None):
        expr_ty = self.visit(node.expr, self.current_func_ty) if node.expr else VoidType()
        
        if self.current_func_ty is None:
            # We are in an 'auto' function, infer from this return
            if isinstance(expr_ty, VoidType):
                # If first return is empty, func is Void
                self.current_func_node.return_type = VoidType()
                self.current_func_ty = VoidType()
            else:
                self.current_func_node.return_type = expr_ty
                self.current_func_ty = expr_ty
        else:
            # Check compatibility
            if not self.is_same_type(self.current_func_ty, expr_ty):
                raise TypeMismatchInStatement(node)

    def visit_expr_stmt(self, node: ExprStmt, o: Any = None):
        self.visit(node.expr, o)

    # Expressions
    def visit_binary_op(self, node: BinaryOp, o: Any = None):
        l_ty = self.visit(node.left, None)
        r_ty = self.visit(node.right, None)
        
        op = node.operator
        
        # Unify if one is unknown
        if l_ty is None and r_ty is not None:
            l_ty = self.unify(node.left, r_ty)
        elif r_ty is None and l_ty is not None:
            r_ty = self.unify(node.right, l_ty)
        elif l_ty is None and r_ty is None:
            # Maybe we have an expected type from context?
            if isinstance(o, (IntType, FloatType)):
                l_ty = self.unify(node.left, o)
                r_ty = self.unify(node.right, o)
            else:
                # Still unknown
                if isinstance(node.left, Identifier):
                    raise TypeCannotBeInferred(node.left.name)
                if isinstance(node.right, Identifier):
                    raise TypeCannotBeInferred(node.right.name)
                raise TypeMismatchInExpression(node)
        
        # Arithmetic Operators (+, -, *, /)
        if op in ['+', '-', '*', '/']:
            # Operands must be int or float
            if not (isinstance(l_ty, (IntType, FloatType)) and isinstance(r_ty, (IntType, FloatType))):
                raise TypeMismatchInExpression(node)
            # Result: int if both int, else float
            if isinstance(l_ty, IntType) and isinstance(r_ty, IntType):
                return IntType()
            return FloatType()
            
        # Modulus Operator (%)
        if op == '%':
            if not (isinstance(l_ty, IntType) and isinstance(r_ty, IntType)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        # Relational Operators (==, !=, <, <=, >, >=)
        if op in ['==', '!=', '<', '<=', '>', '>=']:
            if not (isinstance(l_ty, (IntType, FloatType)) and isinstance(r_ty, (IntType, FloatType))):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        # Logical Operators (&&, ||)
        if op in ['&&', '||']:
            if not (isinstance(l_ty, IntType) and isinstance(r_ty, IntType)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_prefix_op(self, node: PrefixOp, o: Any = None):
        ty = self.visit(node.operand, None)
        op = node.operator
        
        if op in ['++', '--']:
            if ty is None:
                ty = self.unify(node.operand, IntType())
            if not isinstance(ty, IntType):
                raise TypeMismatchInExpression(node)
            # Must be variable or member access
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        if op in ['+', '-']:
            if ty is None:
                # Context might specify
                if isinstance(o, (IntType, FloatType)):
                    ty = self.unify(node.operand, o)
                else:
                    # Default to int? or wait?
                    # Spec says: "Prefix unary sign identity/negation: Operand int or float, result same as operand"
                    # If unknown, we can't decide.
                    if isinstance(node.operand, Identifier):
                        raise TypeCannotBeInferred(node.operand.name)
                    raise TypeMismatchInExpression(node)
            
            if not isinstance(ty, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            return ty
            
        if op == '!':
            if ty is None:
                ty = self.unify(node.operand, IntType())
            if not isinstance(ty, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_postfix_op(self, node: PostfixOp, o: Any = None):
        ty = self.visit(node.operand, None)
        op = node.operator
        
        if op in ['++', '--']:
            if ty is None:
                ty = self.unify(node.operand, IntType())
            if not isinstance(ty, IntType):
                raise TypeMismatchInExpression(node)
            # Must be variable or member access
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: AssignExpr, o: Any = None):
        # LHS must be Identifier or MemberAccess
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
            
        l_ty = self.visit(node.lhs, o)
        
        # If LHS is unknown (auto), try to infer it from RHS
        if l_ty is None:
            r_ty = self.visit(node.rhs, None)
            if r_ty is not None:
                if isinstance(node.lhs, Identifier):
                    decl = self.lookup(node.lhs.name)
                    if isinstance(decl, VarDecl) and decl.var_type is None:
                        decl.var_type = r_ty
                        l_ty = r_ty
        else:
            r_ty = self.visit(node.rhs, l_ty) # Pass LHS type to RHS for struct literals
            
        if not self.is_same_type(l_ty, r_ty):
            raise TypeMismatchInExpression(node)
            
        return l_ty

    def visit_member_access(self, node: MemberAccess, o: Any = None):
        obj_ty = self.visit(node.obj, o)
        if not isinstance(obj_ty, StructType):
            raise TypeMismatchInExpression(node)
            
        decl = self.lookup(obj_ty.struct_name)
        if not isinstance(decl, StructDecl):
            raise UndeclaredStruct(obj_ty.struct_name)
            
        # Find member in StructDecl
        for member in decl.members:
            if member.name == node.member:
                return member.member_type
                
        raise TypeMismatchInExpression(node) # Member not found

    def visit_func_call(self, node: FuncCall, o: Any = None):
        decl = self.lookup(node.name)
        if not isinstance(decl, FuncDecl):
            raise UndeclaredFunction(node.name)
            
        if len(node.args) != len(decl.params):
            raise TypeMismatchInExpression(node)
            
        for i, arg in enumerate(node.args):
            p_ty = decl.params[i].param_type
            arg_ty = self.visit(arg, p_ty) # Pass param type for struct literals
            if not self.is_same_type(arg_ty, p_ty):
                raise TypeMismatchInExpression(node)
                
        return decl.return_type

    def visit_identifier(self, node: Identifier, o: Any = None):
        decl = self.lookup(node.name)
        if not decl:
            raise UndeclaredIdentifier(node.name)
            
        # Get type based on decl kind
        if isinstance(decl, VarDecl):
            ty = decl.var_type
        elif isinstance(decl, Param):
            ty = decl.param_type
        else:
            # Identifier used as expr but refers to Func or Struct name
            raise TypeMismatchInExpression(node)
            
        if ty is None: # auto without init
            if isinstance(o, (IntType, FloatType, StringType, StructType)):
                if isinstance(decl, VarDecl):
                    decl.var_type = o
                    ty = o
            else:
                # Still unknown
                return None
        
        return ty

    def visit_struct_literal(self, node: StructLiteral, o: Any = None):
        # o should be the expected StructType
        if not isinstance(o, StructType):
            raise TypeMismatchInExpression(node)
            
        decl = self.lookup(o.struct_name)
        if not isinstance(decl, StructDecl):
            raise UndeclaredStruct(o.struct_name)
            
        if len(node.values) != len(decl.members):
            raise TypeMismatchInExpression(node)
            
        for i, val in enumerate(node.values):
            m_ty = decl.members[i].member_type
            val_ty = self.visit(val, m_ty)
            if not self.is_same_type(val_ty, m_ty):
                raise TypeMismatchInExpression(node)
                
        return o

    # Literals
    def visit_int_literal(self, node: IntLiteral, o: Any = None):
        return IntType()

    def visit_float_literal(self, node: FloatLiteral, o: Any = None):
        return FloatType()

    def visit_string_literal(self, node: StringLiteral, o: Any = None):
        return StringType()
