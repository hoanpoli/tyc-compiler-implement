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

var_decl_stmt: decl_type ID SEMI_COLON | decl_type ID ASSIGN expr SEMI_COLON;
var_decl: decl_type ID;

block_stmt: LB stmt_list RB;

decl_type: type | AUTO;

type: INT | FLOAT_KW | STRING | ID;

if_stmt: matched_if | unmatched_if;
matched_if: IF LP expr RP LB stmt_list RB ELSE block_stmt;
unmatched_if: IF LP expr RP block_stmt | IF LP expr RP matched_if ELSE unmatched_if;

while_stmt: WHILE LP expr LP LB stmt_list RB;
for_stmt: FOR LP for_init SEMI_COLON for_cond SEMI_COLON for_update RP LB stmt_list RB;
for_init: var_decl | expr | ;
for_cond: expr | ;
for_update: expr | ;

switch_stmt: SWITCH LP expr LP LB switch_body RB;
switch_body: default_then_cases
            | cases_then_default
            | cases_default_cases
            | cases_only;

default_then_cases: default_clause case_list;
cases_then_default: case_list default_clause;
cases_default_cases: case_list default_clause case_list;
cases_only: case_list;
case_list : case_clause case_list | case_clause;
case_clause: CASE case_expr COLON stmt_list break_stmt?;
default_clause: DEFAULT COLON stmt_list break_stmt?;

case_expr: case_add;
case_add: case_mul case_add_tail;
case_add_tail: ADD case_mul case_add_tail | SUB case_mul case_add_tail | ;
case_mul: case_unary case_mul_tail;
case_mul_tail: MUL case_add case_mul_tail 
                | DIV case_add case_mul_tail
                | MOD case_add case_mul_tail
                | ;
case_unary: ADD case_unary | SUB case_unary | case_primary;
case_primary: INTLIT | LP case_expr RP;

break_stmt: BREAK SEMI_COLON;
continue_stmt: CONTINUE SEMI_COLON;
return_stmt: RETURN expr SEMI_COLON | RETURN SEMI_COLON;

expr_stmt: expr SEMI_COLON;

expr: assign_expr;
assign_expr: postfix ASSIGN assign_expr | logic_or_expr;
logic_or_expr: logic_and logic_or_tail;
logic_or_tail: OR logic_and logic_or_tail | ;
logic_and: equality logic_and_tail;
logic_and_tail: AND equality logic_and_tail | ;
equality: relational equality_tail;
equality_tail: EQUAL relational equality_tail
                | NOT_EQUAL relational equality_tail
                | ;

relational: additive relational_tail;

relational_tail: LESS_THAN additive relational_tail
                | GREATER_THAN additive relational_tail
                | LESS_THAN_OR_EQUAL additive relational_tail
                | GREATER_THAN_OR_EQUAL additive relational_tail 
                | ;

additive: multiplicative additive_tail;

additive_tail: ADD multiplicative additive_tail
                | SUB multiplicative additive_tail
                | ;

multiplicative: unary multiplicative_tail;

multiplicative_tail: MUL unary multiplicative_tail 
                    | DIV unary multiplicative_tail
                    | MOD unary multiplicative_tail
                    | ;

unary: NOT unary
        | INC unary
        | DEC unary
        | SUB unary
        | postfix;

postfix: postfix DOT ID
        | postfix LP argument_list RP
        | postfix INC
        | postfix DEC
        | primary_expr;

primary_expr: ID
            | INTLIT
            | FLOATLIT
            | STRINGLIT
            | LP expr RP;
argument_list: expr argument_tail | ;
argument_tail: COMMA expr argument_tail | ;

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
STRINGLIT: '"' ( '\\' [bfrnt\\"] | ~["\\\r\n] )* '"' { self.text = self.text[1:-1] };

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs

ILLEGAL_ESCAPE: '"' (('\\'[bfrnt\\"]|~[\n\\"]))* ('\\'(~[bfrnt\\"]));
UNCLOSE_STRING:  '"'('\\'[bfrnt\\"]|~[\r\t\n\\"])* ;
ERROR_CHAR: . ;
