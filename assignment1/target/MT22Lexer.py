# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01c2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\6\2{\n\2\r\2\16\2|\3\2\3\2\3\3\3\3\3")
        buf.write("\3\7\3\u0084\n\3\f\3\16\3\u0087\13\3\3\3\6\3\u008a\n\3")
        buf.write("\r\3\16\3\u008b\3\3\5\3\u008f\n\3\3\4\3\4\3\4\7\4\u0094")
        buf.write("\n\4\f\4\16\4\u0097\13\4\3\4\7\4\u009a\n\4\f\4\16\4\u009d")
        buf.write("\13\4\5\4\u009f\n\4\3\4\3\4\7\4\u00a3\n\4\f\4\16\4\u00a6")
        buf.write("\13\4\5\4\u00a8\n\4\3\4\3\4\5\4\u00ac\n\4\3\4\6\4\u00af")
        buf.write("\n\4\r\4\16\4\u00b0\5\4\u00b3\n\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00c0\n\5\3\6\3\6\3\6\3\6")
        buf.write("\7\6\u00c6\n\6\f\6\16\6\u00c9\13\6\3\6\3\6\3\6\3\6\7\6")
        buf.write("\u00cf\n\6\f\6\16\6\u00d2\13\6\3\6\3\6\5\6\u00d6\n\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\7\7\u00de\n\7\f\7\16\7\u00e1\13")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3*")
        buf.write("\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\67")
        buf.write("\5\67\u019d\n\67\3\67\7\67\u01a0\n\67\f\67\16\67\u01a3")
        buf.write("\13\67\38\38\38\39\39\39\39\79\u01ac\n9\f9\169\u01af\13")
        buf.write("9\3:\3:\3:\3;\3;\3;\3;\7;\u01b8\n;\f;\16;\u01bb\13;\3")
        buf.write(";\3;\3;\3<\3<\3<\3\u00d0\2=\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q\2s:u\2w;\3\2\f\5\2\13\f\17\17\"")
        buf.write("\"\3\2\62;\3\2\63;\4\2GGgg\4\2--//\4\2\f\f\17\17\6\2\f")
        buf.write("\f\17\17$$^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\2\u01d6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2s\3\2\2\2\2w\3\2\2\2\3z\3\2\2\2\5\u008e\3\2")
        buf.write("\2\2\7\u009e\3\2\2\2\t\u00bf\3\2\2\2\13\u00d5\3\2\2\2")
        buf.write("\r\u00d9\3\2\2\2\17\u00e5\3\2\2\2\21\u00e7\3\2\2\2\23")
        buf.write("\u00e9\3\2\2\2\25\u00eb\3\2\2\2\27\u00ed\3\2\2\2\31\u00ef")
        buf.write("\3\2\2\2\33\u00f1\3\2\2\2\35\u00f4\3\2\2\2\37\u00f7\3")
        buf.write("\2\2\2!\u00fa\3\2\2\2#\u00fd\3\2\2\2%\u00ff\3\2\2\2\'")
        buf.write("\u0102\3\2\2\2)\u0104\3\2\2\2+\u0107\3\2\2\2-\u010a\3")
        buf.write("\2\2\2/\u010c\3\2\2\2\61\u010e\3\2\2\2\63\u0110\3\2\2")
        buf.write("\2\65\u0112\3\2\2\2\67\u0114\3\2\2\29\u0116\3\2\2\2;\u0118")
        buf.write("\3\2\2\2=\u011a\3\2\2\2?\u011c\3\2\2\2A\u011e\3\2\2\2")
        buf.write("C\u0120\3\2\2\2E\u0125\3\2\2\2G\u012b\3\2\2\2I\u0133\3")
        buf.write("\2\2\2K\u0136\3\2\2\2M\u013b\3\2\2\2O\u0141\3\2\2\2Q\u0147")
        buf.write("\3\2\2\2S\u014b\3\2\2\2U\u0154\3\2\2\2W\u0157\3\2\2\2")
        buf.write("Y\u015f\3\2\2\2[\u0166\3\2\2\2]\u016d\3\2\2\2_\u0172\3")
        buf.write("\2\2\2a\u0178\3\2\2\2c\u017d\3\2\2\2e\u0181\3\2\2\2g\u018a")
        buf.write("\3\2\2\2i\u018d\3\2\2\2k\u0195\3\2\2\2m\u019c\3\2\2\2")
        buf.write("o\u01a4\3\2\2\2q\u01a7\3\2\2\2s\u01b0\3\2\2\2u\u01b3\3")
        buf.write("\2\2\2w\u01bf\3\2\2\2y{\t\2\2\2zy\3\2\2\2{|\3\2\2\2|z")
        buf.write("\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177\b\2\2\2\177\4\3\2\2")
        buf.write("\2\u0080\u008f\t\3\2\2\u0081\u0089\t\4\2\2\u0082\u0084")
        buf.write("\7a\2\2\u0083\u0082\3\2\2\2\u0084\u0087\3\2\2\2\u0085")
        buf.write("\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0088\3\2\2\2")
        buf.write("\u0087\u0085\3\2\2\2\u0088\u008a\t\3\2\2\u0089\u0085\3")
        buf.write("\2\2\2\u008a\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f\b\3\3\2\u008e")
        buf.write("\u0080\3\2\2\2\u008e\u0081\3\2\2\2\u008f\6\3\2\2\2\u0090")
        buf.write("\u009f\7\62\2\2\u0091\u009b\t\4\2\2\u0092\u0094\7a\2\2")
        buf.write("\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3")
        buf.write("\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0098\u009a\t\3\2\2\u0099\u0095\3\2\2\2\u009a")
        buf.write("\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u0090\3")
        buf.write("\2\2\2\u009e\u0091\3\2\2\2\u009f\u00a7\3\2\2\2\u00a0\u00a4")
        buf.write("\7\60\2\2\u00a1\u00a3\t\3\2\2\u00a2\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a0\3")
        buf.write("\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00b2\3\2\2\2\u00a9\u00ab")
        buf.write("\t\5\2\2\u00aa\u00ac\t\6\2\2\u00ab\u00aa\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00af\t\3\2\2")
        buf.write("\u00ae\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3")
        buf.write("\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00a9")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b5\b\4\4\2\u00b5\b\3\2\2\2\u00b6\u00b7\7v\2\2\u00b7")
        buf.write("\u00b8\7t\2\2\u00b8\u00b9\7w\2\2\u00b9\u00c0\7g\2\2\u00ba")
        buf.write("\u00bb\7h\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7n\2\2\u00bd")
        buf.write("\u00be\7u\2\2\u00be\u00c0\7g\2\2\u00bf\u00b6\3\2\2\2\u00bf")
        buf.write("\u00ba\3\2\2\2\u00c0\n\3\2\2\2\u00c1\u00c2\7\61\2\2\u00c2")
        buf.write("\u00c3\7\61\2\2\u00c3\u00c7\3\2\2\2\u00c4\u00c6\n\7\2")
        buf.write("\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00d6\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00ca\u00cb\7\61\2\2\u00cb\u00cc\7,\2\2")
        buf.write("\u00cc\u00d0\3\2\2\2\u00cd\u00cf\13\2\2\2\u00ce\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d3\u00d4\7,\2\2\u00d4\u00d6\7\61\2\2\u00d5\u00c1\3")
        buf.write("\2\2\2\u00d5\u00ca\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8")
        buf.write("\b\6\2\2\u00d8\f\3\2\2\2\u00d9\u00df\7$\2\2\u00da\u00de")
        buf.write("\n\b\2\2\u00db\u00dc\7^\2\2\u00dc\u00de\t\t\2\2\u00dd")
        buf.write("\u00da\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e1\3\2\2\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e2\3")
        buf.write("\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\7$\2\2\u00e3\u00e4")
        buf.write("\b\7\5\2\u00e4\16\3\2\2\2\u00e5\u00e6\7-\2\2\u00e6\20")
        buf.write("\3\2\2\2\u00e7\u00e8\7/\2\2\u00e8\22\3\2\2\2\u00e9\u00ea")
        buf.write("\7,\2\2\u00ea\24\3\2\2\2\u00eb\u00ec\7\61\2\2\u00ec\26")
        buf.write("\3\2\2\2\u00ed\u00ee\7\'\2\2\u00ee\30\3\2\2\2\u00ef\u00f0")
        buf.write("\7#\2\2\u00f0\32\3\2\2\2\u00f1\u00f2\7(\2\2\u00f2\u00f3")
        buf.write("\7(\2\2\u00f3\34\3\2\2\2\u00f4\u00f5\7~\2\2\u00f5\u00f6")
        buf.write("\7~\2\2\u00f6\36\3\2\2\2\u00f7\u00f8\7?\2\2\u00f8\u00f9")
        buf.write("\7?\2\2\u00f9 \3\2\2\2\u00fa\u00fb\7#\2\2\u00fb\u00fc")
        buf.write("\7?\2\2\u00fc\"\3\2\2\2\u00fd\u00fe\7>\2\2\u00fe$\3\2")
        buf.write("\2\2\u00ff\u0100\7>\2\2\u0100\u0101\7?\2\2\u0101&\3\2")
        buf.write("\2\2\u0102\u0103\7@\2\2\u0103(\3\2\2\2\u0104\u0105\7@")
        buf.write("\2\2\u0105\u0106\7?\2\2\u0106*\3\2\2\2\u0107\u0108\7<")
        buf.write("\2\2\u0108\u0109\7<\2\2\u0109,\3\2\2\2\u010a\u010b\7*")
        buf.write("\2\2\u010b.\3\2\2\2\u010c\u010d\7+\2\2\u010d\60\3\2\2")
        buf.write("\2\u010e\u010f\7]\2\2\u010f\62\3\2\2\2\u0110\u0111\7_")
        buf.write("\2\2\u0111\64\3\2\2\2\u0112\u0113\7\60\2\2\u0113\66\3")
        buf.write("\2\2\2\u0114\u0115\7.\2\2\u01158\3\2\2\2\u0116\u0117\7")
        buf.write("=\2\2\u0117:\3\2\2\2\u0118\u0119\7<\2\2\u0119<\3\2\2\2")
        buf.write("\u011a\u011b\7}\2\2\u011b>\3\2\2\2\u011c\u011d\7\177\2")
        buf.write("\2\u011d@\3\2\2\2\u011e\u011f\7?\2\2\u011fB\3\2\2\2\u0120")
        buf.write("\u0121\7c\2\2\u0121\u0122\7w\2\2\u0122\u0123\7v\2\2\u0123")
        buf.write("\u0124\7q\2\2\u0124D\3\2\2\2\u0125\u0126\7d\2\2\u0126")
        buf.write("\u0127\7t\2\2\u0127\u0128\7g\2\2\u0128\u0129\7c\2\2\u0129")
        buf.write("\u012a\7m\2\2\u012aF\3\2\2\2\u012b\u012c\7d\2\2\u012c")
        buf.write("\u012d\7q\2\2\u012d\u012e\7q\2\2\u012e\u012f\7n\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130\u0131\7c\2\2\u0131\u0132\7p\2\2\u0132")
        buf.write("H\3\2\2\2\u0133\u0134\7f\2\2\u0134\u0135\7q\2\2\u0135")
        buf.write("J\3\2\2\2\u0136\u0137\7g\2\2\u0137\u0138\7n\2\2\u0138")
        buf.write("\u0139\7u\2\2\u0139\u013a\7g\2\2\u013aL\3\2\2\2\u013b")
        buf.write("\u013c\7h\2\2\u013c\u013d\7c\2\2\u013d\u013e\7n\2\2\u013e")
        buf.write("\u013f\7u\2\2\u013f\u0140\7g\2\2\u0140N\3\2\2\2\u0141")
        buf.write("\u0142\7h\2\2\u0142\u0143\7n\2\2\u0143\u0144\7q\2\2\u0144")
        buf.write("\u0145\7c\2\2\u0145\u0146\7v\2\2\u0146P\3\2\2\2\u0147")
        buf.write("\u0148\7h\2\2\u0148\u0149\7q\2\2\u0149\u014a\7t\2\2\u014a")
        buf.write("R\3\2\2\2\u014b\u014c\7h\2\2\u014c\u014d\7w\2\2\u014d")
        buf.write("\u014e\7p\2\2\u014e\u014f\7e\2\2\u014f\u0150\7v\2\2\u0150")
        buf.write("\u0151\7k\2\2\u0151\u0152\7q\2\2\u0152\u0153\7p\2\2\u0153")
        buf.write("T\3\2\2\2\u0154\u0155\7k\2\2\u0155\u0156\7h\2\2\u0156")
        buf.write("V\3\2\2\2\u0157\u0158\7k\2\2\u0158\u0159\7p\2\2\u0159")
        buf.write("\u015a\7v\2\2\u015a\u015b\7g\2\2\u015b\u015c\7i\2\2\u015c")
        buf.write("\u015d\7g\2\2\u015d\u015e\7t\2\2\u015eX\3\2\2\2\u015f")
        buf.write("\u0160\7t\2\2\u0160\u0161\7g\2\2\u0161\u0162\7v\2\2\u0162")
        buf.write("\u0163\7w\2\2\u0163\u0164\7t\2\2\u0164\u0165\7p\2\2\u0165")
        buf.write("Z\3\2\2\2\u0166\u0167\7u\2\2\u0167\u0168\7v\2\2\u0168")
        buf.write("\u0169\7t\2\2\u0169\u016a\7k\2\2\u016a\u016b\7p\2\2\u016b")
        buf.write("\u016c\7i\2\2\u016c\\\3\2\2\2\u016d\u016e\7v\2\2\u016e")
        buf.write("\u016f\7t\2\2\u016f\u0170\7w\2\2\u0170\u0171\7g\2\2\u0171")
        buf.write("^\3\2\2\2\u0172\u0173\7y\2\2\u0173\u0174\7j\2\2\u0174")
        buf.write("\u0175\7k\2\2\u0175\u0176\7n\2\2\u0176\u0177\7g\2\2\u0177")
        buf.write("`\3\2\2\2\u0178\u0179\7x\2\2\u0179\u017a\7q\2\2\u017a")
        buf.write("\u017b\7k\2\2\u017b\u017c\7f\2\2\u017cb\3\2\2\2\u017d")
        buf.write("\u017e\7q\2\2\u017e\u017f\7w\2\2\u017f\u0180\7v\2\2\u0180")
        buf.write("d\3\2\2\2\u0181\u0182\7e\2\2\u0182\u0183\7q\2\2\u0183")
        buf.write("\u0184\7p\2\2\u0184\u0185\7v\2\2\u0185\u0186\7k\2\2\u0186")
        buf.write("\u0187\7p\2\2\u0187\u0188\7w\2\2\u0188\u0189\7g\2\2\u0189")
        buf.write("f\3\2\2\2\u018a\u018b\7q\2\2\u018b\u018c\7h\2\2\u018c")
        buf.write("h\3\2\2\2\u018d\u018e\7k\2\2\u018e\u018f\7p\2\2\u018f")
        buf.write("\u0190\7j\2\2\u0190\u0191\7g\2\2\u0191\u0192\7t\2\2\u0192")
        buf.write("\u0193\7k\2\2\u0193\u0194\7v\2\2\u0194j\3\2\2\2\u0195")
        buf.write("\u0196\7c\2\2\u0196\u0197\7t\2\2\u0197\u0198\7t\2\2\u0198")
        buf.write("\u0199\7c\2\2\u0199\u019a\7{\2\2\u019al\3\2\2\2\u019b")
        buf.write("\u019d\t\n\2\2\u019c\u019b\3\2\2\2\u019d\u01a1\3\2\2\2")
        buf.write("\u019e\u01a0\t\13\2\2\u019f\u019e\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("n\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\13\2\2\2\u01a5")
        buf.write("\u01a6\b8\6\2\u01a6p\3\2\2\2\u01a7\u01ad\7$\2\2\u01a8")
        buf.write("\u01a9\7^\2\2\u01a9\u01ac\t\t\2\2\u01aa\u01ac\n\b\2\2")
        buf.write("\u01ab\u01a8\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3")
        buf.write("\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aer")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\5q9\2\u01b1\u01b2")
        buf.write("\b:\7\2\u01b2t\3\2\2\2\u01b3\u01b9\7$\2\2\u01b4\u01b5")
        buf.write("\7^\2\2\u01b5\u01b8\t\t\2\2\u01b6\u01b8\n\b\2\2\u01b7")
        buf.write("\u01b4\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2")
        buf.write("\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc\3")
        buf.write("\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd\7^\2\2\u01bd\u01be")
        buf.write("\n\t\2\2\u01bev\3\2\2\2\u01bf\u01c0\5u;\2\u01c0\u01c1")
        buf.write("\b<\b\2\u01c1x\3\2\2\2\34\2|\u0085\u008b\u008e\u0095\u009b")
        buf.write("\u009e\u00a4\u00a7\u00ab\u00b0\u00b2\u00bf\u00c7\u00d0")
        buf.write("\u00d5\u00dd\u00df\u019c\u019f\u01a1\u01ab\u01ad\u01b7")
        buf.write("\u01b9\t\b\2\2\3\3\2\3\4\3\3\7\4\38\5\3:\6\3<\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    INTLIT = 2
    FLOATLIT = 3
    BOOLLIT = 4
    COMMENT = 5
    STRINGLIT = 6
    ADD = 7
    SUB = 8
    MUL = 9
    DIV = 10
    MOD = 11
    NOT = 12
    AND = 13
    OR = 14
    EQ = 15
    NE = 16
    LT = 17
    LE = 18
    GT = 19
    GE = 20
    SCOPE = 21
    LPAREN = 22
    RPAREN = 23
    LBRACK = 24
    RBRACK = 25
    DOT = 26
    COMMA = 27
    SEMI = 28
    COLON = 29
    LBRACE = 30
    RBRACE = 31
    EQUAL = 32
    AUTO_K = 33
    BREAK_K = 34
    BOOLEAN_K = 35
    DO_K = 36
    ELSE_K = 37
    FALSE_K = 38
    FLOAT_K = 39
    FOR_K = 40
    FUNCTION_K = 41
    IF_K = 42
    INT_K = 43
    RETURN_K = 44
    STRING_K = 45
    TRUE_K = 46
    WHILE_K = 47
    VOID_K = 48
    OUT_K = 49
    CONTINUE_K = 50
    OF_K = 51
    INHERIT_K = 52
    ARRAY_K = 53
    ID = 54
    ERROR_CHAR = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'='", 
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "INTLIT", "FLOATLIT", "BOOLLIT", "COMMENT", "STRINGLIT", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", 
            "NE", "LT", "LE", "GT", "GE", "SCOPE", "LPAREN", "RPAREN", "LBRACK", 
            "RBRACK", "DOT", "COMMA", "SEMI", "COLON", "LBRACE", "RBRACE", 
            "EQUAL", "AUTO_K", "BREAK_K", "BOOLEAN_K", "DO_K", "ELSE_K", 
            "FALSE_K", "FLOAT_K", "FOR_K", "FUNCTION_K", "IF_K", "INT_K", 
            "RETURN_K", "STRING_K", "TRUE_K", "WHILE_K", "VOID_K", "OUT_K", 
            "CONTINUE_K", "OF_K", "INHERIT_K", "ARRAY_K", "ID", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "INTLIT", "FLOATLIT", "BOOLLIT", "COMMENT", "STRINGLIT", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQ", "NE", "LT", "LE", "GT", "GE", "SCOPE", "LPAREN", 
                  "RPAREN", "LBRACK", "RBRACK", "DOT", "COMMA", "SEMI", 
                  "COLON", "LBRACE", "RBRACE", "EQUAL", "AUTO_K", "BREAK_K", 
                  "BOOLEAN_K", "DO_K", "ELSE_K", "FALSE_K", "FLOAT_K", "FOR_K", 
                  "FUNCTION_K", "IF_K", "INT_K", "RETURN_K", "STRING_K", 
                  "TRUE_K", "WHILE_K", "VOID_K", "OUT_K", "CONTINUE_K", 
                  "OF_K", "INHERIT_K", "ARRAY_K", "ID", "ERROR_CHAR", "STRING_UNCLOSE", 
                  "UNCLOSE_STRING", "ESCAPE_ILLEGAL", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.INTLIT_action 
            actions[2] = self.FLOATLIT_action 
            actions[5] = self.STRINGLIT_action 
            actions[54] = self.ERROR_CHAR_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
             raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text[1:])
     


