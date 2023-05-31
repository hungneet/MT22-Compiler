from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decllist EOF ;
    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))


    # Visit a parse tree produced by MT22Parser#decllist.
    # decllist: decl decllist | decl ;
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist())


    # Visit a parse tree produced by MT22Parser#decl.
    # decl: vardecl | funcdecl ;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())


    # Visit a parse tree produced by MT22Parser#vardecl.
    # vardecl: vardecl_short_form | vardecl_full_form 
    #        | vardecl_array_full | vardecl_array_short ;
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        if ctx.vardecl_short_form():
            return self.visit(ctx.vardecl_short_form())
        elif ctx.vardecl_full_form():
            return self.visit(ctx.vardecl_full_form())
        elif ctx.vardecl_array_full():
            return self.visit(ctx.vardecl_array_full())
        elif ctx.vardecl_array_short():
            return self.visit(ctx.vardecl_array_short())


    # Visit a parse tree produced by MT22Parser#vardecl_short_form.
    # vardecl_short_form: idlist COLON var_type SEMI ;
    def visitVardecl_short_form(self, ctx:MT22Parser.Vardecl_short_formContext):
        idlist = self.visit(ctx.idlist())
        var_type = self.visit(ctx.var_type())
        return [VarDecl(id, var_type) for id in idlist]


    # Visit a parse tree produced by MT22Parser#vardecl_full_form.
    # vardecl_full_form: ID var_recur expr SEMI ;
    def visitVardecl_full_form(self, ctx:MT22Parser.Vardecl_full_formContext):
        # print("Start vardecl_full_form")
        # print("ctx.expr()")
        eles = {
            "ids": [ctx.ID().getText()],
            "expr": [self.visit(ctx.expr())]
        }
        # print("eles = ",eles)
        return self.visitVar_recur(ctx.var_recur(), eles)


    # Visit a parse tree produced by MT22Parser#var_recur.
    # eles = {"ids": [], "type": "", "exp": []}
    # var_recur: COLON var_type EQ | COMMA ID var_recur expr COMMA ;
    def visitVar_recur(self, ctx:MT22Parser.Var_recurContext, eles):
        if ctx.var_type():
            type = self.visit(ctx.var_type())
            result = []
            # print(eles)
            for i in range(len(eles["ids"])):
                id = eles["ids"][i]
                init = eles["expr"][len(eles["expr"])-1-i]
                result += [VarDecl(id, type, init)]
            return result
        else:
            eles["ids"] = eles["ids"] + [ctx.ID().getText()]
            eles["expr"] = eles["expr"] + [self.visit(ctx.expr())]
            return self.visitVar_recur(ctx.var_recur(), eles)


    # Visit a parse tree produced by MT22Parser#vardecl_array_short.
    # vardecl_array_short: idlist COLON array_type SEMI ;
    def visitVardecl_array_short(self, ctx:MT22Parser.Vardecl_array_shortContext):
        idlist = self.visit(ctx.idlist())
        array_type = self.visit(ctx.array_type())
        return [VarDecl(id, array_type) for id in idlist]


    # Visit a parse tree produced by MT22Parser#vardecl_array_full.
    # vardecl_array_full: ID varecur_array array_value_list SEMI ;
    def visitVardecl_array_full(self, ctx:MT22Parser.Vardecl_array_fullContext):
        eles = {
            "ids": [ctx.ID().getText()],
            "expr": [self.visit(ctx.array_value_list())]
        }
        return self.visitVarecur_array(ctx.varecur_array(), eles)


    # Visit a parse tree produced by MT22Parser#varecur_array.
    # varecur_array: COLON array_type EQ | COMMA ID varecur_array array_value_list COMMA ;
    def visitVarecur_array(self, ctx:MT22Parser.Varecur_arrayContext, eles):
        if ctx.array_type():
            type = self.visit(ctx.array_type())
            result = []
            for i in range(len(eles["ids"])):
                id = eles["ids"][i]
                init = eles["expr"][len(eles["expr"])-1-i]
                result += [VarDecl(id, type, init)]
            return result
        else:
            eles["ids"] = eles["ids"] + [ctx.ID().getText()]
            eles["expr"] = eles["expr"] + [self.visit(ctx.array_value_list())]
            return self.visitVarecur_array(ctx.varecur_array(), eles)


    # Visit a parse tree produced by MT22Parser#dimension.
    # dimension: LSB intlist RSB ;
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visit(ctx.intlist())


    # Visit a parse tree produced by MT22Parser#array_value_list.
    # array_value_list: LCB array_value_prime RCB | expr ;
    def visitArray_value_list(self, ctx:MT22Parser.Array_value_listContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        return ArrayLit(self.visit(ctx.array_value_prime()))


    # Visit a parse tree produced by MT22Parser#array_value_prime.
    # array_value_prime: LCB array_value_prime RCB | array_value | ;
    def visitArray_value_prime(self, ctx:MT22Parser.Array_value_primeContext):
        if ctx.getChildCount() == 0:
            return []
        elif ctx.array_value_prime():
            return [ArrayLit(self.visit(ctx.array_value_prime()))]
        else:
            return self.visit(ctx.array_value())


    # Visit a parse tree produced by MT22Parser#array_value.
    # array_value: exprlist | ;
    def visitArray_value(self, ctx:MT22Parser.Array_valueContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.exprlist())


    # Visit a parse tree produced by MT22Parser#paramlist.
    # paramlist: paramprime | ;
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visitParamprime(ctx.paramprime())


    # Visit a parse tree produced by MT22Parser#paramprime.
    # paramprime: paramdecl COMMA paramprime | paramdecl ;
    def visitParamprime(self, ctx:MT22Parser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visitParamdecl(ctx.paramdecl())]
        return [self.visitParamdecl(ctx.paramdecl())] + self.visitParamprime(ctx.paramprime())


    # Visit a parse tree produced by MT22Parser#paramdecl.
    # paramdecl: INHERIT? OUT? ID COLON (array_type | var_type) ;
    def visitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        inherit = False
        out = False
        if ctx.INHERIT():
            inherit = True
        if ctx.OUT():   
            out = True
        if ctx.array_type():
            return ParamDecl(ctx.ID(), self.visitArray_type(ctx.array_type()), out, inherit)
        return ParamDecl(ctx.ID(), self.visitVar_type(ctx.var_type()), out, inherit)

#  ------------------------- Function Declaration -------------------------- #
    # Visit a parse tree produced by MT22Parser#funcdecl.
    # funcdecl: func_head func_body ;
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        eles = self.visitFunc_head(ctx.func_head())
        if eles["params"] == None:
            eles["params"] = []
        return [FuncDecl(eles["name"], eles["return_type"], eles["params"], eles["inherit"], self.visitFunc_body(ctx.func_body()))]


    # Visit a parse tree produced by MT22Parser#func_head.
    # func_head				    : ID COLON FUNCTION return_type (LB paramlist RB) (INHERIT ID)? ;
    def visitFunc_head(self, ctx:MT22Parser.Func_headContext):
        inherit = None
        if ctx.INHERIT():
            inherit = ctx.ID(1).getText()
        # eles = {}
        # eles["name"] = ctx.ID()
        # eles["return_type"] = self.visit(ctx.return_type())
        # eles["params"] = self.visit(ctx.paramlist())
        # eles["inherit"] = inherit
        eles = {
            "name": ctx.ID(0).getText(),
            "return_type": self.visit(ctx.return_type()),
            "params": self.visit(ctx.paramlist()),
            "inherit": inherit
        }
        return eles


    # Visit a parse tree produced by MT22Parser#func_body.
    # func_body: block_stmt ;
    def visitFunc_body(self, ctx:MT22Parser.Func_bodyContext):
        return self.visit(ctx.block_stmt())


    # Visit a parse tree produced by MT22Parser#element_type.
    # element_type: INTEGER | FLOAT | STRING | BOOLEAN ;
    def visitElement_type(self, ctx:MT22Parser.Element_typeContext):
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.BOOLEAN():
            return BooleanType()


    # Visit a parse tree produced by MT22Parser#var_type.
    # var_type: element_type | AUTO ;
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.element_type())


    # Visit a parse tree produced by MT22Parser#return_type.
    # return_type				: var_type | VOID | array_type ;
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        if ctx.var_type():
            return self.visit(ctx.var_type())
        elif ctx.VOID():
            return VoidType()
        return self.visit(ctx.array_type())


    # Visit a parse tree produced by MT22Parser#array_type.
    # array_type: ARRAY dimension OF element_type ;
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.dimension()), self.visit(ctx.element_type()))


    # Visit a parse tree produced by MT22Parser#idlist.
    # idlist: ID COMMA idlist | ID ;
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())


    # Visit a parse tree produced by MT22Parser#intlist.
    # intlist: INTLIT COMMA intlist | INTLIT ;
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.intlist())

# ------------------------- Expression -------------------------- #
    # Visit a parse tree produced by MT22Parser#array.
    # array_lit: LCB exprlist? RCB ;
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        # print("ctx.exprlist()")
        if ctx.exprlist():
            return ArrayLit(self.visit(ctx.exprlist()))
        return ArrayLit([])


    # Visit a parse tree produced by MT22Parser#exprlist.
    # exprlist: expr COMMA exprlist | expr ;
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 1:
            # print("ctx.expr()")
            return [self.visit(ctx.expr())]
        # print("[ctx.expr()] + ctx.exprlist()")
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())


    # Visit a parse tree produced by MT22Parser#expr.
    # expr: expr1 DOUBLE_COLON expr1 | expr1 ;
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.DOUBLE_COLON():
            return BinExpr(ctx.DOUBLE_COLON().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1(0))


    # Visit a parse tree produced by MT22Parser#expr1.
    # expr1: expr2 relational expr2 | expr2 ;
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.relational():
            return BinExpr(ctx.relational().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.expr2(0))


    # Visit a parse tree produced by MT22Parser#expr2.
    # expr2: expr2 (BOOL_CONJ | BOOL_DISJ) expr3 | expr3 ;
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.expr2():
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())


    # Visit a parse tree produced by MT22Parser#expr3.
    # expr3: expr3 (ADD | SUB) expr4 | expr4 ;
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.expr3():
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())


    # Visit a parse tree produced by MT22Parser#expr4.
    # expr4: expr4 (MUL | DIV | REMAINDER) expr5 | expr5 ;
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.expr4():
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())


    # Visit a parse tree produced by MT22Parser#expr5.
    # expr5				: BOOL_NEGA expr5 | expr6 ;
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.expr5():
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())


    # Visit a parse tree produced by MT22Parser#expr6.
    # expr6: SUB expr6 | expr7 ;
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.expr6():
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())

    # Visit a parse tree produced by MT22Parser#expr7.
    # expr7				: indexOperator | operands ;
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.indexOperator():
            return self.visit(ctx.indexOperator())
        # print("ctx.operands()")
        return self.visit(ctx.operands())


    # Visit a parse tree produced by MT22Parser#relational.
    # relational: EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_EQ | GREATER_THAN_EQ ;
    # def visitRelational(self, ctx:MT22Parser.RelationalContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexOperator.
    # indexOperator: ID LSB exprlist RSB ;
    def visitIndexOperator(self, ctx:MT22Parser.IndexOperatorContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.exprlist()))


    # Visit a parse tree produced by MT22Parser#allLiterals.
    # allLiterals: (INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit) ;
    def visitAllLiterals(self, ctx:MT22Parser.AllLiteralsContext):
        if ctx.INTLIT():
            # print("INTLIT()")
            # print("Value = ",int(ctx.INTLIT().getText()))
            return IntegerLit(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            result = ctx.FLOATLIT().getText()
            if len(result) > 1:
                if (result[0] == "." and (result[1] == "E" or result[1] == "e")):
                    result = "0.0"
            return FloatLit(float(result))
        if ctx.BOOLLIT():
            return BooleanLit(True) if ctx.BOOLLIT().getText() == "true" else BooleanLit(False)
        if ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        if ctx.array_lit():
            # print("ArrayLit, ctx.array()")
            return self.visit(ctx.array_lit())


    # Visit a parse tree produced by MT22Parser#funcCall.
    # funcCall: ID LB argulist RB ;
    def visitFuncCall(self, ctx:MT22Parser.FuncCallContext):
        return FuncCall(ctx.ID(), self.visit(ctx.argulist()))


    # Visit a parse tree produced by MT22Parser#argulist.
    # argulist: arguprime | ;
    def visitArgulist(self, ctx:MT22Parser.ArgulistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.arguprime())


    # Visit a parse tree produced by MT22Parser#arguprime.
    # arguprime: argu COMMA arguprime | argu ;
    def visitArguprime(self, ctx:MT22Parser.ArguprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.argu())]
        return [self.visit(ctx.argu())] + self.visit(ctx.arguprime())


    # Visit a parse tree produced by MT22Parser#argu.
    # argu: operands | expr ;
    def visitArgu(self, ctx:MT22Parser.ArguContext):
        if ctx.operands():
            return self.visit(ctx.operands())
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MT22Parser#operands.
    # operands: ID | allLiterals | funcCall | LB expr RB ;
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        if ctx.allLiterals():
            # print("ctx.allLiterals()")
            return self.visit(ctx.allLiterals())
        elif ctx.expr():
            # print("ctx.expr()")
            return self.visit(ctx.expr())
        elif ctx.funcCall():
            return self.visit(ctx.funcCall())
        return Id(ctx.ID().getText())

# ------------------------ Statement ------------------------ #
    # Visit a parse tree produced by MT22Parser#stmtlist.
    # stmtlist: stmt stmtlist | ;
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())


    # Visit a parse tree produced by MT22Parser#stmt.
    # stmt: vardecl | assign_stmt | if_stmt | for_stmt 
    #     | while_stmt | dowhile_stmt | break_stmt | continue_stmt 
    #     | return_stmt | call_stmt | block_stmt ;
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        # if ctx.vardecl():
        #     return self.visit(ctx.vardecl())
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        if ctx.while_stmt():
            # print("ctx.while_stmt()")
            return self.visit(ctx.while_stmt())
        if ctx.dowhile_stmt():
            return self.visit(ctx.dowhile_stmt())
        if ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        if ctx.call_stmt():
            return self.visit(ctx.call_stmt())
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())


    # Visit a parse tree produced by MT22Parser#body_stmt.
    # body_stmt: block_stmt | stmt | SEMI ;
    def visitBody_stmt(self, ctx:MT22Parser.Body_stmtContext):
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        elif ctx.stmt():
            return self.visit(ctx.stmt())
        else:
            return None


    # Visit a parse tree produced by MT22Parser#boolean_exprlist.
    # boolean_exprlist: expr ;
    def visitBoolean_exprlist(self, ctx:MT22Parser.Boolean_exprlistContext):
        # print("ctx.expr()")
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    # assign_stmt: (ID | ID LSB exprlist RSB) EQ expr SEMI ;
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        if ctx.exprlist():
            return AssignStmt(ArrayCell(ctx.ID().getText(), self.visit(ctx.exprlist())), self.visit(ctx.expr()))
        return AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr()))


    # Visit a parse tree produced by MT22Parser#if_stmt.
    # if_stmt			: IF (LB boolean_exprlist RB) body_stmt (ELSE body_stmt)? ;
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        # print("If_stmt start")
        # print("ctx.boolean_exprlist()")
        cond = self.visit(ctx.boolean_exprlist())
        tstmt = self.visit(ctx.body_stmt(0))
        if ctx.ELSE():
            fstmt = self.visit(ctx.body_stmt(1))
            return IfStmt(cond, tstmt, fstmt)
        return IfStmt(cond, tstmt)

            


    # Visit a parse tree produced by MT22Parser#for_stmt.
    # for_stmt: FOR (LB init_var COMMA expr COMMA update_expr RB) body_stmt ;
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        init = self.visit(ctx.init_var())
        cond = self.visit(ctx.expr())
        upd = self.visit(ctx.update_expr())
        stmt = self.visit(ctx.body_stmt())
        return ForStmt(init, cond, upd, stmt)


    # Visit a parse tree produced by MT22Parser#update_expr.
    # update_expr: expr |  ;
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        return None


    # Visit a parse tree produced by MT22Parser#init_var.
    # init_var: (ID | ID LSB exprlist RSB) EQ expr ;
    def visitInit_var(self, ctx:MT22Parser.Init_varContext):
        if ctx.exprlist():
            return AssignStmt(ArrayCell(ctx.ID().getText(), self.visit(ctx.exprlist())), self.visit(ctx.expr()))
        return AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr()))


    # Visit a parse tree produced by MT22Parser#while_stmt.
    # while_stmt: WHILE (LB boolean_exprlist RB) body_stmt ;
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        # print("ctx.boolean_exprlist()")
        cond = self.visit(ctx.boolean_exprlist())
        # print("ctx.body_stmt()")
        stmt = self.visit(ctx.body_stmt())
        return WhileStmt(cond, stmt)


    # Visit a parse tree produced by MT22Parser#dowhile_stmt.
    # dowhile_stmt: DO block_stmt WHILE (LB boolean_exprlist RB) SEMI ;
    def visitDowhile_stmt(self, ctx:MT22Parser.Dowhile_stmtContext):
        cond = self.visit(ctx.boolean_exprlist())
        stmt = self.visit(ctx.block_stmt())
        return DoWhileStmt(cond, stmt)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    # break_stmt: BREAK SEMI ; 
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    # continue_stmt: CONTINUE SEMI ; 
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_stmt.
    # return_stmt		: RETURN expr? SEMI ; 
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()


    # Visit a parse tree produced by MT22Parser#call_stmt.
    # call_stmt: ID LB callElementList RB SEMI ; 
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.callElementList()))
    

    # callElementList: callElementPrime | ;
    def visitCallElementList(self, ctx:MT22Parser.CallElementListContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.callElementPrime())
    

    # callElementPrime	: expr COMMA callElementPrime | expr ;
    def visitCallElementPrime(self, ctx:MT22Parser.CallElementPrimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.callElementPrime())


    # Visit a parse tree produced by MT22Parser#block_stmt.
    # block_stmt: LCB blocklist RCB ;
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return BlockStmt(self.visit(ctx.blocklist()))
    

    # Visit a parse tree produced by MT22Parser#blocklist.
    # blocklist: block_prime | ;
    def visitBlocklist(self, ctx:MT22Parser.BlocklistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.block_prime())


    # Visit a parse tree produced by MT22Parser#block_prime.
    # block_prime: block block_prime | block ;
    def visitBlock_prime(self, ctx:MT22Parser.Block_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.block())
        return self.visit(ctx.block()) + self.visit(ctx.block_prime())


    # Visit a parse tree produced by MT22Parser#block.
    # block: stmt | vardecl ;
    def visitBlock(self, ctx:MT22Parser.BlockContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())]
        return self.visit(ctx.vardecl())