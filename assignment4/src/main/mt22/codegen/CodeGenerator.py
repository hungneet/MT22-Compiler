from Emitter import Emitter
from functools import reduce
from Utils import *
from Frame import Frame
from abc import ABC
from Visitor import *
# from main.mt22.utils.AST import *
from AST import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
    
class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("printFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("readBoolean", MType([], BooleanType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType([], StringType()), CName(self.libName)),
                Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),
                
                # Will be handle later
                Symbol("super", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("preventDefault", MType([StringType()], VoidType()), CName(self.libName)),
                ]

    def gen(self, ctx, path):
        # ctx: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ctx, gl, path)
        gc.visit(ctx, None)

class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        self.value = value

class CName(Val):
    def __init__(self, value):
        self.value = value

class CodeGenVisitor(Visitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.className = "MT22Class"
        self.path = path
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.listVarGlobal = []
        self.listArrayGlobal = []

    def getTypeLiteral(self, literal):
        if type(literal).__name__ == "IntegerLit":
            return IntegerType()
        if type(literal).__name__ == "FloatLit":
            return FloatType()
        if type(literal).__name__ == "StringLit":
            return StringType()
        if type(literal).__name__ == "BooleanLit":
            return BooleanType()
        if type(literal).__name__ == "ArrayLit":
            # explist:List[Literal]
            eleType = self.getTypeLiteral(literal.explist[0])
            arrayDimen = ([len(literal.explist)] + eleType.dimensions) if isinstance(eleType,ArrayType) else [len(literal.explist)]
            while isinstance(eleType, ArrayType):
                eleType = eleType.eleType

            return ArrayType(eleType, arrayDimen)

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decls:
            e = self.visit(x, e)
        # generate default constructor
        self.getInit()
        self.genMETHOD(FuncDecl("<init>", None, list(), None, BlockStmt( list())), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def getInit(self):
        methodname, methodtype = "<clinit>", MType([], VoidType())
        frame = Frame(methodname, methodtype.rettype)
        code = self.emit.emitMETHOD(methodname, methodtype, False, frame)
        self.emit.printout(code)
        frame.enterScope(True)

        for item in self.listVarGlobal:
            if type(item).__name__ == "VarDecl":
                init_code, init_type = self.visit(item.init, Access(frame, None, False, True))
                self.emit.printout(init_code)
                code = self.emit.emitPUTSTATIC(self.className + "/" + item.name, init_type, frame)
                self.emit.printout(code)
        for item in self.listArrayGlobal:
            size = item.varDimen[0]
            frame.push()
            initCode, initType = self.visit(item.varInit, Access(frame, None, False, True))
            self.emit.printout(self.emit.emitInitNewStaticArray(self.className + "/" + item.variable.name, size, self.getTypeLiteral(item.varInit).eleType, frame, initCode))

        code = self.emit.emitRETURN(methodtype.rettype, frame)
        self.emit.printout(code)
        code = self.emit.emitENDMETHOD(frame)
        self.emit.printout(code)

        frame.exitScope()

    def genMETHOD(self, ctx, o, frame):
        isInit = ctx.return_type is None
        isMain = ctx.name == "main" and len(
            ctx.params) == 0 and type(ctx.return_type) is VoidType
        returnType = VoidType() if isInit else ctx.return_type
        methodName = "<init>" if isInit else ctx.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.typ, ctx.params))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))
        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), ctx.params, SubBody(frame, []))
            print("a", glenv.sym)
            print("b", local.sym)
            glenv.sym = local.sym + glenv.sym

        body = ctx.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.body))
        if ctx.inherit:
            for x in body.body:
                if type(x) is CallStmt:
                    if x.name == "super":
                        superStmt = CallStmt(ctx.inherit, x.args)
                        self.visit(superStmt, SubBody(frame, glenv))
                    elif x.name == "preventDefault":
                        continue
                    else:
                        self.visit(x, SubBody(frame, glenv))
                else:
                    self.visit(x, SubBody(frame, glenv))
        else:
            list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.body))


        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ctx, o):
        frame = Frame(ctx.name, ctx.return_type)
        self.genMETHOD(ctx, o, frame)
        params = [x.typ for x in ctx.params]
        if ctx.inherit:
            sym = Utils.lookup(ctx.inherit, o.sym, lambda x: x.name)
            print(sym)
        return Symbol(ctx.name, MType([x.typ for x in ctx.params], ctx.return_type), CName(self.className))

    def visitParamDecl(self, ctx, o):
        idx = o.frame.getNewIndex()
        return Symbol(ctx.name, ctx.typ, Index(idx))

    # Expressions
    def visitIntegerType(self, ctx, o): pass
    def visitFloatType(self, ctx, o): pass
    def visitBooleanType(self, ctx, o): pass
    def visitStringType(self, ctx, o): pass
    def visitArrayType(self, ctx, o): pass
    def visitAutoType(self, ctx, o): pass
    def visitVoidType(self, ctx, o): pass

    def visitVarDecl(self, ctx, o):
        if o.frame is None: # global
            code = self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False, ctx.init)
            self.emit.printout(code)
            o.sym += [Symbol(ctx.name, ctx.typ, CName(self.className))]

            if ctx.init is not None:
                varType = self.getTypeLiteral(ctx.init)
                if type(varType).__name__ == 'ArrayType':
                    self.listArrayGlobal += [ctx]
                else:
                    self.listVarGlobal += [ctx]
            return o

        idx = o.frame.getNewIndex()
        code = self.emit.emitVAR(idx, ctx.name, ctx.typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
        self.emit.printout(code)
        o.sym.sym += [Symbol(ctx.name, ctx.typ, Index(idx))]

        if ctx.init is not None:
            varType = self.getTypeLiteral(ctx.init)
            if type(varType).__name__ != "ArrayType":
                initCode, initType = self.visit(ctx.init, Access(o.frame, o.sym, False, True))
                initCode += self.emit.emitWRITEVAR(ctx.name, initType, idx, o.frame)
                self.emit.printout(initCode)
            else:
                o.frame.push()
                initCode, initType = self.visit(ctx.init, Access(o.frame, o.sym, False, True))
                self.emit.printout(self.emit.emitInitNewLocalArray(idx, ctx.typ.dimensions[0], ctx.typ.typ, o.frame, initCode))
        return o

    # -------------- Visit stmts -------------- #

    def visitCall(self, ctx, o, isStmt):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym


        sym = Utils.lookup(ctx.name, nenv, lambda x: x.name)
        print(sym)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for x in ctx.args:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        code = in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ctx.name, ctype, frame)

        if isStmt:
            self.emit.printout(code)
        else:
            return code, ctype.rettype

    def visitAssignStmt(self, ctx, o):
        rcode, rtype = self.visit(ctx.rhs, Access(o.frame, o.sym, False))
        self.emit.printout(rcode)
        lcode, ltype = self.visit(ctx.lhs, Access(o.frame, o.sym, True))
        self.emit.printout(lcode)

    # lhs, rhs
    def visitBlockStmt(self, ctx, o):
        for stmt in ctx.body:
            self.visit(stmt, o)

    # cond, tstmt, fstmt
    def visitIfStmt(self, ctx, o): 
        # Xin mã cho expr
        ec, et = self.visit(ctx.cond, Access(o.frame, o.sym, False, True))
        self.emit.printout(ec)
        # Xin từ frame: fLabel
        fLabel = o.frame.getNewLabel()

        # Nhảy đến fLabel nếu false
        code = self.emit.emitIFFALSE(fLabel, o.frame)
        self.emit.printout(code)

        # Sinh mã cho tstmt
        print(ctx.tstmt)
        self.visit(ctx.tstmt, o)
        if ctx.fstmt is None:
            # Đặt fLabel tại đây
            code = self.emit.emitLABEL(fLabel, o.frame)
            self.emit.printout(code)
        else:
            # Xin từ frame: eLabel
            eLabel = o.frame.getNewLabel()
            # Nhảy đến eLabel
            code = self.emit.emitGOTO(eLabel, o.frame)
            self.emit.printout(code)
            # Đặt fLabel tại đây
            code = self.emit.emitLABEL(fLabel, o.frame)
            self.emit.printout(code)
            # Sinh mã fstmt
            self.visit(ctx.fstmt, o)
            # Đặt eLabel tại đây
            code = self.emit.emitLABEL(eLabel, o.frame)
            self.emit.printout(code)

    def visitForStmt(self, ctx, o):

        o.frame.enterLoop()

        # Sinh mã cho init
        print(ctx.init)
        self.visit(ctx.init, o)

        # Xin từ frame: cntLabel, brkLabel
        cntLabel = o.frame.getContinueLabel()
        brkLabel = o.frame.getBreakLabel()

        # Đặt cntLabel tại đây
        code = self.emit.emitLABEL(cntLabel, o.frame)
        self.emit.printout(code)

        # Sinh mã cho cond
        code = self.visit(ctx.cond, Access(o.frame, o.sym, False, True))[0]
        self.emit.printout(code)

        # Nhảy đến break nếu false
        code = self.emit.emitIFFALSE(brkLabel, o.frame)
        self.emit.printout(code)

        # Sinh mã cho stmt
        self.visit(ctx.stmt, o)

        # Sinh mã cho update
        assign = AssignStmt(ctx.init.lhs, ctx.upd)
        self.visit(assign, o)
        # code = self.visit(ctx.upd, Access(o.frame, o.sym, False))[0]
        # self.emit.printout(code)

        # Nhảy đến continue
        code = self.emit.emitGOTO(cntLabel, o.frame)
        self.emit.printout(code)

        # Đặt brkLabel
        code = self.emit.emitLABEL(brkLabel, o.frame)
        self.emit.printout(code)

        o.frame.exitLoop()

    def visitWhileStmt(self, ctx, o): 
        o.frame.enterLoop()
        
        # Xin từ frame: cntLabel, brkLabel
        cntLabel = o.frame.getContinueLabel()
        brkLabel = o.frame.getBreakLabel()

        # Đặt cntLabel tại đây
        code = self.emit.emitLABEL(cntLabel, o.frame)
        self.emit.printout(code)

        # Sinh mã cho expr
        code  = self.visit(ctx.cond, Access(o.frame, o.sym, False))[0]
        self.emit.printout(code)

        # Nhảy đến brkLabel nếu False
        code = self.emit.emitIFFALSE(brkLabel, o.frame)
        self.emit.printout(code)


        self.visit(ctx.stmt, o)
        code = self.emit.emitGOTO(cntLabel, o.frame)
        self.emit.printout(code)
        code = self.emit.emitLABEL(brkLabel, o.frame)
        self.emit.printout(code)

        o.frame.exitLoop()

    def visitDoWhileStmt(self, ctx, o): 
        o.frame.enterLoop()

        cntLabel = o.frame.getContinueLabel()
        brkLabel = o.frame.getBreakLabel()


        code = self.emit.emitLABEL(cntLabel, o.frame)
        self.emit.printout(code)

        self.visit(ctx.stmt, o)
        code = self.visit(ctx.cond, Access(o.frame, o.sym, False))[0]
        self.emit.printout(code)


        code = self.emit.emitIFFALSE(brkLabel, o.frame)
        self.emit.printout(code)

        code = self.emit.emitGOTO(cntLabel, o.frame)
        self.emit.printout(code)

        code = self.emit.emitLABEL(brkLabel, o.frame)
        self.emit.printout(code)

        o.frame.exitLoop()

    def visitBreakStmt(self, ctx, o): 
        brkLabel = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(brkLabel, o.frame))
    
    def visitContinueStmt(self, ctx, o): 
        cntLabel = o.frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(cntLabel, o.frame))
    
    def visitReturnStmt(self, ctx, o): 
        # expr:Expr
        retType = o.frame.returnType
        if not type(retType) is VoidType:
            expCode, expType = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
            if isinstance(retType,FloatType) and isinstance(expType, IntegerType):
                expCode = expCode + self.emit.emitI2F(o.frame)
            self.emit.printout(expCode)
        self.emit.printout(self.emit.emitRETURN(retType, o.frame))
    
    def visitCallStmt(self, ctx, o):
        self.visitCall(ctx, o, True)

    # Literals
    def visitIntegerLit(self, ctx, o):
        return self.emit.emitPUSHICONST(ctx.val, o.frame), IntegerType()

    def visitFloatLit(self, ctx, o): 
        return self.emit.emitPUSHFCONST(str(ctx.val), o.frame), FloatType()
    
    def visitStringLit(self, ctx, o): 
        return self.emit.emitPUSHCONST(str(ctx.val), StringType(), o.frame), StringType()

    def visitBooleanLit(self, ctx, o): 
        return self.emit.emitPUSHICONST(ctx.val, o.frame), BooleanType()
    
    def visitArrayLit(self, ctx, o): 
        initCode = ""
        for index in range(len(ctx.explist)):
            litCode, litType = self.visit(ctx.explist[index], o)
            initCode += self.emit.emitDUP(o.frame)
            initCode += self.emit.emitPUSHICONST(index, o.frame)
            initCode += litCode
            initCode += self.emit.emitASTORE(litType, o.frame)
        return initCode, self.getTypeLiteral(ctx)

    def visitBinExpr(self, ctx, o):
        e1c, e1t = self.visit(ctx.left, o)
        e2c, e2t = self.visit(ctx.right, o)

        op = None
        rtype = None

        if type(e1t) == type(e2t):
            rtype = e1t
        elif type(e1t) is IntegerType and type(e2t) is FloatType:
            e1c = e1c + self.emit.emitI2F(o.frame)
            rtype = e2t
        elif type(e2t) is IntegerType and type(e1t) is FloatType:
            e2c = e2c + self.emit.emitI2F(o.frame)
            rtype = e1t

        if ctx.op in ['+', '-']:
            op = self.emit.emitADDOP(ctx.op, rtype, o.frame)
        elif ctx.op in ['*']:
            op = self.emit.emitMULOP(ctx.op, rtype, o.frame)
        elif ctx.op in ['/']:
            if type(e1t) is IntegerType and type(e2t) is IntType:
                e1c = e1c + self.emit.emitI2F(o.frame)
                e2c = e2c + self.emit.emitI2F(o.frame)
                rtype = FloatType()
            op = self.emit.emitMULOP(ctx.op, rt, o.frame)
            
        elif ctx.op in ['%']:
            op = self.emit.emitMOD(o.frame)
            rtype = IntegerType()
        
        elif ctx.op in ['&&']:
            op = self.emit.emitANDOP(o.frame)
            rtype = BooleanType()

        elif ctx.op in ['||']:
            op = self.emit.emitOROP(o.frame)
            rtype = BooleanType()
        

        elif ctx.op in ['::']:
            pass

        elif ctx.op in ['>','>=','<','<=','!=','==']:
            op = self.emit.emitREOP(ctx.op, rtype, o.frame)
            rtype = BooleanType()
        
        return e1c + e2c + op, rtype

    def visitUnExpr(self, ctx, o): 
        ec, et = self.visit(ctx.val, o)
        if ctx.op in ['-']:
            code = self.emit.emitNEGOP(et, o.frame)
        elif ctx.op in ['!']:
            code = self.emit.emitNOT(BooleanType(), o.frame)
            return ec + code, et

    def visitId(self, ctx, o): 
        sym = list(filter(lambda x: x.name == ctx.name, o.sym.sym))[0]

        if o.isLeft is True:
            if type(sym.value) is Index:
                code = self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame)
            else:
                code = self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, sym.mtype, o.frame)
        else:
            if type(sym.value) is Index:
                code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
            else:
                code = self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype, o.frame)

        return code, sym.mtype

    def visitArrayCell(self, ctx, o): 
        arrCode, arrType = self.visit(Id(ctx.name), Access(o.frame, o.sym, False, True))
        idxCode, idxType = self.visit(ctx.cell[0], Access(o.frame, o.sym, False, True))
        if o.isLeft:
            return [arrCode + idxCode, self.emit.emitASTORE(arrType.typ, o.frame)], arrType.typ
        return arrCode + idxCode + self.emit.emitALOAD(arrType.typ, o.frame), arrType.typ

    def visitFuncCall(self, ctx, o): 
        self.visitCall(ctx, o, False)