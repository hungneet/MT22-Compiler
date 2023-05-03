import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # WS
    def test_WS(self):
        """white space
        """
        self.assertTrue(TestLexer.test("     \n \n \r   \t", "<EOF>", 100))
    
   # Comment
    def test_comment_cpp(self):
        """"Test comment c++"""
        self.assertTrue(TestLexer.test("//this this a comment", "<EOF>", 102))

    def test_comment_c(self):
        """test comment c
        """
        self.assertTrue(TestLexer.test(
            "/* A C-style comment */", "<EOF>", 103))

    def test_general_cmt(self):
        """combine cmt
        """
        self.assertTrue(TestLexer.test(
            "//hello\nabc/* A C-style comment */", "abc,<EOF>", 104))
    # ID lit

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_uppercase_id(self):
        """UPPERCASE
        """
        self.assertTrue(TestLexer.test(
            "ABCD EFGH IJJJ", "ABCD,EFGH,IJJJ,<EOF>", 105))

    def test_id_rand(self):
        self.assertTrue(TestLexer.test(
            "_halh2 H1230_33", "_halh2,H1230_33,<EOF>", 110))

    def test_id_error(self):
        self.assertTrue(TestLexer.test("#", "Error Token #", 126))

   # Keyword
    def test_keyword(self):
        self.assertTrue(TestLexer.test("auto", "auto,<EOF>", 106))

    # Opp
    def test_opp(self):
        """operators"""
        self.assertTrue(TestLexer.test("+-*/%", "+,-,*,/,%,<EOF>", 107))

    def test_opp2(self):
        self.assertTrue(TestLexer.test(
            "&&||==!=::", "&&,||,==,!=,::,<EOF>", 108))
    # Sep

    def test_seperators(self):
        self.assertTrue(TestLexer.test(
            "([.,;:}{])", "(,[,.,,,;,:,},{,],),<EOF>", 109))
    # Interger LIT

    def test_int(self):
        self.assertTrue(TestLexer.test(
            "713 3178300", "713,3178300,<EOF>", 111))

    def test_int1(self):
        """uderscore int
        """
        self.assertTrue(TestLexer.test("1_233_4", "12334,<EOF>", 112))

    def test_int2(self):
        self.assertTrue(TestLexer.test("1__3", "13,<EOF>", 113))

    def test_int3(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 114))

    def test_int4(self):
        self.assertTrue(TestLexer.test("0123", "0,123,<EOF>", 128))

    # Float lit
    def test_float(self):
        self.assertTrue(TestLexer.test("1.234", "1.234,<EOF>", 115))

    def test_float2(self):
        self.assertTrue(TestLexer.test("1234.23", "1234.23,<EOF>", 116))

    def test_float3(self):
        self.assertTrue(TestLexer.test("1_23.3_2", "123.3,_2,<EOF>", 117))

    def test_float4(self):
        self.assertTrue(TestLexer.test("0.23e2", "0.23e2,<EOF>", 118))

    def test_float5(self):
        self.assertTrue(TestLexer.test("7E-10", "7E-10,<EOF>", 119))
    # boolean lit

    def test_bool(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 120))
    # String lit

    def test_string(self):
        """vanila string no error
        """
        self.assertTrue(TestLexer.test("\"this is a string\"",
                        "this is a string,<EOF>", 125))

    def test_string2(self):
        self.assertTrue(TestLexer.test(
            "\"\\\\t his is a string \\t \\' \"", "\\\\t his is a string \\t \\' ,<EOF>", 131))

    def test_string3(self):
        self.assertTrue(TestLexer.test("\"#*(@*)$)!\"",
                        "#*(@*)$)!,<EOF>", 132))

    def test_string4(self):
        self.assertTrue(TestLexer.test(
            "\"he asked: \\\"who ask\\\"\"", "he asked: \\\"who ask\\\",<EOF>", 136))

    def test_string5(self):
        self.assertTrue(TestLexer.test(
            "\"\\f \\r \\b \\t \\n \\\" \\' \"", "\\f \\r \\b \\t \\n \\\" \\' ,<EOF>", 137))

    def test_unclose(self):
        """unclose string
        """
        self.assertTrue(TestLexer.test(
            "\"    unclose", "Unclosed String:     unclose", 129))

    def test_unclose2(self):
        self.assertTrue(TestLexer.test("\"quai su bing chi ling",
                        "Unclosed String: quai su bing chi ling", 138))
    def test_unclose3(self):
        self.assertTrue(TestLexer.test("\"\\t cai nay \\\" van loi\\\"","Unclosed String: \\t cai nay \\\" van loi\\\"",139))
    def test_illescape(self):
        """illegal escape
        """
        self.assertTrue(TestLexer.test(
            "\"\\e\"", "Illegal Escape In String: \e", 130))

    def test_illEs2(self):
        self.assertTrue(TestLexer.test("\"\\\\\"", "\\\\,<EOF>", 134))

    def test_illEs3(self):
        self.assertTrue(TestLexer.test("\" hello quai su bing chilling \\jha \"",
                        "Illegal Escape In String:  hello quai su bing chilling \j", 135))

    # Array lit
    def test_arr(self):
        self.assertTrue(TestLexer.test("\\t", "Error Token \\", 121))

    def test_arr2(self):
        self.assertTrue(TestLexer.test(
            "{7E-3,hu21_dd,true,2131}", "{,7E-3,,,hu21_dd,,,true,,,2131,},<EOF>", 122))

    def test_arr3(self):
        self.assertTrue(TestLexer.test(
            "{}", "{,},<EOF>", 123))

    def test_arr6(self):
        self.assertTrue(TestLexer.test("{   }}", "{,},},<EOF>", 124))

    def test_arr4(self):
        self.assertTrue(TestLexer.test("{ 2, 3 }", "{,2,,,3,},<EOF>", 127))

    def test_arr5(self):
        self.assertTrue(TestLexer.test(
            "{\"hello\"}", "{,hello,},<EOF>", 133))
        
    def test_case1(self):
        self.assertTrue(TestLexer.test(
        '123 a = 45_3 + 2.0 / b /* A comment */ ;',
        '123,a,=,453,+,2.0,/,b,;,<EOF>',
        140))

    def test_41(self):
        self.assertTrue(TestLexer.test(
        "1 22 333 4444 0 55_6_78", "1,22,333,4444,0,55678,<EOF>", 141))

    def test_42(self):
        self.assertTrue(TestLexer.test(
            "tRue false TruE FalSE", "tRue,false,TruE,FalSE,<EOF>", 142))

    def test_43(self):
        self.assertTrue(TestLexer.test(
            "abc123 = 456", "abc123,=,456,<EOF>", 143))

    def test_44(self):
        self.assertTrue(TestLexer.test(
            "if (a == 5)", "if,(,a,==,5,),<EOF>", 144))

    def test_45(self):
        self.assertTrue(TestLexer.test(
            "1 + 2 - 3 * 4 / 5", "1,+,2,-,3,*,4,/,5,<EOF>", 145))

    def test_46(self):
        self.assertTrue(TestLexer.test(
            "x = 123; // this is a comment", "x,=,123,;,<EOF>", 146))

    def test_47(self):
        self.assertTrue(TestLexer.test(
            "/* C-style comment */", "<EOF>", 147))

    def test_48(self):
        self.assertTrue(TestLexer.test(
            "// C++-style comment", "<EOF>", 148))

    def test_49(self):
        self.assertTrue(TestLexer.test(
            "// A C++ style comment\n123", "123,<EOF>", 149))

    def test_50(self):
        self.assertTrue(TestLexer.test(
            "2 < 3 && 4 > 5 || 6 == 7", "2,<,3,&&,4,>,5,||,6,==,7,<EOF>", 150))

    def test_51(self):
        self.assertTrue(TestLexer.test(
            "123 == 456 != 789 <= 321 >= 654", "123,==,456,!=,789,<=,321,>=,654,<EOF>", 151))

    def test_52(self):
        self.assertTrue(TestLexer.test(
            "if (a == 5) { return true; } else { return false; }", "if,(,a,==,5,),{,return,true,;,},else,{,return,false,;,},<EOF>", 152))

    def test_53(self):
        self.assertTrue(TestLexer.test(
            "abcdefg1234567_8_9_0", "abcdefg1234567_8_9_0,<EOF>", 153))

    def test_54(self):
        self.assertTrue(TestLexer.test(
            "int[] arr = new int[10];", "int,[,],arr,=,new,int,[,10,],;,<EOF>", 154))

    def test_55(self):
        self.assertTrue(TestLexer.test(
            "a = -b", "a,=,-,b,<EOF>", 155))

    def test_56(self):
        self.assertTrue(TestLexer.test(
            "double a = 3.1415; float b = 0.0; float c = -1.5;", "double,a,=,3.1415,;,float,b,=,0.0,;,float,c,=,-,1.5,;,<EOF>", 156))
    def test_56(self):
        self.assertTrue(TestLexer.test("123_456", "123456,<EOF>", 156))

    def test_57(self):
        self.assertTrue(TestLexer.test("1_23_", "123,_,<EOF>", 157))

    def test_58(self):
        self.assertTrue(TestLexer.test("\"Hello world!\"", "Hello world!,<EOF>", 158))

    def test_59(self):
        self.assertTrue(TestLexer.test("a==3", "a,==,3,<EOF>", 159))

    def test_60(self):
        self.assertTrue(TestLexer.test("10==0xA", "10,==,0,xA,<EOF>", 160))

    def test_61(self):
        self.assertTrue(TestLexer.test("20==0o24", "20,==,0,o24,<EOF>", 161))

    def test_62(self):
        self.assertTrue(TestLexer.test("30==0b11110", "30,==,0,b11110,<EOF>", 162))

    def test_63(self):
        self.assertTrue(TestLexer.test("1/2", "1,/,2,<EOF>", 163))

    def test_64(self):
        self.assertTrue(TestLexer.test("1", "1,<EOF>", 164))

    def test_65(self):
        self.assertTrue(TestLexer.test("5-2", "5,-,2,<EOF>", 165))

    def test_66(self):
        self.assertTrue(TestLexer.test("a//b", "a,<EOF>", 166))

    def test_67(self):
        self.assertTrue(TestLexer.test("1.5e-2", "1.5e-2,<EOF>", 167))

    def test_68(self):
        self.assertTrue(TestLexer.test("1.23e4", "1.23e4,<EOF>", 168))

    def test_69(self):
        self.assertTrue(TestLexer.test("0.0001", "0.0001,<EOF>", 169))

    def test_70(self):
        self.assertTrue(TestLexer.test("0e0", "0e0,<EOF>", 170))

    def test_71(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 171))

    def test_72(self):
        self.assertTrue(TestLexer.test("x = a + 2;\ny = b * 3;\nreturn x + y;", "x,=,a,+,2,;,y,=,b,*,3,;,return,x,+,y,;,<EOF>", 172))

    def test_73(self):
        self.assertTrue(TestLexer.test("// This is a comment\na = 1;", "a,=,1,;,<EOF>", 173))

    def test_74(self):
        self.assertTrue(TestLexer.test("/* This is a comment */\na = 2;", "a,=,2,;,<EOF>", 174))

    def test_75(self):
        self.assertTrue(TestLexer.test("/* This is a\n   multiline\n   comment */\nwhile i < 10 do i = i + 1;", "while,i,<,10,do,i,=,i,+,1,;,<EOF>", 175))

    def test_76(self):
        self.assertTrue(TestLexer.test("// This is a C++ style comment\nb = 2;", "b,=,2,;,<EOF>", 176))
    def test_77(self):
        self.assertTrue(TestLexer.test("7.8e-4", "7.8e-4,<EOF>", 177))

    def test_78(self):
        self.assertTrue(TestLexer.test("\"0.001\"\"", "0.001,Error Token \"", 178))

    def test_79(self):
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 179))

    def test_80(self):
        self.assertTrue(TestLexer.test("hello\tworld", "hello,world,<EOF>", 180))

    def test_81(self):
        self.assertTrue(TestLexer.test("hello\nworld", "hello,world,<EOF>", 181))

    def test_82(self):
        self.assertTrue(TestLexer.test("hello\rworld", "hello,world,<EOF>", 182))

    def test_83(self):
        self.assertTrue(TestLexer.test("hello\\world", "hello,Error Token \\", 183))

    def test_84(self):
        self.assertTrue(TestLexer.test("hello\"world\"", "hello,world,<EOF>", 184))

    def test_85(self):
        self.assertTrue(TestLexer.test("// This is a comment", "<EOF>", 185))

    def test_86(self):
        self.assertTrue(TestLexer.test("/* This is a comment */", "<EOF>", 186))

    def test_87(self):
        self.assertTrue(TestLexer.test("/* This is a comment */ a = 5;", "a,=,5,;,<EOF>", 187))

    def test_88(self):
        self.assertTrue(TestLexer.test("a = 5; // This is a comment", "a,=,5,;,<EOF>", 188))

    def test_89(self):
        self.assertTrue(TestLexer.test("a = \"Hello, world!\";", "a,=,Hello, world!,;,<EOF>", 189))

    def test_90(self):
        self.assertTrue(TestLexer.test("a = 3.14;", "a,=,3.14,;,<EOF>", 190))

    def test_91(self):
        self.assertTrue(TestLexer.test("a = true;", "a,=,true,;,<EOF>", 191))

    def test_92(self):
        self.assertTrue(TestLexer.test("a = false;", "a,=,false,;,<EOF>", 192))

    def test_93(self):
        self.assertTrue(TestLexer.test("if (a == 5) then b = true;", "if,(,a,==,5,),then,b,=,true,;,<EOF>", 193))

    def test_94(self):
        self.assertTrue(TestLexer.test("if (a == 5) then b = true; else b = false;", "if,(,a,==,5,),then,b,=,true,;,else,b,=,false,;,<EOF>", 194))

    def test_95(self):
        self.assertTrue(TestLexer.test("while (i < 10) do i = i + 1;", "while,(,i,<,10,),do,i,=,i,+,1,;,<EOF>", 195))

    def test_96(self):
        self.assertTrue(TestLexer.test("for (i = 0; i < 10; i = i + 1) do println(i);", "for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),do,println,(,i,),;,<EOF>", 196))

    def test_97(self):
        self.assertTrue(TestLexer.test("println(\"Hello, \\\ world!\");", "println,(,Hello, \\\ world!,),;,<EOF>",197))
    def test_98(self):
        self.assertTrue(TestLexer.test("//yo\nhello","hello,<EOF>",198))
    def test_99(self):
        self.assertTrue(TestLexer.test("//yo\rhello","hello,<EOF>",199))
        