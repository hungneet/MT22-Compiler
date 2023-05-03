import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_simplevardecl(self):
        input = """x, y, z: boolean ;"""
        expect = """Program([
	VarDecl(x, BooleanType)
	VarDecl(y, BooleanType)
	VarDecl(z, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
        
    def test_simplevardecl2(self):
        input = """x: array [2,3] of integer ;"""
        expect = """Program([
	VarDecl(x, ArrayType([2, 3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_simplevardecl3(self):
        input = """x, y, z: auto ;"""
        expect = """Program([
	VarDecl(x, AutoType)
	VarDecl(y, AutoType)
	VarDecl(z, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test_fullvardecl1(self):
        input = """x: integer = 1 ;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_ful_vardecl_2(self):
        input = """x: integer = false;"""
        expect = """Program([
	VarDecl(x, IntegerType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
    def test_f_vardecl_3(self):
        input = """x: float = 2_1.31e-2;"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(21.31e-2))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test_fvardecl_4(self):
        input = """x: void = a[1,2];"""
        expect = """Program([
	VarDecl(x, VoidType, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_fvardecl_5(self):
        input = """x: void = a;"""
        expect = """Program([
	VarDecl(x, VoidType, Id(a))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    def test_fvardecl_5_2(self):
        input = """x: string = "Hung pro";"""
        expect = """Program([
	VarDecl(x, StringType, StringLit(Hung pro))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test_fvardecl_6(self):
        input = """x: auto = foo(a);"""
        expect = """Program([
	VarDecl(x, AutoType, FuncCall(foo, [Id(a)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_fvardecl_7(self):
        input = """x: auto = foo(a,2,2.1,"c");"""
        expect = """Program([
	VarDecl(x, AutoType, FuncCall(foo, [Id(a), IntegerLit(2), FloatLit(2.1), StringLit(c)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_fvardecl_8(self):
        input = """x: auto = {a,2,2.1,"c"};"""
        expect = """Program([
	VarDecl(x, AutoType, ArrayLit([Id(a), IntegerLit(2), FloatLit(2.1), StringLit(c)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
    
    def test_fvardecl_9(self):
        input = """x: auto = {};"""
        expect = """Program([
	VarDecl(x, AutoType, ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
    def test_fvardecl_10(self):
        input = """x: auto = foo();"""
        expect = """Program([
	VarDecl(x, AutoType, FuncCall(foo, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    def test_fullvardecl_11(self):
        input = """x: integer = -1 ;"""
        expect = """Program([
	VarDecl(x, IntegerType, UnExpr(-, IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
    #Test Expr
    def test_fullvardecl_12(self):
        input = """x: integer = !true ;"""
        expect = """Program([
	VarDecl(x, IntegerType, UnExpr(!, BooleanLit(True)))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    def test_fullvardecl_13(self):
        input = """x: integer = 2 - 3 ;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(-, IntegerLit(2), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
    def test_fullvardecl_14(self):
        input = """x: integer = 2 && 3 ;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(&&, IntegerLit(2), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
    def test_fullvardecl_15(self):
        input = """x: integer = 2 >= 3 ;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(>=, IntegerLit(2), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    def test_fullvardecl_16(self):
        input = """x: integer = 2 :: 3 ;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(::, IntegerLit(2), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    def test_fullvardecl_17(self):
        input = """x: integer = foo(2 +3,-4) ;"""
        expect = """Program([
	VarDecl(x, IntegerType, FuncCall(foo, [BinExpr(+, IntegerLit(2), IntegerLit(3)), UnExpr(-, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
    def test_fullvardecl_18(self):
        input = """x: integer = a[2 +3,-4] ;"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(2), IntegerLit(3)), UnExpr(-, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
    def test_fullvardecl_19(self):
        input = """x: integer = 2+4*5  ;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(4), IntegerLit(5))))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    def test_fullvardecl_20(self):
        input = """x: integer = 2+4*5 && !a ==4 ;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(==, BinExpr(&&, BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(4), IntegerLit(5))), UnExpr(!, Id(a))), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    def test_fullvardecl_21(self):
        input = """x: integer = 2+4*5 && !a ==4 ;
        x: integer = a[2 +3,-4]; x: integer = foo(2 +3,-4);
        """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(==, BinExpr(&&, BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(4), IntegerLit(5))), UnExpr(!, Id(a))), IntegerLit(4)))
	VarDecl(x, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(2), IntegerLit(3)), UnExpr(-, IntegerLit(4))]))
	VarDecl(x, IntegerType, FuncCall(foo, [BinExpr(+, IntegerLit(2), IntegerLit(3)), UnExpr(-, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    def test_fullvardecl_22(self):
        input = """x,y,lae_t: integer = 2+4*5,1 &&3, !a ==4 ;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(4), IntegerLit(5))))
	VarDecl(y, IntegerType, BinExpr(&&, IntegerLit(1), IntegerLit(3)))
	VarDecl(lae_t, IntegerType, BinExpr(==, UnExpr(!, Id(a)), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
    
    #STMT TEST
    
    def test_stmt(self):
        input = """main: function void () {
            a = 1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
    
    def test_stmt2(self):
        input = """main: function void () {
            a[3] = 1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(3)]), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
    def test_stmt3_1(self):
        input = """main: function void () {
            a[3] = 1-3 + 4 * foo(3);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(3)]), BinExpr(+, BinExpr(-, IntegerLit(1), IntegerLit(3)), BinExpr(*, IntegerLit(4), FuncCall(foo, [IntegerLit(3)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
    def test_stmt4(self):
        input = """main: function void () {
            a[3] = 1-3 + 4 * foo(3); hung= "gamer";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(3)]), BinExpr(+, BinExpr(-, IntegerLit(1), IntegerLit(3)), BinExpr(*, IntegerLit(4), FuncCall(foo, [IntegerLit(3)])))), AssignStmt(Id(hung), StringLit(gamer))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
    
    def test_stmt5(self):
        input = """main: function void () {
            if (a==0) i=i+1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    def test_stmt6(self):
        input = """main: function void () {
            if (a==0) {i=i+1;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
    def test_stmt7(self):
        input = """main: function void () {
            if (a==0) {i=i+1;
            a: integer = 1;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), VarDecl(a, IntegerType, IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
    def test_stmt8(self):
        input = """main: function void () {
            if (a==0) i=i+1; else i=i-1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_stmt9(self):
        input = """main: function void () {
            for(i=0, i<10, i+1){ i=1+1;}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(i, IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, IntegerLit(1), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
    def test_stmt10(self):
        input = """main: function void () {
            for(i=0, i<10, i+1) i=1+1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(i), BinExpr(+, IntegerLit(1), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
    def test_stmt11(self):
        input = """
        foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

        main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
    
    def test_stmt12(self):
        input = """
        main: function void () {
           continue;
           break;
           return 1+1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ContinueStmt(), BreakStmt(), ReturnStmt(BinExpr(+, IntegerLit(1), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
    def test_var3(self):
        input = """ z: string = "bool" ; z: integer = 123_3_3;
        main: function void() {}"""
        expect = """Program([
	VarDecl(z, StringType, StringLit(bool))
	VarDecl(z, IntegerType, IntegerLit(12333))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
    def test_func_with_params(self):
        input = """
        foo: function integer (a: integer, b: float) {
            c: integer;
            c = a + b;
            return c;
        }
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(c, IntegerType), AssignStmt(Id(c), BinExpr(+, Id(a), Id(b))), ReturnStmt(Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_if_else_stmt(self):
        input = """
        main: function void () {
            if (a > b)  {
                print("a is greater than b");
            }
            else {
                print("b is greater than a");
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([CallStmt(print, StringLit(a is greater than b))]), BlockStmt([CallStmt(print, StringLit(b is greater than a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    #function test
    
    def test_func1(self):
        """function
        """
        input = """
        x: integer = 65;
        fact: function integer (n: integer){
            if (n==0) return 1;
            else return n * fact(n-1);
        }
        main: function void() {}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 208))
    def test_func2(self):
        """function
        """
        input = """
        x: integer = 65;
        fact: function integer (n: integer){
            if (n==0) return 1;
            else return n * fact(n-1);
        }
        inc: function void (out n : integer, delta: integer){
            n = n +delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x,delta);
            printInteger(x);
            }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 209))
    def test_func3(self):
        input = """main: function void() {
            r, s: integer;
            r = 2.0;
            a, b: array [5] of integer;
            s = r * r * myPI;
            a[0] = s;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 210))
    def test_rand(self):
        input = """x,f_2: integer = 3,2; """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(3))
	VarDecl(f_2, IntegerType, IntegerLit(2))
])"""
        self.assertTrue(TestAST.test(input, expect, 212)) 
    #expression
    def test_exp1(self):
        input = """main: function void() {
            x,y: float = 1.334, 1_342.2e+4;
            n: float = x+y*y;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.334)), VarDecl(y, FloatType, FloatLit(1342.2e+4)), VarDecl(n, FloatType, BinExpr(+, Id(x), BinExpr(*, Id(y), Id(y))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 213))
    def test_exp2(self):
        input = """main: function void() {
            x,y: float = 1.334, 1_342.2e+4;
            n: float = x+y*y-2/x +y%7;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.334)), VarDecl(y, FloatType, FloatLit(1342.2e+4)), VarDecl(n, FloatType, BinExpr(+, BinExpr(-, BinExpr(+, Id(x), BinExpr(*, Id(y), Id(y))), BinExpr(/, IntegerLit(2), Id(x))), BinExpr(%, Id(y), IntegerLit(7))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 214))
    def test_exp3(self):
        input = """main: function void() {
            y= zda[0];
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(y), ArrayCell(zda, [IntegerLit(0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 215))
    #statement
    def test_stmt(self):
        input = """main: function void() {
            x= epando(x) *5;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(*, FuncCall(epando, [Id(x)]), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 216))
    def test_stmt2(self):
        input = """main: function auto() {
            z= "hello" + "world";
            }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(Id(z), BinExpr(+, StringLit(hello), StringLit(world)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 217))
    def test_stmt3(self):
        input = """main: function void() {
            if(z==y) return sum(0);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(z), Id(y)), ReturnStmt(FuncCall(sum, [IntegerLit(0)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 218))
    def test_stmt4(self):
        input = """main: function auto() {
            z[1,3]= "hello" + "world";
            }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(ArrayCell(z, [IntegerLit(1), IntegerLit(3)]), BinExpr(+, StringLit(hello), StringLit(world)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 219))
    def test_stmt5(self):
        input = """main: function auto() {
            z[1,3]= y[z];
            }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(ArrayCell(z, [IntegerLit(1), IntegerLit(3)]), ArrayCell(y, [Id(z)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 220))
    def test_stmt6(self):
        input = """main: function auto() {
            z[1,3]= {1,3,3};
            }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([AssignStmt(ArrayCell(z, [IntegerLit(1), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 221))
    def test_stmt7(self):
        input = """main: function void() {
            for(i=0, i<10, i+1){ writeInt(i);}
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 222))
    def test_stmt8(self):
        input = """main: function void() {
            for(i=1+3, i<10, i+1){ writeInt(i);}
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(+, IntegerLit(1), IntegerLit(3))), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 223))
    def test_stmt8_2(self):
        input = """main: function void() {
            for(i=11+4, i<8 && i>6, i+2-0.5){ writeInt(i);}
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(+, IntegerLit(11), IntegerLit(4))), BinExpr(>, BinExpr(<, Id(i), BinExpr(&&, IntegerLit(8), Id(i))), IntegerLit(6)), BinExpr(-, BinExpr(+, Id(i), IntegerLit(2)), FloatLit(0.5)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 224))
    def test_stmt9_1(self):
        input = """main: function void() {
            while(hung3 == 1000){
                writeln("Hello mother fker");
                hung3= hung3 +100;
            }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(hung3), IntegerLit(1000)), BlockStmt([CallStmt(writeln, StringLit(Hello mother fker)), AssignStmt(Id(hung3), BinExpr(+, Id(hung3), IntegerLit(100)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 225))
    def test_stmt9(self):
        input = """main: function void() {
            while(funcz(5)!=3){
                writeln("Hello mother fker");
                hung3= hung3 +100;
            }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, FuncCall(funcz, [IntegerLit(5)]), IntegerLit(3)), BlockStmt([CallStmt(writeln, StringLit(Hello mother fker)), AssignStmt(Id(hung3), BinExpr(+, Id(hung3), IntegerLit(100)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 226))
    def test_stmt11(self):
        input = """main: function void() {
            while(funcz(5)!=3){
                writeln("Hello mother fker");
                hung3= hung3 +100;
                continue;break;
            }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, FuncCall(funcz, [IntegerLit(5)]), IntegerLit(3)), BlockStmt([CallStmt(writeln, StringLit(Hello mother fker)), AssignStmt(Id(hung3), BinExpr(+, Id(hung3), IntegerLit(100))), ContinueStmt(), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 228))
    def test_stmt12(self):
        input = """main: function void() {
            do { write("hello");}
            while (n<11);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(n), IntegerLit(11)), BlockStmt([CallStmt(write, StringLit(hello))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 229))
    def test_rand2(self):
        input = """main: function void() {
            x: array [2,3] of string = {1,2 ,3};
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([2, 3], StringType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 236))
    def test_rand3(self):
        input = """main: function void() {
            x: array [2,3] of string = {1___3.e3,"2" ,"3",33_3};
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([2, 3], StringType), ArrayLit([FloatLit(13.e3), StringLit(2), StringLit(3), IntegerLit(333)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 237))
    
    def test_rand6(self):
        input = """main: function void() {
            if (x==0) i=i+1; else i =i+1; 
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input,expect, 240))
    def test_rand9(self):
        input = """main: function void() {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 243))
    def test_rand10(self):
        input = """main: function void() {
            readInteger();
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 244))
    def test_rand11(self):
        input = """main: function void() {
            printInteger(1234);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(1234))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 245))
    def test_rand12(self):
        input = """main: function void() {
            readFloat();
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(readFloat, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 246))
    def test_rand63(self):
        input = """main: function integer() {
        a = 5;
        b = 7;
        return a + b;
    }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(5)), AssignStmt(Id(b), IntegerLit(7)), ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 262))
    def test_r1(self):
        input = """foo: function boolean(x: integer, y: array [2] of float) {
        for (i = 0, i < x,  i + 1) {
            y[i] = i * 2.0;
        }
        return true;
    }"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(x, IntegerType), Param(y, ArrayType([2], FloatType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(x)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(y, [Id(i)]), BinExpr(*, Id(i), FloatLit(2.0)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 263))
    def test_ran4(self):
        input = """bar: function void() {
            if (x > y) {
                print("x is greater than y");
            }
            else if (y > x) {
                print("y is greater than x");
            }
            else {
                print("x and y are equal");
            }
        }"""
        expect = """Program([
	FuncDecl(bar, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(x), Id(y)), BlockStmt([CallStmt(print, StringLit(x is greater than y))]), IfStmt(BinExpr(>, Id(y), Id(x)), BlockStmt([CallStmt(print, StringLit(y is greater than x))]), BlockStmt([CallStmt(print, StringLit(x and y are equal))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 264))
    def test_rad5(self):
        input = """baz: function float(x: float, y: float) {
            if (x > y) {
                return x;
            }
            else {
                return y;
            }
        }"""
        expect = """Program([
	FuncDecl(baz, FloatType, [Param(x, FloatType), Param(y, FloatType)], None, BlockStmt([IfStmt(BinExpr(>, Id(x), Id(y)), BlockStmt([ReturnStmt(Id(x))]), BlockStmt([ReturnStmt(Id(y))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 265))
    def test_rand266(self):
        input = """foo: function void() { 
        if (a>1) integzer=1;
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), AssignStmt(Id(integzer), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 266))
    def test_ra1nd(self):
        input = """foo: function integer() {
             x: integer = 1;
            y: integer = 2;
            return x + y;
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), VarDecl(y, IntegerType, IntegerLit(2)), ReturnStmt(BinExpr(+, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 269))

    def test_ran2(self):
        input = """foo: function void() {
            x: integer = 1;
            if (x == 1) {
                putInt(x);
            }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(1)), IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([CallStmt(putInt, Id(x))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 270))
    def test_ra3(self):
        input = """foo: function boolean() {
             x: boolean = true;
             y: boolean = false;
            return x && y || !x && !y;
        }"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [], None, BlockStmt([VarDecl(x, BooleanType, BooleanLit(True)), VarDecl(y, BooleanType, BooleanLit(False)), ReturnStmt(BinExpr(&&, BinExpr(||, BinExpr(&&, Id(x), Id(y)), UnExpr(!, Id(x))), UnExpr(!, Id(y))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 271))
    def test_ra4(self):
        input = """foo: function string() {
             x: string = "hello";
             y: string = "world";
            return x + " " + y;
        }"""
        expect = """Program([
	FuncDecl(foo, StringType, [], None, BlockStmt([VarDecl(x, StringType, StringLit(hello)), VarDecl(y, StringType, StringLit(world)), ReturnStmt(BinExpr(+, BinExpr(+, Id(x), StringLit( )), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 272))
    def test_ran5(self):
        input = """foo: function float() {
             x: float = 1.0;
             y: float = 2.0;
            return x / y;
        }"""
        expect = """Program([
	FuncDecl(foo, FloatType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.0)), VarDecl(y, FloatType, FloatLit(2.0)), ReturnStmt(BinExpr(/, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 273))
    def test_ran6(self):
        input = """foo: function boolean(x: boolean) {
            return !x;
        }"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(x, BooleanType)], None, BlockStmt([ReturnStmt(UnExpr(!, Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 274))
    def test_ran7(self):
        input = """foo: function integer(x: integer, y: integer) {
            if (x > y) {
                return x - y;
            }
            else {
                return y - x;
            }
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(x), Id(y)), BlockStmt([ReturnStmt(BinExpr(-, Id(x), Id(y)))]), BlockStmt([ReturnStmt(BinExpr(-, Id(y), Id(x)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 275))
    def test_ran9(self):
        input = """foo: function boolean(x: integer, y: integer) {
            return x == y;
        }"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(==, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 277))
    def test_ran10(self):
        input = """foo: function integer(x: integer) {
            return x * x;
        }

        bar: function integer(x: integer) {
            return foo(x) + foo(x + 1);
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(x)))]))
	FuncDecl(bar, IntegerType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(foo, [Id(x)]), FuncCall(foo, [BinExpr(+, Id(x), IntegerLit(1))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 278))
    def test_case282(self):
        input = """main: function void() {
            x= z::y;
            z= a[1] + a[2];}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(z), Id(y))), AssignStmt(Id(z), BinExpr(+, ArrayCell(a, [IntegerLit(1)]), ArrayCell(a, [IntegerLit(2)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 282))
    def test_case284(self):
        input = """main: function void() {
            x= z::y;
            hello(funtion());
            z: array[2] of integer = {};}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(z), Id(y))), CallStmt(hello, FuncCall(funtion, [])), VarDecl(z, ArrayType([2], IntegerType), ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 284))
    def test_295(self):
        input = """main: function void() {
            x: array [3] of float = a[1];
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], FloatType), ArrayCell(a, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 295))
    def test_vardecl(self):
        """var dec"""
        input = """
        x: integer = 65;
        main: function void() {}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 201))
    def test_vardecl2(self):
        """many var dec
        """
        input = """x: void; y: float = 6.42; z: auto; k: boolean = false;"""
        expect = """Program([
	VarDecl(x, VoidType)
	VarDecl(y, FloatType, FloatLit(6.42))
	VarDecl(z, AutoType)
	VarDecl(k, BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 202))
    def test_multiple_func_decl(self):
        input = """
        foo: function void () {}
        bar: function integer (a: integer, b: float) {
            return a + b;
        }
        baz: function string () {
            return "hello";
        }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([]))
	FuncDecl(bar, IntegerType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(baz, StringType, [], None, BlockStmt([ReturnStmt(StringLit(hello))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_for_stmt(self):
        input = """
        main: function void () {
            for (i = 0, i < 10, 2) {
                print(i);
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), IntegerLit(2), BlockStmt([CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_array_access(self):
        input = """
        main: function void () {
            arr[1 + 2] = 3;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(+, IntegerLit(1), IntegerLit(2))]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_func4(self):
        input = """foo: function void (a: integer, b: boolean) {
            if (a == 0) 
                return z;
            else
                b = true;
            foo(a-1, b);
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), ReturnStmt(Id(z)), AssignStmt(Id(b), BooleanLit(True))), CallStmt(foo, BinExpr(-, Id(a), IntegerLit(1)), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    def test_stmt13(self):
        input = """main: function void () {
            do {
                x = x + 1;
            } while( x < 10);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(x), IntegerLit(10)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    def test_stmt14(self):
        input = """main: function void () {
            for (i=0, i<10, i+1) {
                if (i % 2 == 0) {
                    continue;
                }
            print(i);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([ContinueStmt()])), CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    def test_stmt15(self):
        input = """main: function void () {
            for (i=0, i<10, i+1) {
                if (i == 5) {
                    break;
                }
                print(i);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(5)), BlockStmt([BreakStmt()])), CallStmt(print, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
    def test_expr6(self):
        input = """main: function void () {
            x = 1;
            y = 2;
            z = x > y;
            print(z);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), IntegerLit(1)), AssignStmt(Id(y), IntegerLit(2)), AssignStmt(Id(z), BinExpr(>, Id(x), Id(y))), CallStmt(print, Id(z))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
    def test_funcdecl4(self):
        input = """
        foo: function void (a: integer, b: float, c: string) {
            if (a == 0) {
                return;
            }
            else {
                print(b);
                foo(a-1, b, c);
            }
        }
        main: function void () {
            foo(10, 10.0, "hello");
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, FloatType), Param(c, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([ReturnStmt()]), BlockStmt([CallStmt(print, Id(b)), CallStmt(foo, BinExpr(-, Id(a), IntegerLit(1)), Id(b), Id(c))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(10), FloatLit(10.0), StringLit(hello))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_expr5(self):
        input = """
        main: function void () {
            x = 1 + 2 * 3 - 4 / 5;
            z = -x;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(-, BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(2), IntegerLit(3))), BinExpr(/, IntegerLit(4), IntegerLit(5)))), AssignStmt(Id(z), UnExpr(-, Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_stmt13(self):
        input = """
        main: function void () {
            do {
                print("hello");
                break;
                continue;
            } while (false);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([CallStmt(print, StringLit(hello)), BreakStmt(), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_expr6(self):
        input = """
        main: function void () {
            a = 5;
            b = 2;
            c = a % b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(5)), AssignStmt(Id(b), IntegerLit(2)), AssignStmt(Id(c), BinExpr(%, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
    def test_func10(self):
        input = """
        foo: function integer (a: integer, b: integer) {
            if (a > b)
                return a;
            else
                return b;
        }
        main: function void () {
            printIntLn(foo(4, 7));
        }
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), ReturnStmt(Id(a)), ReturnStmt(Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printIntLn, FuncCall(foo, [IntegerLit(4), IntegerLit(7)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_func11(self):
        input = """
        factorial: function integer (n: integer) {
            if (n == 0)
                return 1;
            else
                return n * factorial(n - 1);
        }
        main: function void () {
            printIntLn(factorial(5));
        }
        """
        expect = """Program([
	FuncDecl(factorial, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printIntLn, FuncCall(factorial, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_func12(self):
        input = """
        gcd: function integer (a: integer, b: integer) {
            while (a != b) {if (a > b)
                    a = a - b;
                else
                    b = b - a;
           }
                return a; 
        }
        main: function void () {
            printIntLn(gcd(12, 18));
        }
        """
        expect = """Program([
	FuncDecl(gcd, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(!=, Id(a), Id(b)), BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), AssignStmt(Id(a), BinExpr(-, Id(a), Id(b))), AssignStmt(Id(b), BinExpr(-, Id(b), Id(a))))])), ReturnStmt(Id(a))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printIntLn, FuncCall(gcd, [IntegerLit(12), IntegerLit(18)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_func13(self):
        input = """
        power: function integer (base: integer, exponent: integer) {
            if (exponent == 0) 
                return 1;
            else
                return base * power(base, exponent - 1);
        }
        main: function void () {
            printIntLn(power(2, 10));
        }
        """
        expect = """Program([
	FuncDecl(power, IntegerType, [Param(base, IntegerType), Param(exponent, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(exponent), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(base), FuncCall(power, [Id(base), BinExpr(-, Id(exponent), IntegerLit(1))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printIntLn, FuncCall(power, [IntegerLit(2), IntegerLit(10)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    def test_array1(self):
        input = """
        main: function void () {
            arr[3] = {1, 2, 3};
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_array2(self):
        input = """
        main: function void () {
         arr[2,3] = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(2), IntegerLit(3)]), ArrayLit([ArrayLit([FloatLit(1.0), FloatLit(2.0), FloatLit(3.0)]), ArrayLit([FloatLit(4.0), FloatLit(5.0), FloatLit(6.0)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_array3(self):
        input = """
        main: function void () {
          
            arr[0] = 1;
            arr[1] = 2;
            arr[2] = 3;
        }
    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0)]), IntegerLit(1)), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), IntegerLit(2)), AssignStmt(ArrayCell(arr, [IntegerLit(2)]), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))


    
        