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
        pass

    def _add_builtins(self, env: List[List[VarDecl | FuncDecl | StructDecl | Param]]):
        builtins = [
            FuncDecl(IntType(), "readInt", [], BlockStmt([])),
            FuncDecl(FloatType(), "readFloat", [], BlockStmt([])),
            FuncDecl(StringType(), "readString", [], BlockStmt([])),
            FuncDecl(VoidType(), "printInt", [Param(IntType(), "arg")], BlockStmt([])),
            FuncDecl(VoidType(), "printFloat", [Param(FloatType(), "arg")], BlockStmt([])),
            FuncDecl(VoidType(), "printString", [Param(StringType(), "arg")], BlockStmt([])),
        ]
        for b in builtins:
            env[0].append(b)

    def _lookup(self, name: str, env: List[List[VarDecl | FuncDecl | StructDecl | Param]]) -> Optional[VarDecl | FuncDecl | StructDecl | Param]:
        for scope in reversed(env):
            for node in scope:
                if node.name == name:
                    return node
        return None

    def _contains_locally(self, name: str, env: List[List[VarDecl | FuncDecl | StructDecl | Param]]) -> bool:
        for node in env[-1]:
            if node.name == name:
                return True
        return False

    def check_program(self, node: Program):
        env = [[]]
        self._add_builtins(env)
        o = {
            "env": env,
            "loop": 0,
            "switch": False,
            "ret_ty": None,
            "func_node": None,
            "auto_vars": []
        }
        return self.visit(node, o)

    def is_same_type(self, t1: Optional[TyCType], t2: Optional[TyCType]) -> bool:
        if t1 is None or t2 is None:
            return False
        if type(t1) is not type(t2):
            return False
        if isinstance(t1, StructType) and isinstance(t2, StructType):
            return t1.struct_name == t2.struct_name
        return True

    def unify(self, node: Expr, expected_ty: TyCType, o: Any) -> TyCType:
        """Try to infer type of node from expected_ty if node has unknown type."""
        actual_ty = self.visit(node, o)
        if actual_ty is None:
            if isinstance(node, Identifier):
                decl = self._lookup(node.name, o['env'])
                if isinstance(decl, VarDecl) and decl.var_type is None:
                    decl.var_type = expected_ty
                    return expected_ty
                raise TypeCannotBeInferred(node.name)
            raise TypeMismatchInExpression(node)
        return actual_ty

    def visit_program(self, node: Program, o: Any = None):
        for decl in node.decls:
            self.visit(decl, o)
        return "Static checking passed"

    def visit_struct_decl(self, node: StructDecl, o: Any = None):
        if self._contains_locally(node.name, o['env']):
            raise Redeclared("Struct", node.name)
        
        
        member_names = set()
        for member in node.members:
            if member.name in member_names:
                raise Redeclared("Variable", member.name)
            member_names.add(member.name)
            
            m_ty = self.visit(member.member_type, o)
            if isinstance(m_ty, StructType):
                if not self._lookup(m_ty.struct_name, o['env']):
                    raise UndeclaredStruct(m_ty.struct_name)
                    
        o['env'][0].append(node)

    def visit_member_decl(self, node: MemberDecl, o: Any = None):
        
        pass

    def visit_func_decl(self, node: FuncDecl, o: Any = None):
        if self._contains_locally(node.name, o['env']):
            raise Redeclared("Function", node.name)
        
        ret_ty = self.visit(node.return_type, o) if node.return_type else None
        if isinstance(ret_ty, StructType):
            if not self._lookup(ret_ty.struct_name, o['env']):
                raise UndeclaredStruct(ret_ty.struct_name)

        param_names = set()
        for p in node.params:
            if p.name in param_names:
                raise Redeclared("Parameter", p.name)
            param_names.add(p.name)
            
            p_ty = self.visit(p.param_type, o)
            if isinstance(p_ty, StructType):
                if not self._lookup(p_ty.struct_name, o['env']):
                    raise UndeclaredStruct(p_ty.struct_name)
            
        o['env'][0].append(node)
        
        func_o = o.copy()
        func_o['env'] = o['env'] + [[]]
        func_o['ret_ty'] = ret_ty
        func_o['func_node'] = node
        func_o['auto_vars'] = [] # New list for this function
        func_o['loop'] = 0
        func_o['switch'] = False
        
        for p in node.params:
            func_o['env'][-1].append(p)
            
        self.visit(node.body, func_o)
        
        for var_node in func_o['auto_vars']:
            if var_node.var_type is None:
                raise TypeCannotBeInferred(var_node.name)
        
        if node.return_type is None and func_o['ret_ty'] is None:
            node.return_type = VoidType()

    def visit_param(self, node: Param, o: Any = None):
        return self.visit(node.param_type, o)

    
    def visit_int_type(self, node: IntType, o: Any = None):
        return IntType()

    def visit_float_type(self, node: FloatType, o: Any = None):
        return FloatType()

    def visit_string_type(self, node: StringType, o: Any = None):
        return StringType()

    def visit_void_type(self, node: VoidType, o: Any = None):
        return VoidType()

    def visit_struct_type(self, node: StructType, o: Any = None):
        if not self._lookup(node.struct_name, o['env']):
            raise UndeclaredStruct(node.struct_name)
        return StructType(node.struct_name)

    
    def visit_block_stmt(self, node: BlockStmt, o: Any = None):
        new_o = o.copy()
        new_o['env'] = o['env'] + [[]]
        for stmt in node.statements:
            self.visit(stmt, new_o)

    def visit_var_decl(self, node: VarDecl, o: Any = None):
        if self._contains_locally(node.name, o['env']):
            raise Redeclared("Variable", node.name)
            
        var_ty = self.visit(node.var_type, o) if node.var_type else None
        
        if node.init_value:
            rhs_ty = self.visit(node.init_value, o) 
            
            if var_ty is None:
                if rhs_ty is None:
                    raise TypeCannotBeInferred(node.name)
                var_ty = rhs_ty
                node.var_type = var_ty 
            else:
                if not self.is_same_type(var_ty, rhs_ty):
                    raise TypeMismatchInStatement(node)
        
        if node.var_type is None:
            o['auto_vars'].append(node)
            
        o['env'][-1].append(node)

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
        
        loop_o = o.copy()
        loop_o['loop'] = o['loop'] + 1
        self.visit(node.body, loop_o)

    def visit_for_stmt(self, node: ForStmt, o: Any = None):
        new_o = o.copy()
        new_o['env'] = o['env'] + [[]] 
        
        if node.init:
            self.visit(node.init, new_o)
        if node.condition:
            cond_ty = self.visit(node.condition, new_o)
            if not isinstance(cond_ty, IntType):
                raise TypeMismatchInStatement(node)
        if node.update:
            self.visit(node.update, new_o)
            
        loop_o = new_o.copy()
        loop_o['loop'] = o['loop'] + 1
        self.visit(node.body, loop_o)

    def visit_switch_stmt(self, node: SwitchStmt, o: Any = None):
        expr_ty = self.visit(node.expr, o)
        if not isinstance(expr_ty, IntType):
            raise TypeMismatchInStatement(node)
            
        switch_o = o.copy()
        switch_o['switch'] = True
        for case in node.cases:
            self.visit(case, switch_o)
        if node.default_case:
            self.visit(node.default_case, switch_o)

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
        if o['loop'] == 0 and not o['switch']:
            raise MustInLoop(node)

    def visit_continue_stmt(self, node: ContinueStmt, o: Any = None):
        if o['loop'] == 0:
            raise MustInLoop(node)

    def visit_return_stmt(self, node: ReturnStmt, o: Any = None):
        expr_ty = self.visit(node.expr, o) if node.expr else VoidType() 
        
        if o['ret_ty'] is None:
            if isinstance(expr_ty, VoidType):
                o['func_node'].return_type = VoidType()
                o['ret_ty'] = VoidType()
            else:
                if expr_ty is None: 
                     if isinstance(node.expr, Identifier):
                         raise TypeCannotBeInferred(node.expr.name)
                     raise TypeMismatchInStatement(node)
                o['func_node'].return_type = expr_ty
                o['ret_ty'] = expr_ty
        else:
            if expr_ty is None:
                 if isinstance(node.expr, Identifier):
                     expr_ty = self.unify(node.expr, o['ret_ty'], o)
                 else:
                     raise TypeMismatchInStatement(node)
            
            if not self.is_same_type(o['ret_ty'], expr_ty):
                raise TypeMismatchInStatement(node)

    def visit_expr_stmt(self, node: ExprStmt, o: Any = None):
        self.visit(node.expr, o)

    def visit_binary_op(self, node: BinaryOp, o: Any = None):
        l_ty = self.visit(node.left, o)
        r_ty = self.visit(node.right, o)
        
        op = node.operator
        
        if l_ty is None and r_ty is not None:
            l_ty = self.unify(node.left, r_ty, o)
        elif r_ty is None and l_ty is not None:
            r_ty = self.unify(node.right, l_ty, o)
        elif l_ty is None and r_ty is None:
            if isinstance(node.left, Identifier):
                raise TypeCannotBeInferred(node.left.name)
            if isinstance(node.right, Identifier):
                raise TypeCannotBeInferred(node.right.name)
            raise TypeMismatchInExpression(node)
        
        if op in ['+', '-', '*', '/']:
            if not (isinstance(l_ty, (IntType, FloatType)) and isinstance(r_ty, (IntType, FloatType))):
                raise TypeMismatchInExpression(node)
            if isinstance(l_ty, IntType) and isinstance(r_ty, IntType):
                return IntType()
            return FloatType()
            
        if op == '%':
            if not (isinstance(l_ty, IntType) and isinstance(r_ty, IntType)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        if op in ['==', '!=', '<', '<=', '>', '>=']:
            if not (isinstance(l_ty, (IntType, FloatType)) and isinstance(r_ty, (IntType, FloatType))):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        if op in ['&&', '||']:
            if not (isinstance(l_ty, IntType) and isinstance(r_ty, IntType)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_prefix_op(self, node: PrefixOp, o: Any = None):
        ty = self.visit(node.operand, o)
        op = node.operator
        
        if op in ['++', '--']:
            if ty is None:
                ty = self.unify(node.operand, IntType(), o)
            if not isinstance(ty, IntType):
                raise TypeMismatchInExpression(node)
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        if op in ['+', '-']:
            if ty is None:
                if isinstance(node.operand, Identifier):
                    raise TypeCannotBeInferred(node.operand.name)
                raise TypeMismatchInExpression(node)
            if not isinstance(ty, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            return ty
            
        if op == '!':
            if ty is None:
                ty = self.unify(node.operand, IntType(), o)
            if not isinstance(ty, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_postfix_op(self, node: PostfixOp, o: Any = None):
        ty = self.visit(node.operand, o)
        op = node.operator
        
        if op in ['++', '--']:
            if ty is None:
                ty = self.unify(node.operand, IntType(), o)
            if not isinstance(ty, IntType):
                raise TypeMismatchInExpression(node)
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            return IntType()
            
        raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: AssignExpr, o: Any = None):
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
            
        l_ty = self.visit(node.lhs, o)
        
        if l_ty is None:
            r_ty = self.visit(node.rhs, o) 
            if r_ty is not None:
                if isinstance(node.lhs, Identifier):
                    decl = self._lookup(node.lhs.name, o['env'])
                    if isinstance(decl, VarDecl) and decl.var_type is None:
                        decl.var_type = r_ty
                        l_ty = r_ty
        else:
            r_ty = self.visit(node.rhs, o) 
            
        if not self.is_same_type(l_ty, r_ty):
            raise TypeMismatchInExpression(node)
            
        return l_ty

    def visit_member_access(self, node: MemberAccess, o: Any = None):
        obj_ty = self.visit(node.obj, o)
        if not isinstance(obj_ty, StructType):
            raise TypeMismatchInExpression(node)
            
        decl = self._lookup(obj_ty.struct_name, o['env'])
        if not isinstance(decl, StructDecl):
            raise UndeclaredStruct(obj_ty.struct_name)
            
        for member in decl.members:
            if member.name == node.member:
                return member.member_type
                
        raise TypeMismatchInExpression(node) 

    def visit_func_call(self, node: FuncCall, o: Any = None):
        decl = self._lookup(node.name, o['env'])
        if not isinstance(decl, FuncDecl):
            raise UndeclaredFunction(node.name)
            
        if len(node.args) != len(decl.params):
            raise TypeMismatchInExpression(node)
            
        for i, arg in enumerate(node.args):
            p_ty = decl.params[i].param_type
            arg_ty = self.visit(arg, o) 
            if not self.is_same_type(arg_ty, p_ty):
                raise TypeMismatchInExpression(node)
                
        return decl.return_type

    def visit_identifier(self, node: Identifier, o: Any = None):
        decl = self._lookup(node.name, o['env'])
        if not decl:
            raise UndeclaredIdentifier(node.name)
            
        if isinstance(decl, VarDecl):
            ty = decl.var_type
        elif isinstance(decl, Param):
            ty = decl.param_type
        else:
            raise TypeMismatchInExpression(node)
            
        return ty

    def visit_struct_literal(self, node: StructLiteral, o: Any = None):
        raise TypeMismatchInExpression(node) 

    def visit_int_literal(self, node: IntLiteral, o: Any = None):
        return IntType()

    def visit_float_literal(self, node: FloatLiteral, o: Any = None):
        return FloatType()

    def visit_string_literal(self, node: StringLiteral, o: Any = None):
        return StringType()
