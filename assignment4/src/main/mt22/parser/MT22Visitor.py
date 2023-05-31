# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl_short_form.
    def visitVardecl_short_form(self, ctx:MT22Parser.Vardecl_short_formContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl_full_form.
    def visitVardecl_full_form(self, ctx:MT22Parser.Vardecl_full_formContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_recur.
    def visitVar_recur(self, ctx:MT22Parser.Var_recurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl_array_short.
    def visitVardecl_array_short(self, ctx:MT22Parser.Vardecl_array_shortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl_array_full.
    def visitVardecl_array_full(self, ctx:MT22Parser.Vardecl_array_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varecur_array.
    def visitVarecur_array(self, ctx:MT22Parser.Varecur_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_value_list.
    def visitArray_value_list(self, ctx:MT22Parser.Array_value_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_value_prime.
    def visitArray_value_prime(self, ctx:MT22Parser.Array_value_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_value.
    def visitArray_value(self, ctx:MT22Parser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramprime.
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramdecl.
    def visitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_head.
    def visitFunc_head(self, ctx:MT22Parser.Func_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_body.
    def visitFunc_body(self, ctx:MT22Parser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element_type.
    def visitElement_type(self, ctx:MT22Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlist.
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational.
    def visitRelational(self, ctx:MT22Parser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexOperator.
    def visitIndexOperator(self, ctx:MT22Parser.IndexOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#allLiterals.
    def visitAllLiterals(self, ctx:MT22Parser.AllLiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcCall.
    def visitFuncCall(self, ctx:MT22Parser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argulist.
    def visitArgulist(self, ctx:MT22Parser.ArgulistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arguprime.
    def visitArguprime(self, ctx:MT22Parser.ArguprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argu.
    def visitArgu(self, ctx:MT22Parser.ArguContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_lit.
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#body_stmt.
    def visitBody_stmt(self, ctx:MT22Parser.Body_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolean_exprlist.
    def visitBoolean_exprlist(self, ctx:MT22Parser.Boolean_exprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_var.
    def visitInit_var(self, ctx:MT22Parser.Init_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:MT22Parser.Dowhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callElementList.
    def visitCallElementList(self, ctx:MT22Parser.CallElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callElementPrime.
    def visitCallElementPrime(self, ctx:MT22Parser.CallElementPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blocklist.
    def visitBlocklist(self, ctx:MT22Parser.BlocklistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_prime.
    def visitBlock_prime(self, ctx:MT22Parser.Block_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block.
    def visitBlock(self, ctx:MT22Parser.BlockContext):
        return self.visitChildren(ctx)



del MT22Parser