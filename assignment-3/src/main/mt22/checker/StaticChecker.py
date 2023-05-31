#ID: 2052504

from Visitor import Visitor
from AST import *
from StaticError import *
from abc import ABC
from functools import reduce


class Symbol(ABC):
    def __init__(self, name, typ, kind=Function(), inherit=None, param=None, isGlobal=False):
        self.name = name
        self.typ = typ
        self.param = param
        self.kind = kind
        self.isGlobal = isGlobal
        self.inherit = inherit

    def return_type(self):
        return self.typ

class Loop(ABC):
    pass


class IfStmt(ABC):
    pass

class StaticChecker(Visitor):

    def __init__(self, ast):
        self.ast = ast
        self.inherit_decl = False
        self.special_func = [Symbol("readInteger", IntegerType, CallStmt),
                   Symbol(name="printInteger", typ= IntegerType,kind = CallStmt),
                   Symbol("readFloat", FloatType, CallStmt),
                   Symbol("writeFloat", FloatType, CallStmt),
                   Symbol("readBoolean", BooleanType, CallStmt),
                   Symbol("printBoolean", BooleanType, CallStmt),
                   Symbol("readString", StringType, CallStmt),
                   Symbol("printString", StringType, CallStmt),
                   Symbol("super", VoidType, CallStmt),
                   Symbol("preventDefault", VoidType, CallStmt)]
        self.func_list = []

    def check(self):
        return self.visit(self.ast, [])
    
    def visitDeclarations(self, declarations, body):
        # Visit each declaration in the list and update the body
        for decl in declarations:
            body = self.visit(decl, body)
        return body
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
    def visitDoWhileStmt(self, ast, param):
        cond = self.visit(ast.cond, param)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInVarDecl(ast)
        env = [[Symbol(None, None, Loop())]] + param
        self.visit(ast.stmt, env)
        return param

    def visitBreakStmt(self, ast, param):
        for pare in param:
            for joiner in pare:
                if isinstance(joiner, Symbol) and isinstance(joiner.kind, Loop):
                    return BreakStmt()
        raise MustInLoop(ast)


    def visitContinueStmt(self, ast, param):
        for pare in param:
            for joiner in pare:
                if isinstance(joiner, Symbol) and isinstance(joiner.kind, Loop):
                    return ContinueStmt()
        raise MustInLoop(ast)

    def visitReturnStmt(self, ast, param):
        type_ret = self.visit(ast.expr, param) if ast.expr is not None else None
        for pare in param:
            for joiner in pare:
                if isinstance(joiner, Symbol) and isinstance(joiner.kind, Function):
                    if isinstance(joiner.typ, type(type_ret)):
                        return joiner.typ
                    if isinstance(joiner.typ, AutoType):
                        joiner.typ = type_ret or VoidType()
                        return joiner.typ
                    if isinstance(joiner.typ, VoidType) and type_ret is None:
                        return joiner.typ
                    if not isinstance(joiner.typ, type(type_ret)):
                        raise TypeMismatchInStatement(ast)
        raise TypeMismatchInStatement(ast)

    def visitUnExpr(self, ast, param):
        et = self.visit(ast.val, param)

        if isinstance(et, AutoType):
            raise Invalid(Variable(), ast.val.name)

        if ast.op == '!':
            if not isinstance(et, BooleanType):
                raise TypeMismatchInExpression(ast)
            return BooleanType()

        if ast.op == '-':
            if not isinstance(et, (IntegerType, FloatType)):
                raise TypeMismatchInExpression(ast)
            return IntegerType() if isinstance(et, IntegerType) else FloatType()

    def visitCallStmt(self, ast, param):
        def check_name(astc, lst):
            # find environment program
            for pare in lst:
                for joiner in pare:
                    if type(joiner) is Symbol:
                        continue
                    if joiner.name == astc.name and type(joiner) is FuncDecl:
                        if joiner.return_type is AutoType:
                            joiner.return_type = VoidType()
                        return True, joiner
            return False, None
        if not any (joiner.name == ast.name for joiner in self.special_func):
            o, func = check_name(ast, param)
            if o is False:
                raise Undeclared(Function(), ast.name)

            # create env param
            param_func = [[]] + param
            for paramdecl in func.params:
                # get all env parameters
                param_func = self.visit(paramdecl, param_func)
            if len(ast.args) != len(param_func[0]):
                raise TypeMismatchInStatement(ast)
            for i in range(0, len(ast.args)):
                if type(param_func[0][i].typ) is not AutoType:
                    typ_ast = self.visit(ast.args[i], param)
                    if type(param_func[0][i].typ) is not type(typ_ast):
                        raise TypeMismatchInStatement(ast)
        elif ast.name == "super":
            return ast.args
        elif ast.name in ["readInteger", "readFloat","readString","readBoolean", "preventDefault"]:
            if len(ast.args) != 0:
                raise TypeMismatchInStatement(ast)
        elif ast.name in ["printInteger", "writeFloat","printString","printBoolean"]:
            if len(ast.args) != 1:
                raise TypeMismatchInStatement(ast)
            for joiner in self.special_func:
                if joiner.name == ast.name:
                    typ = self.visit(ast.args[0], param)
                    if type(typ) is not joiner.typ:
                        raise TypeMismatchInStatement(ast)
        return param


    def visitFuncCall(self, ast, param):
        for pare in param:
            for joiner in pare:
                if isinstance(joiner, FuncDecl) and joiner.name == ast.name:
                    func = joiner
                    break
            else:
                continue
            break
        else:
            raise Undeclared(Function(), ast.name)

        if len(ast.args) != len(func.params):
            raise TypeMismatchInExpression(ast)
        return func.return_type


    def visitAssignStmt(self, ast, param):
        right = self.visit(ast.rhs, param)
        left = self.visit(ast.lhs, param)

        if isinstance(right, VoidType):
            raise TypeMismatchInExpression(ast)

        if isinstance(right, AutoType) and isinstance(ast.rhs, FuncCall):
            raise Invalid(Variable(), ast.rhs.name)

        if not isinstance(right, type(left)) and not isinstance(left, AutoType):
            raise TypeMismatchInExpression(ast)

        if isinstance(right, AutoType):
            for par in param:
                for p in par:
                    if isinstance(p, Symbol):
                        continue
                    elif isinstance(p, FuncDecl) and p.name == ast.rhs.name:
                        if isinstance(p.return_type, AutoType) and isinstance(ast.lhs.typ, AutoType):
                            raise Invalid(Function(), p.name)
                        if isinstance(p.return_type, AutoType) and not isinstance(ast.lhs.typ, AutoType):
                            p.return_type = self.visit(ast.lhs.typ, param)
                            break
                        
        for p in [p for par in param for p in par if p.name == ast.lhs.name and isinstance(p.typ, AutoType)]:
            p.typ = self.visit(right, param)
            break
        return param


    def visitBlockStmt(self, ast, param):

        if not param:
            return param
        func = param[0][0]
        first_stmt = ast.body[0] if len(ast.body) > 1 else ast.body
        if isinstance(func, Symbol) and func.inherit is not None:
            if isinstance(first_stmt, CallStmt):
                first_sname = first_stmt.name
                if first_sname in ["super", "preventDefault"]:
                    spar = self.visit(first_stmt, param)
                    for joiner in self.func_list:
                        if joiner.name == func.inherit:
                            fpar = joiner.param
                    if len(spar) != len(fpar):
                        raise TypeMismatchInStatement(first_stmt)
                    for i in range(len(spar)):
                        arg = self.visit(spar[i], param)
                        if type(arg) is not type(fpar[i].typ):
                            raise TypeMismatchInExpression(spar[i])                       
                else:
                    raise InvalidStatementInFunction(func.name)
            else:
                raise InvalidStatementInFunction(func.name)
        elif func.inherit is None and isinstance(func, Symbol) and len(ast.body)!=0:
            if isinstance(ast.body[0], CallStmt):
                first_sname = ast.body[0].name
                if first_sname in ["super", "preventDefault"]:
                    raise InvalidStatementInFunction(func.name)
        for joiner in ast.body:
            self.visit(joiner, param)

        return param

    def visitIfStmt(self, ast, param):
        condition = self.visit(ast.cond, param)
        if not isinstance(condition, BooleanType):
            raise TypeMismatchInExpression(ast)   
        t_env = self.visit(ast.tstmt, [[Symbol(None, None, IfStmt())]] + param)
        f_env = self.visit(ast.fstmt, [[Symbol(None, None, IfStmt())]] + param) if ast.fstmt else param
        return param


    def visitForStmt(self, ast, param):
        self.visit(ast.init, param)
        typ = self.visit(ast.cond, param)
        if not isinstance(typ, BooleanType):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.upd, param)

        env = [[Symbol(None, None, Loop())]] + param
        self.visit(ast.stmt, env)
        return param

    def visitWhileStmt(self, ast, param):
        cond = self.visit(ast.cond, param)
        if not isinstance(cond, BooleanType):
            raise TypeMismatchInStatement(ast)
        env = [[Symbol(None, None, Loop())]] + param
        self.visit(ast.stmt, env)
        return param

    def visitIntegerType(self, ast, param):
        return IntegerType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBooleanType(self, ast, param):
        return BooleanType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        return ArrayType(ast.dimensions, ast.typ)

    def visitAutoType(self, ast, param):
        return AutoType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitId(self, ast, param):
        for pare in param:
            for joiner in pare:
                if isinstance(joiner, Symbol):
                    continue
                if (isinstance(joiner, (VarDecl, ParamDecl)) and joiner.name == ast.name):
                    return joiner.typ
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, param):
        for pare in param:
            for joiner in pare:
                if isinstance(joiner, Symbol) or joiner.name != ast.name or not isinstance(joiner.typ, ArrayType):
                    continue
                if len(joiner.typ.dimensions) == len(ast.cell):
                    for cell in ast.cell:
                        if not isinstance(self.visit(cell, param), IntegerType):
                            raise TypeMismatchInExpression(ast)
                    return joiner.typ.typ
                else:
                    raise TypeMismatchInStatement(ast)
        raise Undeclared(Variable(), ast.name)

    def visitIntegerLit(self, ast, param):
        return IntegerType()

    def visitFloatLit(self, ast, param):
        return FloatType()

    def visitStringLit(self, ast, param):
        return StringType()

    def visitBooleanLit(self, ast, param):
        return BooleanType()

    def visitArrayLit(self, ast, param):
        def get_num(lst):
            return reduce(lambda x, y: x * y, lst, 1)

        def check_type(lst):
            typ = self.visit(lst[0], param)
            for i in lst:
                _typ = self.visit(i, param)
                if type(typ) is not type(_typ):
                    return False, None
            return True, typ
            
        def get_dimensions(pare):
            if type(pare) is ArrayLit and isinstance(pare.explist, list):
                return [len(pare.explist)] + get_dimensions(pare.explist[0])
            else:
                return []
                
        def flatten(lst, param=[]):
            if type(lst) is ArrayLit and isinstance(lst.explist, list):
                for i in lst.explist:
                    param = flatten(i, param)
            elif type(lst) is ArrayLit and type(lst.explist) is not list:
                param = param + [lst.explist]
            else:
                param = param + [lst]
            return param
            
        dim = get_dimensions(ast)
        ct, typ_check = check_type(flatten(ast))
        sametype = (get_num(dim) == len(flatten(ast))) and ct
            
        if not sametype:
            raise IllegalArrayLiteral(ast)
                
        return ArrayType(dim, self.visit(typ_check, param))


    def visitBinExpr(self, ast, param):
        e1t = self.visit(ast.left, param)
        e2t = self.visit(ast.right, param)

        if ast.op in ['+', '-', '*', '/']:
            if not isinstance(e1t, (FloatType, IntegerType)) or not isinstance(e2t, (FloatType, IntegerType)):
                raise TypeMismatchInExpression(ast)
            if isinstance(e1t, FloatType) or isinstance(e2t, FloatType):
                return FloatType()
            return IntegerType()

        if ast.op == '%':
            if not isinstance(e1t, IntegerType) or not isinstance(e2t, IntegerType):
                raise TypeMismatchInExpression(ast)
            return IntegerType()

        if ast.op == '::':
            if isinstance(e1t, StringType) and isinstance(e2t, StringType):
                return StringType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ['&&', '||']:
            if not isinstance(e1t, BooleanType) or not isinstance(e2t, BooleanType):
                raise TypeMismatchInExpression(ast)
            return BooleanType()

        if ast.op in ['==', '!=']:
            if type(e1t) is not type(e2t):
                raise TypeMismatchInExpression(ast)
            if isinstance(e1t, (IntegerType, BooleanType)):
                return BooleanType()
            raise TypeMismatchInExpression(ast)

        if ast.op in ['<', '>', '<=', '>=']:
            if not isinstance(e1t, (FloatType, IntegerType)) or not isinstance(e2t, (FloatType, IntegerType)):
                raise TypeMismatchInExpression(ast)
            return BooleanType()

        raise TypeMismatchInExpression(ast)

    def visitVarDecl(self, ast, param):
        if len(param) > 1:
            for para in param[0]:
                if self.inherit_decl:
                    if isinstance(para, ParamDecl):
                        if para.name == ast.name:
                            raise Invalid(Parameter(), ast.name)
                if isinstance(para, VarDecl) or isinstance(para, ParamDecl):
                    if para.name == ast.name:
                        raise Redeclared(Variable(), ast.name)

            if isinstance(ast.typ, AutoType) and ast.init is None:
                raise Invalid(Variable(), ast.name)

            if ast.init is not None:
                expr_type = self.visit(ast.init, param)
                if not isinstance(expr_type, type(ast.typ)):
                    if isinstance(ast.typ, AutoType) and not isinstance(expr_type, VoidType):
                        ast.typ = self.visit(expr_type, param)
                    elif isinstance(expr_type, VoidType):
                        raise TypeMismatchInVarDecl(ast)
                    elif isinstance(ast.typ, FloatType) and isinstance(expr_type, IntegerType):
                        expr_type = FloatType()
                    elif not isinstance(ast.init, FuncCall):
                        raise TypeMismatchInVarDecl(ast)
                if isinstance(expr_type, ArrayType) and isinstance(ast.typ, ArrayType):
                    if len(expr_type.dimensions) == len(ast.typ.dimensions):
                        for i in range(0, len(expr_type.dimensions)):
                            if expr_type.dimensions[i] != ast.typ.dimensions[i]:
                                raise TypeMismatchInVarDecl(ast)
                    if isinstance(ast.typ.typ, AutoType):
                        ast.typ.typ = self.visit(expr_type.typ, param)
                    if not isinstance(expr_type.typ, type(ast.typ.typ)):
                        raise TypeMismatchInVarDecl(ast)
                if isinstance(expr_type, AutoType) and isinstance(ast.init, FuncCall) and isinstance(ast.typ, AutoType):
                    raise Invalid(Function(), ast.init.name)
                elif isinstance(expr_type, AutoType) and isinstance(ast.init, FuncCall):
                    for pare in param:
                        for joiner in pare:
                            if joiner.name == ast.init.name and isinstance(joiner, FuncCall):
                                joiner.return_type = self.visit(ast.typ, param)
                                break

            param[0].append(ast)
        return param

    def visitParamDecl(self, ast, param):
        # Check for parameter redeclaration
        for par in param[0]:
            if isinstance(par, ParamDecl) and par.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
        
        # Add the parameter to the Symbol table
        param[0].append(ast)
        
        return param
    
    def visitFuncDecl(self, ast, param):
        # Check for function redeclaration
        for joiner in param[0]:
            if isinstance(joiner, FuncDecl) and joiner.name == ast.name and type(joiner.return_type) == type(ast.return_type):
                raise Redeclared(Function(), ast.name)

        # Check for special function redeclaration
        for special_func in self.special_func:
            if special_func.name == ast.name:
                raise Redeclared(Function(), ast.name)

        # Add the function to the Symbol table
        param[0].append(ast)

        if len(param) > 1:
            # Handle inheritance
            declared = None
            if ast.inherit is not None:
                for pare in param:
                    for joiner in pare:
                        if isinstance(joiner, FuncDecl) and joiner.name == ast.inherit:
                            declared = joiner
                            break
                    if declared is not None:
                        break

                if declared is None:
                    raise Undeclared(Function(), ast.inherit)
                self.inherit_decl = True
            else:
                self.inherit_decl = False

            # Create a new environment for the function
            env = [[Symbol(ast.name, ast.return_type, Function(), ast.inherit, ast.params)]] + param

            # Add the function to the list of functions
            self.func_list.append(Symbol(ast.name, ast.return_type, Function(), ast.inherit, ast.params))

            # Visit the function parameters
            for paramdecl in ast.params:
                env = self.visit(paramdecl, env)

            # Visit the function body
            env = self.visit(ast.body, env)

        return param

    def visitProgram(self, ast, param):
        # Visit each declaration in the program and update the param
        param = self.visitDeclarations(ast.decls, [[]])

        # Add the special function to the param
        param += [self.special_func]

        # Visit each declaration again and update the body
        body = [[]] + param
        body = self.visitDeclarations(ast.decls, body)

        # Find the main function declaration and check if it exists
        main_decl = next((decl for decl in ast.decls if decl.name == "main" and isinstance(decl.return_type, VoidType)), None)
        if not main_decl:
            raise NoEntryPoint()
        return [] 







 