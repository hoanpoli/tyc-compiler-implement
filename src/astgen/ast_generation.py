from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):
    def visitProgram(self, ctx: TyCParser.ProgramContext):
        if ctx.getChildCount() == 0:
            return Program([])
        return Program(self.visit(ctx.decl_list()))

    def visitDecl(self, ctx: TyCParser.DeclContext):
        return self.visitChildren(ctx)

    def visitDecl_list(self, ctx: TyCParser.Decl_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.decl())] + self.visit(ctx.decl_list())

    def visitFunc_decl(self, ctx: TyCParser.Func_declContext):
        return_type = self.visit(ctx.func_return())
        name = ctx.ID().getText()
        params = self.visit(ctx.param_list()) if ctx.param_list() else []
        body = self.visit(ctx.block_stmt()) if ctx.block_stmt() else []
        return FuncDecl(return_type, name, params, body)

    def visitFunc_return(self, ctx: TyCParser.Func_returnContext):
        return self.visit(ctx.return_type())

    def visitReturn_type(self, ctx: TyCParser.Return_typeContext):
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.type_())

    def visitParam_list(self, ctx: TyCParser.Param_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#param_prime.
    def visitParam_prime(self, ctx: TyCParser.Param_primeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#param_decl.
    def visitParam_decl(self, ctx: TyCParser.Param_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#stmt_list.
    def visitStmt_list(self, ctx: TyCParser.Stmt_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmt_list())

    # Visit a parse tree produced by TyCParser#struct_decl.
    def visitStruct_decl(self, ctx: TyCParser.Struct_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#struct_body_list.
    def visitStruct_body_list(self, ctx: TyCParser.Struct_body_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#struct_member_list.
    def visitStruct_member_list(self, ctx: TyCParser.Struct_member_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#struct_body.
    def visitStruct_body(self, ctx: TyCParser.Struct_bodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#stmt.
    def visitStmt(self, ctx: TyCParser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#var_decl_stmt.
    def visitVar_decl_stmt(self, ctx: TyCParser.Var_decl_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#var_init.
    def visitVar_init(self, ctx: TyCParser.Var_initContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#block_stmt.
    def visitBlock_stmt(self, ctx):
        if ctx.stmt_list():
            return BlockStmt(self.visit(ctx.stmt_list()))
        return BlockStmt([])

    # Visit a parse tree produced by TyCParser#decl_type.
    def visitDecl_type(self, ctx: TyCParser.Decl_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#type.
    def visitType(self, ctx: TyCParser.TypeContext):
        text = ctx.getText()
        if text == "int":
            return IntType()
        if text == "float":
            return FloatType()
        if text == "string":
            return StringType()
        if text == "void":
            return VoidType()
        return StructType(text)

    # Visit a parse tree produced by TyCParser#if_stmt.
    def visitIf_stmt(self, ctx: TyCParser.If_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#else_part.
    def visitElse_part(self, ctx: TyCParser.Else_partContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#while_stmt.
    def visitWhile_stmt(self, ctx: TyCParser.While_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#for_stmt.
    def visitFor_stmt(self, ctx: TyCParser.For_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#for_init.
    def visitFor_init(self, ctx: TyCParser.For_initContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#for_var_decl.
    def visitFor_var_decl(self, ctx: TyCParser.For_var_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#for_cond.
    def visitFor_cond(self, ctx: TyCParser.For_condContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#for_update.
    def visitFor_update(self, ctx: TyCParser.For_updateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#switch_stmt.
    def visitSwitch_stmt(self, ctx: TyCParser.Switch_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#switch_body.
    def visitSwitch_body(self, ctx: TyCParser.Switch_bodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#switch_item_list.
    def visitSwitch_item_list(self, ctx: TyCParser.Switch_item_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#switch_item.
    def visitSwitch_item(self, ctx: TyCParser.Switch_itemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#case_clause.
    def visitCase_clause(self, ctx: TyCParser.Case_clauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#default_clause.
    def visitDefault_clause(self, ctx: TyCParser.Default_clauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#case_expr.
    def visitCase_expr(self, ctx: TyCParser.Case_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#case_add.
    def visitCase_add(self, ctx: TyCParser.Case_addContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#case_mul.
    def visitCase_mul(self, ctx: TyCParser.Case_mulContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#case_unary.
    def visitCase_unary(self, ctx: TyCParser.Case_unaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#case_primary.
    def visitCase_primary(self, ctx: TyCParser.Case_primaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#break_stmt.
    def visitBreak_stmt(self, ctx: TyCParser.Break_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#continue_stmt.
    def visitContinue_stmt(self, ctx: TyCParser.Continue_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#return_stmt.
    def visitReturn_stmt(self, ctx: TyCParser.Return_stmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return ReturnStmt(expr)

    # Visit a parse tree produced by TyCParser#return_expr.
    def visitReturn_expr(self, ctx: TyCParser.Return_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#expr_stmt.
    def visitExpr_stmt(self, ctx: TyCParser.Expr_stmtContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by TyCParser#expr.
    def visitExpr(self, ctx: TyCParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#assign_expr.
    def visitAssign_expr(self, ctx: TyCParser.Assign_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logic_or_expr())
        left = self.visit(ctx.lhs())
        right = self.visit(ctx.assign_expr())
        return AssignExpr(left, right)

    # Visit a parse tree produced by TyCParser#lhs.
    def visitLhs(self, ctx: TyCParser.LhsContext):
        return Identifier(ctx.ID().getText())

    # Visit a parse tree produced by TyCParser#logic_or_expr.
    def visitLogic_or_expr(self, ctx: TyCParser.Logic_or_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logic_and_expr())
        left = self.visit(ctx.logic_or_expr())
        right = self.visit(ctx.logic_and_expr())
        return BinaryOp(ctx.OR().getText(), left, right)

    # Visit a parse tree produced by TyCParser#logic_and_expr.
    def visitLogic_and_expr(self, ctx: TyCParser.Logic_and_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.equality_expr())
        left = self.visit(ctx.logic_and_expr())
        right = self.visit(ctx.equality_expr())
        return BinaryOp(ctx.AND().getText(), left, right)

    # Visit a parse tree produced by TyCParser#equality_expr.
    def visitEquality_expr(self, ctx: TyCParser.Equality_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relational_expr())
        left = self.visit(ctx.relational_expr())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.relational_expr())
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by TyCParser#relational_expr.
    def visitRelational_expr(self, ctx: TyCParser.Relational_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.additive_expr())
        left = self.visit(ctx.additive_expr())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.additive_expr())
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by TyCParser#additive_expr.
    def visitAdditive_expr(self, ctx: TyCParser.Additive_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplicative_expr())
        left = self.visit(ctx.additive_expr())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.multiplicative_expr())
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by TyCParser
    def visitMultiplicative_expr(self, ctx: TyCParser.Multiplicative_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unary_expr())
        left = self.visit(ctx.multiplicative_expr())
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.unary_expr())
        return BinaryOp(op, left, right)

    # Visit a parse tree produced by TyCParser#unary_expr.
    def visitUnary_expr(self, ctx: TyCParser.Unary_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#prefix_expr.
    def visitPrefix_expr(self, ctx: TyCParser.Prefix_exprContext):
        right = self.visit(ctx.unary_expr())
        return PrefixOp(ctx.getChild(0).getText(), right)

    # Visit a parse tree produced by TyCParser#postfix_expr.
    def visitPostfix_expr(self, ctx: TyCParser.Postfix_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary_expr())
        return 

    # Visit a parse tree produced by TyCParser#postfix_suffix.
    def visitPostfix_suffix(self, ctx: TyCParser.Postfix_suffixContext):
        if ctx.getChildCount == 2:
            return ctx.getChild(1).getText()
        return self.visit(ctx.argument_list())

    # Visit a parse tree produced by TyCParser#primary_expr.
    def visitPrimary_expr(self, ctx: TyCParser.Primary_exprContext):
        if ctx.ID():
            return Identifier(ctx.ID().getText())
        if ctx.INT_LITERAL():
            return IntLiteral(int(ctx.INT_LITERAL().getText()))
        if ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        if ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        if ctx.expr():
            return self.visit(ctx.expr())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TyCParser#struct_literal.
    def visitStruct_literal(self, ctx: TyCParser.Struct_literalContext):
        return self.visit(ctx.argument_list())

    # Visit a parse tree produced by TyCParser#argument_list.
    def visitArgument_list(self, ctx: TyCParser.Argument_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.expr)] + self.visit(ctx.argument_tail())

    # Visit a parse tree produced by TyCParser#argument_tail.
    def visitArgument_tail(self, ctx: TyCParser.Argument_tailContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.expr)] + self.visit(ctx.argument_tail())
