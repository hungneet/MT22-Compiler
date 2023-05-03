//ID: 2052504

grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: manydecl EOF;//
manydecl: decl manydecl | decl;//
decl: vardecl | funcdecl;//


//4. TYPE 4.1
atomic_type: BOOLEAN_K | INT_K | FLOAT_K | STRING_K;// 
//4.2
array_type: ARRAY_K dimension OF_K atomic_type;//
dimension: LBRACK intlist RBRACK;//
intlist: INTLIT COMMA intlist | INTLIT;//

arraylit: LBRACE nullable_explist RBRACE;//

//4.3, 4.4
dtype: atomic_type | array_type | VOID_K | AUTO_K;//

//5. DECLARATION

//5.1 Variable decl 5.1.1 variable
vardecl:  (simple_vardecl|full_vardecl) SEMI;//
simple_vardecl: idlist COLON dtype;//
full_vardecl: ID COMMA fullvar_helper COMMA exp 
			| ID COLON dtype EQUAL exp;//
fullvar_helper:	ID COMMA fullvar_helper COMMA exp 
			| ID COLON dtype EQUAL exp;//
			
idlist: ID COMMA idlist | ID ;//

//5.1.2 parameter


//5.2 function decl

// funcdecl: func_pro func_body;
funcdecl: ID COLON FUNCTION_K dtype LPAREN nullable_paralist RPAREN inherit blockstmt;
inherit : INHERIT_K ID|	;
nullable_paralist: paralist|;
paralist: paradecl COMMA paralist| paradecl;
paradecl: INHERIT_K? OUT_K? ID COLON dtype;
// func_body: blockstmt;

//6. EXPRESSIONS

//6.5 
index_opp: ID LBRACK exp_list RBRACK;//
//6.6 function call
funccall: ID LPAREN argument_list RPAREN;//
argument_list:  exp_list|;//
//6.7 
exp://
	<assoc = left> index_opp
	|<assoc = right> SUB exp
	|<assoc = right> NOT exp
	|<assoc = left> exp (MUL | DIV | MOD) exp
	|<assoc = left> exp (SUB | ADD) exp
	|<assoc = left> exp (AND | OR) exp
	|exp (EQ | NE | LT | GT | LE | GE) exp
	|exp SCOPE exp
	|operand;//
operand: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | ID |funccall | arraylit| LPAREN exp RPAREN;//

nullable_explist: exp_list|;//
exp_list: exp COMMA exp_list| exp;//

subexp: LPAREN exp RPAREN;


//7. STATEMENTS
stmt:
	assign_stmt
	| if_stmt
	| for_stmt
	| while_stmt
	| dowhile_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt
	| blockstmt;
//7.1 assignment
assign_stmt: lhs EQUAL exp SEMI;
lhs: ID | index_opp;

//7.2 if
if_stmt: IF_K LPAREN exp RPAREN stmt (ELSE_K stmt)?;
//7.3 for stmt
for_stmt:
	FOR_K LPAREN (ID EQUAL exp) COMMA exp COMMA exp RPAREN stmt;

//7.4 While 
while_stmt: WHILE_K LPAREN exp RPAREN stmt;
//7.5 do while
dowhile_stmt: DO_K blockstmt WHILE_K LPAREN exp RPAREN SEMI;
//7.6 break
break_stmt: BREAK_K SEMI;
//7.7 continue
continue_stmt: CONTINUE_K SEMI;
//7.8 return
return_stmt: RETURN_K exp? SEMI;
//7.9 call stmt
call_stmt: ID LPAREN argument_list RPAREN SEMI;
//7.10 block 
blockstmt: LBRACE (contentlist|) RBRACE ;
contentlist: content contentlist| content;
content: vardecl | blockstmt|stmt;


// //8 Special function
// specialfunction: readInt|printInt|readFloat | writeFloat| readBool| printBool | readString| printString| sup_exp| preventDefault;


//////////////////////////////////////// Tokens in MT22 language///////////////////////////////////////////

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

INTLIT: [0-9]|([1-9] ('_'* [0-9])+) {self.text = self.text.replace("_","")};
FLOATLIT: ('0' | ([1-9]) ('_'* [0-9])*) ('.' ([0-9])*)? (
		('e' | 'E') ('+' | '-')? ([0-9])+
	)? {self.text = self.text.replace("_","")};

BOOLLIT: ('true' | 'false');
COMMENT: ('//' ~[\r\n]* | '/*' .*? '*/') -> skip;
STRINGLIT:
	'"' (~["\r\n\\] | '\\' [btnfr"'\\])* '"' {self.text = self.text[1:-1]};

//Operator
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
NE: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
SCOPE: '::';

// Separators in MT22 language
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LBRACE: '{';
RBRACE: '}';
EQUAL: '=';

// MT22 keywords

// KEYWORD:AUTO_K | BREAK_K | BOOLEAN_K |DO_K | ELSE_K| FALSE_K| FLOAT_K | FOR_K | FUNCTION_K| IF_K
// | INT_K | RETURN_K | STRING_K| | TRUE_K|WHILE_K | VOID_K| OUT_K| CONTINUE_K| OF_K | INHERIT_K |
// ARRAY_K;
AUTO_K: 'auto';
BREAK_K: 'break';
BOOLEAN_K: 'boolean';
DO_K: 'do';
ELSE_K: 'else';
FALSE_K: 'false';
FLOAT_K: 'float';
FOR_K: 'for';
FUNCTION_K: 'function';
IF_K: 'if';
INT_K: 'integer';
RETURN_K: 'return';
STRING_K: 'string';
TRUE_K: 'true';
WHILE_K: 'while';
VOID_K: 'void';
OUT_K: 'out';
CONTINUE_K: 'continue';
OF_K: 'of';
INHERIT_K: 'inherit';
ARRAY_K: 'array';

ID: ([a-z] | [A-Z] | '_') ([a-z] | [A-Z] | '_' | [0-9])*;


ERROR_CHAR: .{raise ErrorToken(self.text)} ;

fragment STRING_UNCLOSE: '"' ( '\\' [btnfr"'\\] | ~[\r\n\\"])*;
UNCLOSE_STRING:
	STRING_UNCLOSE { raise UncloseString(self.text[1:])};

fragment ESCAPE_ILLEGAL:
	'"' ('\\' [btnfr"'\\] | ~[\r\n\\"])* '\\' ~[btnfr"'\\];
ILLEGAL_ESCAPE:
	ESCAPE_ILLEGAL {raise IllegalEscape(self.text[1:])};

