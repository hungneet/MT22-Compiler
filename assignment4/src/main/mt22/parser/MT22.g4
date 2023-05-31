// 2010301
grammar MT22;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}


options{
	language=Python3;
}

program			: decllist EOF ;

// ------------------------------------------------------------//
// ------------------------- Parser -------------------------- //
// ------------------------------------------------------------//

// vardecl, funcdecl
decllist				: decl decllist | decl ;
decl					: vardecl | funcdecl ;

// ------------------------- Variable Declarations -------------------------- //
// Variables: <identifer-list>: <type> [= <expression-list>]?;
vardecl					: vardecl_short_form | vardecl_full_form 
						| vardecl_array_full | vardecl_array_short ;

vardecl_short_form		: idlist COLON var_type SEMI ;
vardecl_full_form 		: ID var_recur expr SEMI ;
var_recur   			: COLON var_type EQ | COMMA ID var_recur expr COMMA ;

vardecl_array_short		: idlist COLON array_type SEMI ;
vardecl_array_full		: ID varecur_array array_value_list SEMI ;
varecur_array			: COLON array_type EQ | COMMA ID varecur_array array_value_list COMMA ;

// [2,2]
dimension				: LSB intlist RSB ;

// {{1,3}, {2,4}}
array_value_list		: LCB array_value_prime RCB | expr ;
array_value_prime		: LCB array_value_prime RCB | array_value | ;
array_value				: exprlist | ;


// Parameters
paramlist				: paramprime | ;
paramprime				: paramdecl COMMA paramprime | paramdecl ;
paramdecl				: INHERIT? OUT? ID COLON (array_type | var_type) ;


// ------------------------- Function Declaration -------------------------- //
funcdecl				: func_head func_body ;
func_head				: ID COLON FUNCTION return_type (LB paramlist RB) (INHERIT ID)? ;
func_body				: block_stmt ;

// Type
element_type			: INTEGER | FLOAT | STRING | BOOLEAN ;
var_type				: element_type | AUTO ;
return_type				: var_type | VOID | array_type ;
array_type				: ARRAY dimension OF element_type ;
// array_type			: ID COLON ARRAY LSB intlist RSB OF element_type ;	

// List
idlist					: ID COMMA idlist | ID ;
intlist					: INTLIT COMMA intlist | INTLIT ;


// ------------------------- Expression -------------------------- //

exprlist			: expr COMMA exprlist | expr ;

expr				: expr1 DOUBLE_COLON expr1 | expr1 ;
expr1				: expr2 relational expr2 | expr2 ;
expr2				: expr2 (BOOL_CONJ | BOOL_DISJ) expr3 | expr3 ;
expr3				: expr3 (ADD | SUB) expr4 | expr4 ;
expr4				: expr4 (MUL | DIV | REMAINDER) expr5 | expr5 ;
expr5				: BOOL_NEGA expr5 | expr6 ;
expr6				: SUB expr6 | expr7 ;
expr7				: indexOperator | operands ;

relational          : EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_EQ | GREATER_THAN_EQ ;
// indexOperator		: ID LSB exprlist? RSB ; // Different
indexOperator		: ID LSB exprlist RSB ;

allLiterals 		: (INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit) ;
funcCall			: ID LB argulist RB ;	
argulist			: arguprime | ;
arguprime			: argu COMMA arguprime | argu ;
argu				: operands | expr ;
operands			: allLiterals | ID | funcCall | LB expr RB ;
array_lit			: LCB exprlist? RCB;


// ------------------------- Statements -------------------------- //
stmtlist		: stmt stmtlist | ;

// stmt			: vardecl | assign_stmt | if_stmt | for_stmt 
// 				| while_stmt | dowhile_stmt | break_stmt | continue_stmt 
// 				| return_stmt | call_stmt | block_stmt ;

stmt			: assign_stmt | if_stmt | for_stmt 
				| while_stmt | dowhile_stmt | break_stmt | continue_stmt 
				| return_stmt | call_stmt | block_stmt ;

body_stmt		: block_stmt | stmt | SEMI ;

boolean_exprlist 	: expr ;

// Assignment Statement
assign_stmt		: (ID | ID LSB exprlist RSB) EQ expr SEMI ;

// If Statement
if_stmt			: IF (LB boolean_exprlist RB) body_stmt (ELSE body_stmt)? ; // Diffrent

// For Statement
for_stmt		: FOR (LB init_var COMMA expr COMMA update_expr RB) body_stmt ;

update_expr		: expr |  ;

// init_var		: ID EQ expr ;
init_var		: (ID | ID LSB exprlist RSB) EQ expr ;

// While Statement
while_stmt		: WHILE (LB boolean_exprlist RB) body_stmt ;

// Do-while Statement
dowhile_stmt	: DO block_stmt WHILE (LB boolean_exprlist RB) SEMI ;

// Break Statement
break_stmt		: BREAK SEMI ; 

// Continue Statement
continue_stmt	: CONTINUE SEMI ; 

// Return Statement
return_stmt		: RETURN expr? SEMI ; 

// Call Statement
call_stmt			: ID LB callElementList RB SEMI ; 
callElementList		: callElementPrime | ;
callElementPrime	: expr COMMA callElementPrime | expr ;

// Block Statement
// block_stmt		: LCB stmtlist RCB ;

block_stmt		: LCB blocklist RCB ;
blocklist		: block_prime | ;
block_prime		: block block_prime | block ;
block			: stmt | vardecl ;

// ------------------------------------------------------------//
// ------------------------- Lexer -------------------------- //
// ------------------------------------------------------------//

// -------------------- Define keywords -------------------- //
AUTO			: 'auto' ;
BREAK			: 'break' ;
BOOLEAN			: 'boolean' ;
DO				: 'do' ;
ELSE			: 'else' ;
FLOAT			: 'float' ;
FOR				: 'for' ;
FUNCTION		: 'function' ;
IF				: 'if' ;
INTEGER			: 'integer' ;
RETURN			: 'return' ;
STRING			: 'string' ;
WHILE			: 'while' ;
VOID			: 'void' ;
OUT				: 'out' ;
CONTINUE		: 'continue' ;
OF				: 'of' ;
INHERIT			: 'inherit' ;
ARRAY			: 'array' ;

// Operators
ADD                 : '+' ;
SUB                 : '-' ;
MUL                 : '*' ;
DIV    				: '/' ;
REMAINDER           : '%' ;

BOOL_NEGA           : '!' ;
BOOL_CONJ           : '&&' ;
BOOL_DISJ           : '||' ;

EQUAL               : '==' ;
NOT_EQUAL           : '!=' ;
LESS_THAN           : '<' ;
GREATER_THAN        : '>' ;
LESS_THAN_EQ        : '<=' ;
GREATER_THAN_EQ		: '>=' ;
DOUBLE_COLON		: '::' ;

// Separators
COMMA      			: ',' ;
SEMI    			: ';' ;
COLON   			: ':' ;
LCB      			: '{' ;
RCB					: '}' ;
LB      			: '(' ;
RB      			: ')' ;
LSB     			: '[' ;
RSB     			: ']' ;
EQ  			    : '=' ;
DOT     			: '.' ;


// Int Literals [1-9][0-9]*(_[0-9]+)*
INTLIT		: '0' | [1-9][0-9]*('_'[0-9]+)*
{
	y = str(self.text)
	self.text = y.replace("_", "")
} ;
// Float literal
FLOATLIT: INTLIT DOT [0-9]*
{
	y = str(self.text)
	self.text = y.replace("_", "")
}
		| INTLIT (DOT [0-9]*)? EXP
{
	y = str(self.text)
	self.text = y.replace("_", "")
} 
		| DOT [0-9]* EXP
{
	y = str(self.text)
	self.text = y.replace("_", "")
} 
;

fragment EXP: ('e' | 'E') [+-]? [0-9]+ ;

// Boolean literal
BOOLLIT						: TRUE | FALSE ;
TRUE						: 'true' ;
FALSE						: 'false' ;

// String literal
STRINGLIT                   : '"' STRING_CHAR* '"'
{
	y = str(self.text)
	self.text = y[1:-1]	
};

fragment STRING_CHAR		: ~[\n"'\\] | [\\]["] | ESCAPE ;
fragment ESCAPE				: '\\'[bfntr'\\] ;
fragment ILL_CHAR			: '\\' ~[bfrnt'\\] | '\\' ;


// Identifiers and literals
ID			: [A-Za-z_][A-Za-z0-9_]* ;

WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines


SINGLE_LINE_COMMENT : '//' ~[\r\n]* -> skip ;
MULTI_LINE_COMMENT 	: '/*' .*? '*/' ->skip ;

ERROR_CHAR			: .;
UNCLOSE_STRING		: '"' STRING_CHAR* ([\n\r] |EOF) ;
ILLEGAL_ESCAPE		: '"' STRING_CHAR* ILL_CHAR ;
