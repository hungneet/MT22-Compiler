#ID: 2052504
from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce


def flatten(lst):
    return reduce(lambda prev, curr: prev + flatten(curr) if isinstance(curr, list) else prev + [curr], lst, [])


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        decls = ctx.manydecl().accept(self)
        return Program(decls)

    def visitManydecl(self, ctx: MT22Parser.ManydeclContext):
        if ctx.manydecl():
            return list(ctx.decl().accept(self)) + list(ctx.manydecl().accept(self))
        else:
            return ctx.decl().accept(self)

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return ctx.vardecl().accept(self) if ctx.vardecl() else ctx.funcdecl().accept(self)

    # VarDecl

    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.getChild(0) == ctx.simple_vardecl():
            return ctx.simple_vardecl().accept(self)
        else:
            return ctx.full_vardecl().accept(self)

    def visitSimple_vardecl(self, ctx: MT22Parser.Simple_vardeclContext):
        sdecl_list = []
        idlist = ctx.idlist().accept(self)
        dtype = ctx.dtype().accept(self)
        for id in idlist:
            sdecl_list.append(VarDecl(id, dtype))
        return sdecl_list

    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.idlist():
            return [ctx.ID().getText()] + ctx.idlist().accept(self)
        else:
            return [ctx.ID().getText()]

    def visitDtype(self, ctx: MT22Parser.DtypeContext):
        if ctx.atomic_type():
            return ctx.atomic_type().accept(self)
        elif ctx.array_type():
            return ctx.array_type().accept(self)
        elif ctx.VOID_K():
            return VoidType()
        elif ctx.AUTO_K():
            return AutoType()

    def visitAtomic_type(self, ctx: MT22Parser.Atomic_typeContext):
        if ctx.BOOLEAN_K():
            return BooleanType()
        elif ctx.INT_K():
            return IntegerType()
        elif ctx.FLOAT_K():
            return FloatType()
        else:
            return StringType()

    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        return ArrayType(ctx.dimension().accept(self), ctx.atomic_type().accept(self))

    def visitDimension(self, ctx: MT22Parser.DimensionContext):
        return ctx.intlist().accept(self)

    def visitIntlist(self, ctx: MT22Parser.IntlistContext):
        if ctx.intlist():
            return [ctx.INTLIT().getText()] + ctx.intlist().accept(self)
        else:
            return [ctx.INTLIT().getText()]

    def visitFull_vardecl(self, ctx: MT22Parser.Full_vardeclContext):
        idname = ctx.ID().getText()
        exp = ctx.exp().accept(self)
        if ctx.dtype():
            dtype = ctx.dtype().accept(self)
            return [VarDecl(idname, dtype, exp)]
        else:
            fvar = ctx.fullvar_helper().accept(self)
            list = [idname, fvar, exp]
            flatten_list = flatten(list)
            typeindex = int(len(flatten_list)/2)
            dtype = str(flatten_list[typeindex])
            idlist = flatten_list[:typeindex]
            val = flatten_list[typeindex+1:]
            return (map(lambda x, y: VarDecl(x, dtype, y), idlist, val))

    def visitFullvar_helper(self, ctx: MT22Parser.Fullvar_helperContext):
        if ctx.dtype():
            return [ctx.ID().getText(), ctx.dtype().accept(self), ctx.exp().accept(self)]
        else:
            return [ctx.ID().getText(), ctx.fullvar_helper().accept(self), ctx.exp().accept(self)]
    # Expression

    def visitExp(self, ctx: MT22Parser.ExpContext):
        if ctx.index_opp():
            return ctx.index_opp().accept(self)
        elif ctx.getChildCount() == 2:
            return UnExpr(ctx.getChild(0).getText(), ctx.getChild(1).accept(self))
        elif ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), ctx.getChild(0).accept(self),  ctx.getChild(2).accept(self))
        else:
            return ctx.operand().accept(self)

    def visitIndex_opp(self, ctx: MT22Parser.Index_oppContext):
        idname = ctx.ID().getText()
        exp = ctx.exp_list().accept(self)
        return ArrayCell(idname, exp)

    def visitExp_list(self, ctx: MT22Parser.Exp_listContext):
        if ctx.exp_list():
            return ctx.exp().accept(self) + ctx.exp_list().accept(self)
        else:
            return ctx.exp().accept(self)

    def visitOperand(self, ctx: MT22Parser.OperandContext):
        if ctx.INTLIT():
            return IntegerLit(ctx.INTLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLit(ctx.FLOATLIT().getText())
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.BOOLLIT():
            return BooleanLit(True if ctx.BOOLLIT().getText() == "true" else False)
        elif ctx.ID():
            return Id(str(ctx.ID().getText()))
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        else:
            return ctx.exp().accept(self)

    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return ArrayLit(ctx.nullable_explist().accept(self))

    def visitNullable_explist(self, ctx: MT22Parser.Nullable_explistContext):
        return ctx.exp_list().accept(self) if ctx.exp_list() else []

    def visitExp_list(self, ctx: MT22Parser.Exp_listContext):
        if ctx.exp_list():
            return [ctx.exp().accept(self)] + ctx.exp_list().accept(self)
        else:
            return [ctx.exp().accept(self)]

    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        return FuncCall(ctx.ID().getText(), ctx.argument_list().accept(self))

    def visitArgument_list(self, ctx: MT22Parser.Argument_listContext):
        return ctx.exp_list().accept(self) if ctx.exp_list() else []

    # Funcdecl

    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        dtype = ctx.dtype().accept(self)
        fname = ctx.getChild(0).getText()
        paralist = ctx.nullable_paralist().accept(self)
        inherit = ctx.inherit().accept(self)
        blockstmt = ctx.blockstmt().accept(self)
        return [FuncDecl(fname, dtype, paralist, inherit, blockstmt)]

    def visitInherit(self, ctx: MT22Parser.InheritContext):
        if ctx.INHERIT_K():
            return ctx.ID().getText()
        else:
            return None

    def visitNullable_paralist(self, ctx: MT22Parser.Nullable_paralistContext):
        return ctx.paralist().accept(self) if ctx.paralist() else []

    def visitParalist(self, ctx: MT22Parser.ParalistContext):
        if ctx.paralist():
            return [ctx.paradecl().accept(self)] + ctx.paralist().accept(self)
        else:
            return [ctx.paradecl().accept(self)]

    def visitParadecl(self, ctx: MT22Parser.ParadeclContext):
        inheritance = True if ctx.INHERIT_K() else False
        out = True if ctx.OUT_K() else False
        idname = ctx.ID().getText()
        dtype = ctx.dtype().accept(self)
        return ParamDecl(idname, dtype, out, inheritance)

    # Statement
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visitChildren(ctx)

        # assignstmt
    def visitAssign_stmt(self, ctx: MT22Parser.Assign_stmtContext):
        return [AssignStmt(ctx.lhs().accept(self), ctx.exp().accept(self))]

    def visitLhs(self, ctx: MT22Parser.LhsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else ctx.index_opp().accept(self)

        # if stmt
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        exp = ctx.exp().accept(self)
        if ctx.getChildCount() == 5:
            stmt = ctx.stmt(0).accept(self)
            if isinstance(stmt, list):
                stmt = stmt[0]
            return [IfStmt(exp, stmt)]
        else:
            ifstmt = ctx.stmt(0).accept(self)
            elstmt = ctx.stmt(1).accept(self)
            if isinstance(ifstmt, list):
                ifstmt = ifstmt[0]
            if isinstance(elstmt, list):
                elstmt = elstmt[0]
            return [IfStmt(exp, ifstmt, elstmt)]
        
        #for stmt
    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        init_exp = AssignStmt(Id(ctx.ID().getText()), ctx.exp(0).accept(self))
        exp1 = ctx.exp(1).accept(self)
        exp2 = ctx.exp(2).accept(self)
        stmt = ctx.stmt().accept(self)
        if isinstance(stmt, list):
                stmt = stmt[0]
        return [ForStmt(init_exp, exp1, exp2, stmt)]
        #while stmt
    def visitWhile_stmt(self,ctx:MT22Parser.While_stmtContext):
        exp= ctx.exp().accept(self)
        stmt= ctx.stmt().accept(self)
        if isinstance(stmt, list):
                stmt = stmt[0]
        return [WhileStmt(exp,stmt)]
        #do while stmt
    def visitDowhile_stmt(self,ctx:MT22Parser.Dowhile_stmtContext):
        blockstmt= ctx.blockstmt().accept(self)
        exp= ctx.exp().accept(self)
        return [DoWhileStmt(exp,blockstmt)]
        #break
    def visitBreak_stmt(self,ctx:MT22Parser.Break_stmtContext):
        return [BreakStmt()]
        #cont
    def visitContinue_stmt(self,ctx:MT22Parser.Continue_stmtContext):
        return [ContinueStmt()]
        #return
    def visitReturn_stmt(self,ctx:MT22Parser.Return_stmtContext):
        return [ReturnStmt(ctx.exp().accept(self) if ctx.exp() else None)]
        #callstmt
    def visitCall_stmt(self,ctx:MT22Parser.Call_stmtContext):
        return  [CallStmt(ctx.ID().getText(), ctx.argument_list().accept(self))]
        # blockstmt
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        content = ctx.contentlist().accept(self) if ctx.contentlist() else []
        return BlockStmt(content)

    def visitContentlist(self, ctx: MT22Parser.ContentlistContext):
        if ctx.contentlist():
            return list(ctx.content().accept(self)) + list(ctx.contentlist().accept(self))
        else:
            return ctx.content().accept(self)
       
    def visitContent(self, ctx: MT22Parser.ContentContext):
        if ctx.blockstmt():
            return [ctx.blockstmt().accept(self)]
        return self.visitChildren(ctx)
