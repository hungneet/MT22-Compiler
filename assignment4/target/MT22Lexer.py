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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01cf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.")
        buf.write("\3.\3/\3/\3/\7/\u012e\n/\f/\16/\u0131\13/\3/\3/\6/\u0135")
        buf.write("\n/\r/\16/\u0136\7/\u0139\n/\f/\16/\u013c\13/\3/\5/\u013f")
        buf.write("\n/\3\60\3\60\3\60\7\60\u0144\n\60\f\60\16\60\u0147\13")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\7\60\u014e\n\60\f\60\16\60")
        buf.write("\u0151\13\60\5\60\u0153\n\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\7\60\u015a\n\60\f\60\16\60\u015d\13\60\3\60\3\60\3\60")
        buf.write("\5\60\u0162\n\60\3\61\3\61\5\61\u0166\n\61\3\61\6\61\u0169")
        buf.write("\n\61\r\61\16\61\u016a\3\62\3\62\5\62\u016f\n\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\7\65\u017e\n\65\f\65\16\65\u0181\13\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\5\66\u018a\n\66\3\67\3\67\3")
        buf.write("\67\38\38\38\58\u0192\n8\39\39\79\u0196\n9\f9\169\u0199")
        buf.write("\139\3:\6:\u019c\n:\r:\16:\u019d\3:\3:\3;\3;\3;\3;\7;")
        buf.write("\u01a6\n;\f;\16;\u01a9\13;\3;\3;\3<\3<\3<\3<\7<\u01b1")
        buf.write("\n<\f<\16<\u01b4\13<\3<\3<\3<\3<\3<\3=\3=\3>\3>\7>\u01bf")
        buf.write("\n>\f>\16>\u01c2\13>\3>\5>\u01c5\n>\3?\3?\7?\u01c9\n?")
        buf.write("\f?\16?\u01cc\13?\3?\3?\3\u01b2\2@\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\2c\62e\63g\64i\65k\2m\2o\2q\66s\67u8w9y:{;}<\3\2")
        buf.write("\17\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f\f$$))^^\3\2")
        buf.write("^^\3\2$$\t\2))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\n\f\16\17\"\"\4\2\f\f\17\17\4\3\f\f\17\17\2\u01e1\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2\2\2\5\u0084\3")
        buf.write("\2\2\2\7\u008a\3\2\2\2\t\u0092\3\2\2\2\13\u0095\3\2\2")
        buf.write("\2\r\u009a\3\2\2\2\17\u00a0\3\2\2\2\21\u00a4\3\2\2\2\23")
        buf.write("\u00ad\3\2\2\2\25\u00b0\3\2\2\2\27\u00b8\3\2\2\2\31\u00bf")
        buf.write("\3\2\2\2\33\u00c6\3\2\2\2\35\u00cc\3\2\2\2\37\u00d1\3")
        buf.write("\2\2\2!\u00d5\3\2\2\2#\u00de\3\2\2\2%\u00e1\3\2\2\2\'")
        buf.write("\u00e9\3\2\2\2)\u00ef\3\2\2\2+\u00f1\3\2\2\2-\u00f3\3")
        buf.write("\2\2\2/\u00f5\3\2\2\2\61\u00f7\3\2\2\2\63\u00f9\3\2\2")
        buf.write("\2\65\u00fb\3\2\2\2\67\u00fe\3\2\2\29\u0101\3\2\2\2;\u0104")
        buf.write("\3\2\2\2=\u0107\3\2\2\2?\u0109\3\2\2\2A\u010b\3\2\2\2")
        buf.write("C\u010e\3\2\2\2E\u0111\3\2\2\2G\u0114\3\2\2\2I\u0116\3")
        buf.write("\2\2\2K\u0118\3\2\2\2M\u011a\3\2\2\2O\u011c\3\2\2\2Q\u011e")
        buf.write("\3\2\2\2S\u0120\3\2\2\2U\u0122\3\2\2\2W\u0124\3\2\2\2")
        buf.write("Y\u0126\3\2\2\2[\u0128\3\2\2\2]\u013e\3\2\2\2_\u0161\3")
        buf.write("\2\2\2a\u0163\3\2\2\2c\u016e\3\2\2\2e\u0170\3\2\2\2g\u0175")
        buf.write("\3\2\2\2i\u017b\3\2\2\2k\u0189\3\2\2\2m\u018b\3\2\2\2")
        buf.write("o\u0191\3\2\2\2q\u0193\3\2\2\2s\u019b\3\2\2\2u\u01a1\3")
        buf.write("\2\2\2w\u01ac\3\2\2\2y\u01ba\3\2\2\2{\u01bc\3\2\2\2}\u01c6")
        buf.write("\3\2\2\2\177\u0080\7c\2\2\u0080\u0081\7w\2\2\u0081\u0082")
        buf.write("\7v\2\2\u0082\u0083\7q\2\2\u0083\4\3\2\2\2\u0084\u0085")
        buf.write("\7d\2\2\u0085\u0086\7t\2\2\u0086\u0087\7g\2\2\u0087\u0088")
        buf.write("\7c\2\2\u0088\u0089\7m\2\2\u0089\6\3\2\2\2\u008a\u008b")
        buf.write("\7d\2\2\u008b\u008c\7q\2\2\u008c\u008d\7q\2\2\u008d\u008e")
        buf.write("\7n\2\2\u008e\u008f\7g\2\2\u008f\u0090\7c\2\2\u0090\u0091")
        buf.write("\7p\2\2\u0091\b\3\2\2\2\u0092\u0093\7f\2\2\u0093\u0094")
        buf.write("\7q\2\2\u0094\n\3\2\2\2\u0095\u0096\7g\2\2\u0096\u0097")
        buf.write("\7n\2\2\u0097\u0098\7u\2\2\u0098\u0099\7g\2\2\u0099\f")
        buf.write("\3\2\2\2\u009a\u009b\7h\2\2\u009b\u009c\7n\2\2\u009c\u009d")
        buf.write("\7q\2\2\u009d\u009e\7c\2\2\u009e\u009f\7v\2\2\u009f\16")
        buf.write("\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\20\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6")
        buf.write("\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\u00a9")
        buf.write("\7v\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac")
        buf.write("\7p\2\2\u00ac\22\3\2\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7h\2\2\u00af\24\3\2\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7i\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7t\2\2\u00b7\26")
        buf.write("\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\30\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\32\3\2\2\2\u00c6\u00c7")
        buf.write("\7y\2\2\u00c7\u00c8\7j\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7g\2\2\u00cb\34\3\2\2\2\u00cc\u00cd")
        buf.write("\7x\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7f\2\2\u00d0\36\3\2\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3")
        buf.write("\7w\2\2\u00d3\u00d4\7v\2\2\u00d4 \3\2\2\2\u00d5\u00d6")
        buf.write("\7e\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9")
        buf.write("\7v\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7w\2\2\u00dc\u00dd\7g\2\2\u00dd\"\3\2\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7h\2\2\u00e0$\3\2\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7j\2\2\u00e4\u00e5")
        buf.write("\7g\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8&\3\2\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee")
        buf.write("\7{\2\2\u00ee(\3\2\2\2\u00ef\u00f0\7-\2\2\u00f0*\3\2\2")
        buf.write("\2\u00f1\u00f2\7/\2\2\u00f2,\3\2\2\2\u00f3\u00f4\7,\2")
        buf.write("\2\u00f4.\3\2\2\2\u00f5\u00f6\7\61\2\2\u00f6\60\3\2\2")
        buf.write("\2\u00f7\u00f8\7\'\2\2\u00f8\62\3\2\2\2\u00f9\u00fa\7")
        buf.write("#\2\2\u00fa\64\3\2\2\2\u00fb\u00fc\7(\2\2\u00fc\u00fd")
        buf.write("\7(\2\2\u00fd\66\3\2\2\2\u00fe\u00ff\7~\2\2\u00ff\u0100")
        buf.write("\7~\2\2\u01008\3\2\2\2\u0101\u0102\7?\2\2\u0102\u0103")
        buf.write("\7?\2\2\u0103:\3\2\2\2\u0104\u0105\7#\2\2\u0105\u0106")
        buf.write("\7?\2\2\u0106<\3\2\2\2\u0107\u0108\7>\2\2\u0108>\3\2\2")
        buf.write("\2\u0109\u010a\7@\2\2\u010a@\3\2\2\2\u010b\u010c\7>\2")
        buf.write("\2\u010c\u010d\7?\2\2\u010dB\3\2\2\2\u010e\u010f\7@\2")
        buf.write("\2\u010f\u0110\7?\2\2\u0110D\3\2\2\2\u0111\u0112\7<\2")
        buf.write("\2\u0112\u0113\7<\2\2\u0113F\3\2\2\2\u0114\u0115\7.\2")
        buf.write("\2\u0115H\3\2\2\2\u0116\u0117\7=\2\2\u0117J\3\2\2\2\u0118")
        buf.write("\u0119\7<\2\2\u0119L\3\2\2\2\u011a\u011b\7}\2\2\u011b")
        buf.write("N\3\2\2\2\u011c\u011d\7\177\2\2\u011dP\3\2\2\2\u011e\u011f")
        buf.write("\7*\2\2\u011fR\3\2\2\2\u0120\u0121\7+\2\2\u0121T\3\2\2")
        buf.write("\2\u0122\u0123\7]\2\2\u0123V\3\2\2\2\u0124\u0125\7_\2")
        buf.write("\2\u0125X\3\2\2\2\u0126\u0127\7?\2\2\u0127Z\3\2\2\2\u0128")
        buf.write("\u0129\7\60\2\2\u0129\\\3\2\2\2\u012a\u013f\7\62\2\2\u012b")
        buf.write("\u012f\t\2\2\2\u012c\u012e\t\3\2\2\u012d\u012c\3\2\2\2")
        buf.write("\u012e\u0131\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3")
        buf.write("\2\2\2\u0130\u013a\3\2\2\2\u0131\u012f\3\2\2\2\u0132\u0134")
        buf.write("\7a\2\2\u0133\u0135\t\3\2\2\u0134\u0133\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2")
        buf.write("\u0137\u0139\3\2\2\2\u0138\u0132\3\2\2\2\u0139\u013c\3")
        buf.write("\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d")
        buf.write("\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013f\b/\2\2\u013e")
        buf.write("\u012a\3\2\2\2\u013e\u012b\3\2\2\2\u013f^\3\2\2\2\u0140")
        buf.write("\u0141\5]/\2\u0141\u0145\5[.\2\u0142\u0144\t\3\2\2\u0143")
        buf.write("\u0142\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2")
        buf.write("\u0145\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0145\3")
        buf.write("\2\2\2\u0148\u0149\b\60\3\2\u0149\u0162\3\2\2\2\u014a")
        buf.write("\u0152\5]/\2\u014b\u014f\5[.\2\u014c\u014e\t\3\2\2\u014d")
        buf.write("\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3")
        buf.write("\2\2\2\u0152\u014b\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154")
        buf.write("\3\2\2\2\u0154\u0155\5a\61\2\u0155\u0156\b\60\4\2\u0156")
        buf.write("\u0162\3\2\2\2\u0157\u015b\5[.\2\u0158\u015a\t\3\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u015b\3")
        buf.write("\2\2\2\u015e\u015f\5a\61\2\u015f\u0160\b\60\5\2\u0160")
        buf.write("\u0162\3\2\2\2\u0161\u0140\3\2\2\2\u0161\u014a\3\2\2\2")
        buf.write("\u0161\u0157\3\2\2\2\u0162`\3\2\2\2\u0163\u0165\t\4\2")
        buf.write("\2\u0164\u0166\t\5\2\2\u0165\u0164\3\2\2\2\u0165\u0166")
        buf.write("\3\2\2\2\u0166\u0168\3\2\2\2\u0167\u0169\t\3\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016a\u016b\3\2\2\2\u016bb\3\2\2\2\u016c\u016f\5e\63")
        buf.write("\2\u016d\u016f\5g\64\2\u016e\u016c\3\2\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016fd\3\2\2\2\u0170\u0171\7v\2\2\u0171\u0172")
        buf.write("\7t\2\2\u0172\u0173\7w\2\2\u0173\u0174\7g\2\2\u0174f\3")
        buf.write("\2\2\2\u0175\u0176\7h\2\2\u0176\u0177\7c\2\2\u0177\u0178")
        buf.write("\7n\2\2\u0178\u0179\7u\2\2\u0179\u017a\7g\2\2\u017ah\3")
        buf.write("\2\2\2\u017b\u017f\7$\2\2\u017c\u017e\5k\66\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0182\u0183\7$\2\2\u0183\u0184\b\65\6\2\u0184j\3\2\2")
        buf.write("\2\u0185\u018a\n\6\2\2\u0186\u0187\t\7\2\2\u0187\u018a")
        buf.write("\t\b\2\2\u0188\u018a\5m\67\2\u0189\u0185\3\2\2\2\u0189")
        buf.write("\u0186\3\2\2\2\u0189\u0188\3\2\2\2\u018al\3\2\2\2\u018b")
        buf.write("\u018c\7^\2\2\u018c\u018d\t\t\2\2\u018dn\3\2\2\2\u018e")
        buf.write("\u018f\7^\2\2\u018f\u0192\n\t\2\2\u0190\u0192\7^\2\2\u0191")
        buf.write("\u018e\3\2\2\2\u0191\u0190\3\2\2\2\u0192p\3\2\2\2\u0193")
        buf.write("\u0197\t\n\2\2\u0194\u0196\t\13\2\2\u0195\u0194\3\2\2")
        buf.write("\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198r\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019c")
        buf.write("\t\f\2\2\u019b\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a0\b:\7\2\u01a0t\3\2\2\2\u01a1\u01a2\7\61\2")
        buf.write("\2\u01a2\u01a3\7\61\2\2\u01a3\u01a7\3\2\2\2\u01a4\u01a6")
        buf.write("\n\r\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2")
        buf.write("\u01a9\u01a7\3\2\2\2\u01aa\u01ab\b;\7\2\u01abv\3\2\2\2")
        buf.write("\u01ac\u01ad\7\61\2\2\u01ad\u01ae\7,\2\2\u01ae\u01b2\3")
        buf.write("\2\2\2\u01af\u01b1\13\2\2\2\u01b0\u01af\3\2\2\2\u01b1")
        buf.write("\u01b4\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2")
        buf.write("\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7")
        buf.write(",\2\2\u01b6\u01b7\7\61\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9")
        buf.write("\b<\7\2\u01b9x\3\2\2\2\u01ba\u01bb\13\2\2\2\u01bbz\3\2")
        buf.write("\2\2\u01bc\u01c0\7$\2\2\u01bd\u01bf\5k\66\2\u01be\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0")
        buf.write("\u01c1\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2")
        buf.write("\u01c3\u01c5\t\16\2\2\u01c4\u01c3\3\2\2\2\u01c5|\3\2\2")
        buf.write("\2\u01c6\u01ca\7$\2\2\u01c7\u01c9\5k\66\2\u01c8\u01c7")
        buf.write("\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cd\u01ce\5o8\2\u01ce~\3\2\2\2\31\2\u012f\u0136\u013a")
        buf.write("\u013e\u0145\u014f\u0152\u015b\u0161\u0165\u016a\u016e")
        buf.write("\u017f\u0189\u0191\u0197\u019d\u01a7\u01b2\u01c0\u01c4")
        buf.write("\u01ca\b\3/\2\3\60\3\3\60\4\3\60\5\3\65\6\b\2\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FLOAT = 6
    FOR = 7
    FUNCTION = 8
    IF = 9
    INTEGER = 10
    RETURN = 11
    STRING = 12
    WHILE = 13
    VOID = 14
    OUT = 15
    CONTINUE = 16
    OF = 17
    INHERIT = 18
    ARRAY = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    REMAINDER = 24
    BOOL_NEGA = 25
    BOOL_CONJ = 26
    BOOL_DISJ = 27
    EQUAL = 28
    NOT_EQUAL = 29
    LESS_THAN = 30
    GREATER_THAN = 31
    LESS_THAN_EQ = 32
    GREATER_THAN_EQ = 33
    DOUBLE_COLON = 34
    COMMA = 35
    SEMI = 36
    COLON = 37
    LCB = 38
    RCB = 39
    LB = 40
    RB = 41
    LSB = 42
    RSB = 43
    EQ = 44
    DOT = 45
    INTLIT = 46
    FLOATLIT = 47
    BOOLLIT = 48
    TRUE = 49
    FALSE = 50
    STRINGLIT = 51
    ID = 52
    WS = 53
    SINGLE_LINE_COMMENT = 54
    MULTI_LINE_COMMENT = 55
    ERROR_CHAR = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'::'", 
            "','", "';'", "':'", "'{'", "'}'", "'('", "')'", "'['", "']'", 
            "'='", "'.'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
            "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", 
            "REMAINDER", "BOOL_NEGA", "BOOL_CONJ", "BOOL_DISJ", "EQUAL", 
            "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQ", "GREATER_THAN_EQ", 
            "DOUBLE_COLON", "COMMA", "SEMI", "COLON", "LCB", "RCB", "LB", 
            "RB", "LSB", "RSB", "EQ", "DOT", "INTLIT", "FLOATLIT", "BOOLLIT", 
            "TRUE", "FALSE", "STRINGLIT", "ID", "WS", "SINGLE_LINE_COMMENT", 
            "MULTI_LINE_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                  "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", 
                  "SUB", "MUL", "DIV", "REMAINDER", "BOOL_NEGA", "BOOL_CONJ", 
                  "BOOL_DISJ", "EQUAL", "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", 
                  "LESS_THAN_EQ", "GREATER_THAN_EQ", "DOUBLE_COLON", "COMMA", 
                  "SEMI", "COLON", "LCB", "RCB", "LB", "RB", "LSB", "RSB", 
                  "EQ", "DOT", "INTLIT", "FLOATLIT", "EXP", "BOOLLIT", "TRUE", 
                  "FALSE", "STRINGLIT", "STRING_CHAR", "ESCAPE", "ILL_CHAR", 
                  "ID", "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()

        if tk == self.UNCLOSE_STRING:
            y = str(result.text)
            if y[-1] == '\n' or y[-1] == '\r':
                raise UncloseString(y[1:-1])
            else:
                raise UncloseString(y[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text[1:])
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[45] = self.INTLIT_action 
            actions[46] = self.FLOATLIT_action 
            actions[51] = self.STRINGLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	y = str(self.text)
            	self.text = y.replace("_", "")

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	y = str(self.text)
            	self.text = y.replace("_", "")

     

        if actionIndex == 2:

            	y = str(self.text)
            	self.text = y.replace("_", "")

     

        if actionIndex == 3:

            	y = str(self.text)
            	self.text = y.replace("_", "")

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	y = str(self.text)
            	self.text = y[1:-1]	

     


