# Generated from d:/Hoan/tyc-compiler-implement/src/grammar/TyC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete listener for a parse tree produced by TyCParser.
class TyCListener(ParseTreeListener):

    # Enter a parse tree produced by TyCParser#program.
    def enterProgram(self, ctx:TyCParser.ProgramContext):
        pass

    # Exit a parse tree produced by TyCParser#program.
    def exitProgram(self, ctx:TyCParser.ProgramContext):
        pass


    # Enter a parse tree produced by TyCParser#decl_list.
    def enterDecl_list(self, ctx:TyCParser.Decl_listContext):
        pass

    # Exit a parse tree produced by TyCParser#decl_list.
    def exitDecl_list(self, ctx:TyCParser.Decl_listContext):
        pass


    # Enter a parse tree produced by TyCParser#decl.
    def enterDecl(self, ctx:TyCParser.DeclContext):
        pass

    # Exit a parse tree produced by TyCParser#decl.
    def exitDecl(self, ctx:TyCParser.DeclContext):
        pass


    # Enter a parse tree produced by TyCParser#func_decl.
    def enterFunc_decl(self, ctx:TyCParser.Func_declContext):
        pass

    # Exit a parse tree produced by TyCParser#func_decl.
    def exitFunc_decl(self, ctx:TyCParser.Func_declContext):
        pass


    # Enter a parse tree produced by TyCParser#func_return.
    def enterFunc_return(self, ctx:TyCParser.Func_returnContext):
        pass

    # Exit a parse tree produced by TyCParser#func_return.
    def exitFunc_return(self, ctx:TyCParser.Func_returnContext):
        pass


    # Enter a parse tree produced by TyCParser#return_type.
    def enterReturn_type(self, ctx:TyCParser.Return_typeContext):
        pass

    # Exit a parse tree produced by TyCParser#return_type.
    def exitReturn_type(self, ctx:TyCParser.Return_typeContext):
        pass


    # Enter a parse tree produced by TyCParser#param_list.
    def enterParam_list(self, ctx:TyCParser.Param_listContext):
        pass

    # Exit a parse tree produced by TyCParser#param_list.
    def exitParam_list(self, ctx:TyCParser.Param_listContext):
        pass


    # Enter a parse tree produced by TyCParser#param_prime.
    def enterParam_prime(self, ctx:TyCParser.Param_primeContext):
        pass

    # Exit a parse tree produced by TyCParser#param_prime.
    def exitParam_prime(self, ctx:TyCParser.Param_primeContext):
        pass


    # Enter a parse tree produced by TyCParser#param_decl.
    def enterParam_decl(self, ctx:TyCParser.Param_declContext):
        pass

    # Exit a parse tree produced by TyCParser#param_decl.
    def exitParam_decl(self, ctx:TyCParser.Param_declContext):
        pass


    # Enter a parse tree produced by TyCParser#stmt_list.
    def enterStmt_list(self, ctx:TyCParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by TyCParser#stmt_list.
    def exitStmt_list(self, ctx:TyCParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by TyCParser#struct_decl.
    def enterStruct_decl(self, ctx:TyCParser.Struct_declContext):
        pass

    # Exit a parse tree produced by TyCParser#struct_decl.
    def exitStruct_decl(self, ctx:TyCParser.Struct_declContext):
        pass


    # Enter a parse tree produced by TyCParser#struct_body_list.
    def enterStruct_body_list(self, ctx:TyCParser.Struct_body_listContext):
        pass

    # Exit a parse tree produced by TyCParser#struct_body_list.
    def exitStruct_body_list(self, ctx:TyCParser.Struct_body_listContext):
        pass


    # Enter a parse tree produced by TyCParser#struct_member_list.
    def enterStruct_member_list(self, ctx:TyCParser.Struct_member_listContext):
        pass

    # Exit a parse tree produced by TyCParser#struct_member_list.
    def exitStruct_member_list(self, ctx:TyCParser.Struct_member_listContext):
        pass


    # Enter a parse tree produced by TyCParser#struct_body.
    def enterStruct_body(self, ctx:TyCParser.Struct_bodyContext):
        pass

    # Exit a parse tree produced by TyCParser#struct_body.
    def exitStruct_body(self, ctx:TyCParser.Struct_bodyContext):
        pass


    # Enter a parse tree produced by TyCParser#stmt.
    def enterStmt(self, ctx:TyCParser.StmtContext):
        pass

    # Exit a parse tree produced by TyCParser#stmt.
    def exitStmt(self, ctx:TyCParser.StmtContext):
        pass


    # Enter a parse tree produced by TyCParser#var_decl_stmt.
    def enterVar_decl_stmt(self, ctx:TyCParser.Var_decl_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#var_decl_stmt.
    def exitVar_decl_stmt(self, ctx:TyCParser.Var_decl_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#var_init.
    def enterVar_init(self, ctx:TyCParser.Var_initContext):
        pass

    # Exit a parse tree produced by TyCParser#var_init.
    def exitVar_init(self, ctx:TyCParser.Var_initContext):
        pass


    # Enter a parse tree produced by TyCParser#block_stmt.
    def enterBlock_stmt(self, ctx:TyCParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#block_stmt.
    def exitBlock_stmt(self, ctx:TyCParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#decl_type.
    def enterDecl_type(self, ctx:TyCParser.Decl_typeContext):
        pass

    # Exit a parse tree produced by TyCParser#decl_type.
    def exitDecl_type(self, ctx:TyCParser.Decl_typeContext):
        pass


    # Enter a parse tree produced by TyCParser#type.
    def enterType(self, ctx:TyCParser.TypeContext):
        pass

    # Exit a parse tree produced by TyCParser#type.
    def exitType(self, ctx:TyCParser.TypeContext):
        pass


    # Enter a parse tree produced by TyCParser#if_stmt.
    def enterIf_stmt(self, ctx:TyCParser.If_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#if_stmt.
    def exitIf_stmt(self, ctx:TyCParser.If_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#else_part.
    def enterElse_part(self, ctx:TyCParser.Else_partContext):
        pass

    # Exit a parse tree produced by TyCParser#else_part.
    def exitElse_part(self, ctx:TyCParser.Else_partContext):
        pass


    # Enter a parse tree produced by TyCParser#while_stmt.
    def enterWhile_stmt(self, ctx:TyCParser.While_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#while_stmt.
    def exitWhile_stmt(self, ctx:TyCParser.While_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#for_stmt.
    def enterFor_stmt(self, ctx:TyCParser.For_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#for_stmt.
    def exitFor_stmt(self, ctx:TyCParser.For_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#for_init.
    def enterFor_init(self, ctx:TyCParser.For_initContext):
        pass

    # Exit a parse tree produced by TyCParser#for_init.
    def exitFor_init(self, ctx:TyCParser.For_initContext):
        pass


    # Enter a parse tree produced by TyCParser#for_var_decl.
    def enterFor_var_decl(self, ctx:TyCParser.For_var_declContext):
        pass

    # Exit a parse tree produced by TyCParser#for_var_decl.
    def exitFor_var_decl(self, ctx:TyCParser.For_var_declContext):
        pass


    # Enter a parse tree produced by TyCParser#for_cond.
    def enterFor_cond(self, ctx:TyCParser.For_condContext):
        pass

    # Exit a parse tree produced by TyCParser#for_cond.
    def exitFor_cond(self, ctx:TyCParser.For_condContext):
        pass


    # Enter a parse tree produced by TyCParser#for_update.
    def enterFor_update(self, ctx:TyCParser.For_updateContext):
        pass

    # Exit a parse tree produced by TyCParser#for_update.
    def exitFor_update(self, ctx:TyCParser.For_updateContext):
        pass


    # Enter a parse tree produced by TyCParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:TyCParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:TyCParser.Switch_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#switch_body.
    def enterSwitch_body(self, ctx:TyCParser.Switch_bodyContext):
        pass

    # Exit a parse tree produced by TyCParser#switch_body.
    def exitSwitch_body(self, ctx:TyCParser.Switch_bodyContext):
        pass


    # Enter a parse tree produced by TyCParser#switch_item_list.
    def enterSwitch_item_list(self, ctx:TyCParser.Switch_item_listContext):
        pass

    # Exit a parse tree produced by TyCParser#switch_item_list.
    def exitSwitch_item_list(self, ctx:TyCParser.Switch_item_listContext):
        pass


    # Enter a parse tree produced by TyCParser#switch_item.
    def enterSwitch_item(self, ctx:TyCParser.Switch_itemContext):
        pass

    # Exit a parse tree produced by TyCParser#switch_item.
    def exitSwitch_item(self, ctx:TyCParser.Switch_itemContext):
        pass


    # Enter a parse tree produced by TyCParser#case_clause.
    def enterCase_clause(self, ctx:TyCParser.Case_clauseContext):
        pass

    # Exit a parse tree produced by TyCParser#case_clause.
    def exitCase_clause(self, ctx:TyCParser.Case_clauseContext):
        pass


    # Enter a parse tree produced by TyCParser#default_clause.
    def enterDefault_clause(self, ctx:TyCParser.Default_clauseContext):
        pass

    # Exit a parse tree produced by TyCParser#default_clause.
    def exitDefault_clause(self, ctx:TyCParser.Default_clauseContext):
        pass


    # Enter a parse tree produced by TyCParser#case_expr.
    def enterCase_expr(self, ctx:TyCParser.Case_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#case_expr.
    def exitCase_expr(self, ctx:TyCParser.Case_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#case_add.
    def enterCase_add(self, ctx:TyCParser.Case_addContext):
        pass

    # Exit a parse tree produced by TyCParser#case_add.
    def exitCase_add(self, ctx:TyCParser.Case_addContext):
        pass


    # Enter a parse tree produced by TyCParser#case_mul.
    def enterCase_mul(self, ctx:TyCParser.Case_mulContext):
        pass

    # Exit a parse tree produced by TyCParser#case_mul.
    def exitCase_mul(self, ctx:TyCParser.Case_mulContext):
        pass


    # Enter a parse tree produced by TyCParser#case_unary.
    def enterCase_unary(self, ctx:TyCParser.Case_unaryContext):
        pass

    # Exit a parse tree produced by TyCParser#case_unary.
    def exitCase_unary(self, ctx:TyCParser.Case_unaryContext):
        pass


    # Enter a parse tree produced by TyCParser#case_primary.
    def enterCase_primary(self, ctx:TyCParser.Case_primaryContext):
        pass

    # Exit a parse tree produced by TyCParser#case_primary.
    def exitCase_primary(self, ctx:TyCParser.Case_primaryContext):
        pass


    # Enter a parse tree produced by TyCParser#break_stmt.
    def enterBreak_stmt(self, ctx:TyCParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#break_stmt.
    def exitBreak_stmt(self, ctx:TyCParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#continue_stmt.
    def enterContinue_stmt(self, ctx:TyCParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#continue_stmt.
    def exitContinue_stmt(self, ctx:TyCParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#return_stmt.
    def enterReturn_stmt(self, ctx:TyCParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#return_stmt.
    def exitReturn_stmt(self, ctx:TyCParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#return_expr.
    def enterReturn_expr(self, ctx:TyCParser.Return_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#return_expr.
    def exitReturn_expr(self, ctx:TyCParser.Return_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#expr_stmt.
    def enterExpr_stmt(self, ctx:TyCParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by TyCParser#expr_stmt.
    def exitExpr_stmt(self, ctx:TyCParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by TyCParser#expr.
    def enterExpr(self, ctx:TyCParser.ExprContext):
        pass

    # Exit a parse tree produced by TyCParser#expr.
    def exitExpr(self, ctx:TyCParser.ExprContext):
        pass


    # Enter a parse tree produced by TyCParser#assign_expr.
    def enterAssign_expr(self, ctx:TyCParser.Assign_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#assign_expr.
    def exitAssign_expr(self, ctx:TyCParser.Assign_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#lhs.
    def enterLhs(self, ctx:TyCParser.LhsContext):
        pass

    # Exit a parse tree produced by TyCParser#lhs.
    def exitLhs(self, ctx:TyCParser.LhsContext):
        pass


    # Enter a parse tree produced by TyCParser#logic_or_expr.
    def enterLogic_or_expr(self, ctx:TyCParser.Logic_or_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#logic_or_expr.
    def exitLogic_or_expr(self, ctx:TyCParser.Logic_or_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#logic_and_expr.
    def enterLogic_and_expr(self, ctx:TyCParser.Logic_and_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#logic_and_expr.
    def exitLogic_and_expr(self, ctx:TyCParser.Logic_and_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#equality_expr.
    def enterEquality_expr(self, ctx:TyCParser.Equality_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#equality_expr.
    def exitEquality_expr(self, ctx:TyCParser.Equality_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#relational_expr.
    def enterRelational_expr(self, ctx:TyCParser.Relational_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#relational_expr.
    def exitRelational_expr(self, ctx:TyCParser.Relational_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#additive_expr.
    def enterAdditive_expr(self, ctx:TyCParser.Additive_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#additive_expr.
    def exitAdditive_expr(self, ctx:TyCParser.Additive_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#multiplicative_expr.
    def enterMultiplicative_expr(self, ctx:TyCParser.Multiplicative_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#multiplicative_expr.
    def exitMultiplicative_expr(self, ctx:TyCParser.Multiplicative_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#unary_expr.
    def enterUnary_expr(self, ctx:TyCParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#unary_expr.
    def exitUnary_expr(self, ctx:TyCParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#prefix_expr.
    def enterPrefix_expr(self, ctx:TyCParser.Prefix_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#prefix_expr.
    def exitPrefix_expr(self, ctx:TyCParser.Prefix_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#postfix_expr.
    def enterPostfix_expr(self, ctx:TyCParser.Postfix_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#postfix_expr.
    def exitPostfix_expr(self, ctx:TyCParser.Postfix_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#postfix_suffix.
    def enterPostfix_suffix(self, ctx:TyCParser.Postfix_suffixContext):
        pass

    # Exit a parse tree produced by TyCParser#postfix_suffix.
    def exitPostfix_suffix(self, ctx:TyCParser.Postfix_suffixContext):
        pass


    # Enter a parse tree produced by TyCParser#primary_expr.
    def enterPrimary_expr(self, ctx:TyCParser.Primary_exprContext):
        pass

    # Exit a parse tree produced by TyCParser#primary_expr.
    def exitPrimary_expr(self, ctx:TyCParser.Primary_exprContext):
        pass


    # Enter a parse tree produced by TyCParser#struct_literal.
    def enterStruct_literal(self, ctx:TyCParser.Struct_literalContext):
        pass

    # Exit a parse tree produced by TyCParser#struct_literal.
    def exitStruct_literal(self, ctx:TyCParser.Struct_literalContext):
        pass


    # Enter a parse tree produced by TyCParser#argument_list.
    def enterArgument_list(self, ctx:TyCParser.Argument_listContext):
        pass

    # Exit a parse tree produced by TyCParser#argument_list.
    def exitArgument_list(self, ctx:TyCParser.Argument_listContext):
        pass


    # Enter a parse tree produced by TyCParser#argument_tail.
    def enterArgument_tail(self, ctx:TyCParser.Argument_tailContext):
        pass

    # Exit a parse tree produced by TyCParser#argument_tail.
    def exitArgument_tail(self, ctx:TyCParser.Argument_tailContext):
        pass



del TyCParser