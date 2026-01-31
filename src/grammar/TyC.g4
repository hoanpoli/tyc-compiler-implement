grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
program: decl_list EOF;
decl_list: decl decl_list | decl;
decl: struct_decl | func_decl;

func_decl: func_return ID LP param_list RP LB stmt_list RB;
func_return: return_type | ;
return_type: type | VOID;
param_list: param_prime | ;
param_prime: param_decl COMMA param_list | param_decl;
param_decl: type ID;
stmt_list: stmt stmt_list | stmt;

struct_decl: STRUCT ID LB struct_body_list RB SEMI_COLON;
struct_body_list: struct_prime | ;
struct_prime: struct_body SEMI_COLON struct_body_list | struct_body;
struct_body: type ID;

stmt: var_decl_stmt | block_stmt | if_stmt | while_stmt | for_stmt | switch_stmt | break_stmt | continue_stmt | return_stmt | expr_stmt;

var_decl_stmt: var_decl assign_expr SEMI_COLON;
var_decl: decl_type ID;

block_stmt: LB stmt_list RB;

decl_type: type | AUTO;

type: INT | FLOAT_KW | STRING | ID;

assign_expr: ASSIGN expr | ;
if_stmt: expr;
while_stmt: expr;
for_stmt: expr;
switch_stmt: expr;
break_stmt: expr;
continue_stmt: expr;
return_stmt: expr;
expr_stmt: expr SEMI_COLON;
expr: ID;

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

ASSIGN: '=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT_EQUAL: '!=';
EQUAL: '==';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';
OR: '||';
AND: '&&';
NOT: '!';
INC: '++';
DEC: '--';

LSB: '[';
RSB:']';
LP: '(';
RP: ')';
LB: '{';
RB: '}';
SEMI_COLON: ';';
COLON: ':';
DOT: '.';
COMMA: ',';

AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT_KW: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

ID: [a-zA-Z_][a-zA-Z_0-9]*;

INTLIT: '-'?[0-9]+;
FLOATLIT: '-'? ( [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)? | '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+ ) ;
STRINGLIT: '"' ( '\\' [bfrnt\\"] | ~["\\\r\n] )* '"';

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs

ILLEGAL_ESCAPE: '"' (('\\'[bfrnt\\"]|~[\n\\"]))* ('\\'(~[bfrnt\\"]));
UNCLOSE_STRING:  '"'('\\'[bfrnt\\"]|~[\r\t\n\\"])* ;
ERROR_CHAR: . ;
