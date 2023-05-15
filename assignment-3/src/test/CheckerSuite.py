import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
 
    def test0(self):
        input = """ y : integer ; """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test1(self):
        input = """x : integer = 1 ; main: function void(){} """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test2(self):
        input = """x : integer = y ; y : integer = 2 ;"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test3(self):
        input = """x : integer = 1 ; c: auto; main: function void(){} """
        expect = "Invalid Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test4(self):
        input = """x: integer = 1; main: function void(){
            x = 2;
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test5(self):
        input = """ main: function void(){
            a: integer = 1.5;
            b: float = a+2;
            } """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(1.5))"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test6(self):
        input = """ main: function void(){
            a: float = 1;
            b: float = a+2;
            c: integer = 2.3;
            } """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.3))"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test7(self):
        input = """ main: function void(){
            a: float = 1;
            b: float = a+2;
            c: auto = 2.3;
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test8(self):
        input = """ main: function void(){
            a: string = "abc";
            b: boolean = 1>2;
            c: auto = b;
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test9(self):
        input = """ 
        foo : function auto ( a : integer , b : integer ) {}
        main: function void(){
            a: string = "abc";
            b: boolean = 1>2;
            c: auto = b;
            d: float = c ;
            } """
        expect = "Type mismatch in Variable Declaration: VarDecl(d, FloatType, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 409))
    
    def test10(self):
        input = """ 
        foo : function auto ( a : integer , b : integer ) {}
        main: function void(){
            e: integer = foo(1,2);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 410))
    
    def test11(self):
        input = """ 
        foo : function auto ( a : integer , b : integer ) {}
        main: function void(){
            e: integer = foo(1,2.3) +1.3;
            } """
        expect = "Type mismatch in expression: BinExpr(+, FuncCall(foo, [IntegerLit(1), FloatLit(2.3)]), FloatLit(1.3))"
        self.assertTrue(TestChecker.test(input, expect, 411))
    
    def test12(self):
        input = """ 
        foo : function auto ( a : integer , b : integer ) {}
        main: function void(){
            foo(1,2.3);
            } """
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), FloatLit(2.3))"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test13(self):
        input = """ 
        foo : function auto ( a : integer , b : integer ) {}
        main: function void(){
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test17(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
        }
        foo2: function auto (inherit a : integer , b : integer ) inherit foo {
            super(a,b);
            a: integer = 1;
        }
        main: function void(){
            } """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test18(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
        }
        foo: function auto ( a : integer , b : integer ) inherit foo {
            super(a,b);
            a: integer = 1;
        }
        main: function void(){

            } """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test19(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
        }
        a: integer = 1;
        main: function void(){

            z: integer = 1;
            foo(a,z);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test20(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3,1] of integer;
        }
        a: integer = 1;
        main: function void(){} """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 419))
    def test21(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,2,3};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 420))
    def test22(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,2.9,3};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(2.9), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 421))
    def test23(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
        }
        x, y, z: integer = 1,2,3;
        main: function void(){
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test24(self):
        input = """
        foo : function void ( a : integer , b : integer ) {
            x: integer = 1;
        }
        main: function void(){
            a,b: integer;
            foo(1,2,3);
            } """
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), IntegerLit(2), IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test25(self):
        input = """
        foo : function void () {
        }
        main: function void(){
            a,b: integer;
            foo();
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test26(self):
        input = """
        foo : function void () {
            a,b: integer;
        }
        main: function void(){
            a,b: integer;
            a= foo1();
            } """
        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test27(self):
        input = """
        foo : function void () {
            a,b: integer;
        }
        main: function void(){
            a: integer = foo();

            } """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 426))
    
    
    def test29(self):
        input = """
        foo : function void () {
            a,b: integer;
        }
        main: function void(){
            break;
            } """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 428))
    def test30(self):
        input = """
        foo : function void () {
            a,b: integer;
        }
        main: function void(){
            continue;
            } """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test31(self):
        input = """
        foo : function void (c: integer) {
            a,b: integer;
        }
        main: function void(){
            foo(1.2);
            } """
        expect = "Type mismatch in statement: CallStmt(foo, FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test32(self):
        input = """
        foo : function void (c: integer) {
            a,b: integer;
        }
        main: function void(){
            foo3();
            } """
        expect = "Undeclared Function: foo3"
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test33(self):
        input = """
        foo : function integer (c: integer) {
            return c+2;
        }
        main: function void(){
            foo(1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test34(self):
        input = """
        main: function void(){
            i:integer;
            for(i=1.2, i<10, i+1){ i=1+1;
            break;
            continue;
            }
            } """
        expect = "Type mismatch in expression: AssignStmt(Id(i), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test35(self):
        input = """
        main: function void(){
             a,i:integer;
              if (a==0) i=i+1;
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 434))


    def test175(self):
        input = """
        foo : function auto ( a : integer , b : integer) {
            
            x: integer = 1;
        }
        foo2: function auto (inherit a : integer , b : integer ) inherit foo {
            super(a,1,z);
            a: integer = 1;
        }
        main: function void(){

            } """
        expect = "Type mismatch in statement: CallStmt(super, Id(a), IntegerLit(1), Id(z))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test36(self):
        input = """
        foo : function auto ( a : integer , b : integer, z: integer ) {
            
            x: integer = 1;
        }
        foo2: function auto (inherit a : integer , b : integer) inherit foo {
            super(1,2.8,3);
            a: integer = 1;
        }
        main: function void(){

            } """
        expect = "Type mismatch in expression: FloatLit(2.8)"
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test37(self):
        input = """
        foo : function auto ( a : integer , b : integer, z: integer ) {
            x: integer = 1;
        }
        foo2: function auto ( a : integer , b : integer)  {
            preventDefault();
        }
        main: function void(){
            } """
        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test38(self):
        input = """
        main: function void(){
            printInteger(1.4);
            } """
        expect = "Type mismatch in statement: CallStmt(printInteger, FloatLit(1.4))"
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test39(self):
        input = """
        main: function void(){
            a : array [5] of integer = {1,2,3,7,5};
            z: integer;
            z = a[3];
        
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test40(self):
        input = """
        main: function void(){
            a : array [5] of integer = {1,2,3,7,5};
            z: integer;
            z = a[3.2];
        
            } """
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(3.2)])"
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test41(self):
        input = """
        main: function void(){
            a : array [5] of integer = {1,2,3,7,5};
            z: integer;
            z = a[3];
            z = a[z];
        
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test42(self):
        input = """
        main: function void(){
            a : array [5] of integer = {1,2,3,7,5};
            z: integer;
            z = a[3];
            z = a[z];
            z = a[z];
        
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test43(self):
        input = """
        main: function void(){
            a : array [5] of integer = {1,2,3,7,5};
            z: integer;
            z = a[3];
            z = a[z];
            z = a[z];
            z = a[z];
        
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test44(self):
        input = """
        main: function void(){
            a : array [5] of integer = {1,2,3,7,5};
            z: integer;
            z = a[3];
            z = a[z];
            z = a[z];
            z = a[z];
            z = a[z];
        
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test45(self):
        input = """
        main: function void(){
            a : array [5] of integer = {1,2,3,7,5};
            z: integer;
            z = a[3];
            z = a[z];
            z = a[z];
            z = a[z];
            z = a[z];
            z = a[z];
        
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test46(self):
        input = """
        main: function void(){
            a : array [5] of integer = {1,2,3,7,5};
            z: integer;
            z = a[3];
            z = a[z];
            z = a[z];
            z = a[z];
            z = a[z];
            z = a[z];
            z = a[z];
        
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test47(self):
            input = """
            foo : function auto ( a : integer , b : integer ) {
                x: integer = 1;
                z: array [3] of integer = {1,3,4,3};
            }
            a: integer = 1;
            main: function void(){
                foo(a,1);
                } """
            expect = "Type mismatch in Variable Declaration: VarDecl(z, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4), IntegerLit(3)]))"
            self.assertTrue(TestChecker.test(input, expect, 447))
    def test48(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test49(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test50(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test51(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test52(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test53(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test54(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test55(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test56(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test57(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test58(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test59(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test60(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test61(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test62(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test63(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test64(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test65(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test66(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 466))
    def test67(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 467))
    def test68(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 468))
    def test69(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 469))
    def test70(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test71(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test72(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 472))
    def test73(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test74(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test75(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test76(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test77(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test78(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test79(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test80(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 480))
    def test81(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 481))
    def test82(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 482))
    def test83(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 483))
    def test84(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 484))
    def test85(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 485))
    def test86(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 486))
    def test87(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 487))
    def test88(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test89(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 489))
    def test90(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test91(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test92(self): 
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test93(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test94(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test95(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test96(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 496))
    def test97(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test98(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test99(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 499))
    def test100(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 500))
    def test10033(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 5004))
    def test1040(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            x: integer = 1;
            z: array [3] of integer = {1,3,4};
        }
        a: integer = 1;
        main: function void(){
            foo(a,1);
            } """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 5040))