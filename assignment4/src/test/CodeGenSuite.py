import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    def test1(self):
        """ """
        input = """
            b: integer = 5;
            main: function void () {
                i: integer = 5;
                while(i > 0) {
                    printInteger(i);
                    i = i - 1;
                }
            }
        """
        expect = "54321"
        self.assertTrue(TestCodeGen.test(input, expect, 501))
    
    def test2(self):
        """ """
        input = """
            main: function void() {
                b: integer = 5;
                printInteger(b);
            }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    def test3(self):
        """ """
        input = """
            b: integer = 5;
            main: function void () {
                i: integer = 5;
                for(i = 0, i < 5, i + 1) {
                    printInteger(i);
                }
            }
        """
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input, expect, 503))
    
    # def test4(self):
    #     """ """
    #     input = """
    #         b: integer = 4;
    #         main: function void () {
    #             i: integer = 5;
    #             if (i == 5) {
    #                 printInteger(i);
    #             }
    #         }
        
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))
    
    # def test5(self):
    #     """ """
    #     input = """
    #         b: integer = 5;
    #         main: function void () {
    #             i: integer = 5;
    #             do {
    #                 printInteger(i);
    #                 i = i - 1;
    #             }
    #             while(i > 0);
    #         }
    #     """
    #     expect = "54321"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))
    
    # def test6(self):
    #     """ """
    #     input = """
    #         main: function void () {
    #             a: integer = 5;
    #             a = 4;
    #             printInteger(a);
    #         }
    #     """
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))
    
    # def test7(self):
    #     """ """
    #     input = """
    #         main: function void() {
    #             a: array [3] of integer = {1,2,3};
    #             printInteger(a[0]);
    #         }
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))
    
    def test8(self):
        """ """
        input = """
            main: function void() {
                b: float = 3.5;
                printFloat(b);
            }
        """
        expect = "3.5"
        self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    # def test9(self):
    #     """ """
    #     input = """
    #         main: function void() {
    #             a: integer = 2;
    #             b: integer = 3;
    #             if (a < b) {
    #                 printString("a is less than b");
    #             }
    #             if (a > b) {
    #                 printString("a is rather than b");
    #             }
    #             if (a == b) {
    #                 printString("a is equal b");
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))
    
    # def test10(self):
    #     """ """
    #     input = """
    #         foo: function integer(a: integer) inherit goo {
    #             super(3);
    #             return 2;
    #         }
    #         goo: function integer(inherit abc: integer) {
    #             return b;
    #         }
    #         main: function void() {}
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    # def test11(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    # def test12(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))
    
    # def test13(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))
    
    # def test14(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))
    
    # def test15(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))
    
    # def test16(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    # def test17(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    # def test18(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))
    
    # def test19(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))
    
    # def test20(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))
    
    # def test21(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))
    
    # def test22(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))
    
    # def test23(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))
    
    # def test24(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    # def test25(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))
    
    # def test26(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))
    
    # def test27(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))
    
    # def test28(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))
    
    # def test29(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))
    
    # def test30(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))
    
    # def test31(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    # def test32(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))
    
    # def test33(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))
    
    # def test34(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))
    
    # def test35(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))
    
    # def test36(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))
    
    # def test37(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))
    
    # def test38(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))
    
    # def test39(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 539))
    
    # def test40(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 540))
    
    # def test41(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 541))
    
    # def test42(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 542))
    
    # def test43(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 543))
    
    # def test44(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 544))
    
    # def test45(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 545))
    
    # def test46(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 546))
    
    # def test47(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 547))
    
    # def test48(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 548))
    
    # def test49(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 549))
    
    # def test50(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 550))
    
    # def test51(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 551))
    
    # def test52(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 552))
    
    # def test53(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 553))
    
    # def test54(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 554))
    
    # def test55(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 555))
    
    # def test56(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 556))
    
    # def test57(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 557))
    
    # def test58(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 558))
    
    # def test59(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 559))
    
    # def test60(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 560))
    
    # def test61(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    # def test62(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 562))
    
    # def test63(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 563))
    
    # def test64(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 564))
    
    # def test65(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    # def test66(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 566))
    
    # def test67(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 567))
    
    # def test68(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 568))
    
    # def test69(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 569))
    
    # def test70(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 570))
    
    # def test71(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 571))
    
    # def test72(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    # def test73(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 573))
    
    # def test74(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 574))
    
    # def test75(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 575))
    
    # def test76(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 576))
    
    # def test77(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 577))
    
    # def test78(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 578))
    
    # def test79(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 579))
    
    # def test80(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 580))
    
    # def test81(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 581))
    
    # def test82(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 582))
    
    # def test83(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 583))
    
    # def test84(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 584))
    
    # def test85(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 585))
    
    # def test86(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 586))
    
    # def test87(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 587))
    
    # def test88(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 588))
    
    # def test89(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 589))
    
    # def test90(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 590))
    
    # def test91(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 591))
    
    # def test92(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 592))
    
    # def test93(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 593))
    
    # def test94(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 594))
    
    # def test95(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 595))
    
    # def test96(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 596))
    
    # def test97(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 597))
    
    # def test98(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 598))
    
    # def test99(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 599))
    
    # def test100(self):
    #     """ """
    #     input = """
        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestCodeGen.test(input, expect, 600))
    