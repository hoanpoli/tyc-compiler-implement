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
decl_list: decl decl_list | ;
decl: struct_decl | func_decl;

func_decl: func_return ID LP param_list RP block_stmt;
func_return: return_type | ;
return_type: type | VOID;
param_list: param_prime | ;
param_prime: param_decl COMMA param_list | param_decl;
param_decl: type ID;
stmt_list: stmt stmt_list | ;

struct_decl: STRUCT ID LB struct_body_list RB SEMI_COLON;
struct_body_list: struct_member_list | ;
struct_member_list: struct_body struct_body_list | struct_body;
struct_body: type ID SEMI_COLON;

stmt: var_decl_stmt | block_stmt | if_stmt | while_stmt | for_stmt | switch_stmt | break_stmt | continue_stmt | return_stmt | expr_stmt;

var_decl_stmt: decl_type ID var_init SEMI_COLON;
var_init: ASSIGN expr | ;

block_stmt: LB stmt_list RB;

decl_type: type | AUTO;

type: INT | FLOAT_KW | STRING | ID;

if_stmt: IF LP expr RP stmt else_part;
else_part: ELSE stmt | ;

while_stmt: WHILE LP expr RP stmt;
for_stmt: FOR LP for_init SEMI_COLON for_cond SEMI_COLON for_update RP stmt;
for_init: for_var_decl | expr | ;
for_var_decl: decl_type ID | decl_type ID ASSIGN expr;

for_cond: expr | ;
for_update: expr | ;

switch_stmt: SWITCH LP expr RP LB switch_body RB;
switch_body: switch_item_list | ;
switch_item_list: switch_item switch_item_list | switch_item;
switch_item: case_clause | default_clause;

case_clause: CASE case_expr COLON stmt_list;
default_clause: DEFAULT COLON stmt_list;

case_expr: case_add;

case_add: case_add ADD case_mul
        | case_add SUB case_mul
        | case_mul;

case_mul: case_mul MUL case_unary
        | case_mul DIV case_unary
        | case_mul MOD case_unary
        | case_unary;

case_unary: ADD case_unary
            | SUB case_unary
            | case_primary;

case_primary: INTLIT | LP case_expr RP;

break_stmt: BREAK SEMI_COLON;
continue_stmt: CONTINUE SEMI_COLON;
return_stmt: RETURN return_expr SEMI_COLON;
return_expr: expr | ;

expr_stmt: expr SEMI_COLON;

expr: assign_expr;
assign_expr: logic_or_expr | logic_or_expr ASSIGN assign_expr;
logic_or_expr: logic_or_expr OR logic_and_expr | logic_and_expr;
logic_and_expr: logic_and_expr AND equality_expr | equality_expr;
equality_expr: equality_expr EQUAL relational_expr
                | equality_expr NOT_EQUAL relational_expr
                | relational_expr;

relational_expr: relational_expr LESS_THAN additive_expr
                | relational_expr GREATER_THAN additive_expr
                | relational_expr LESS_THAN_OR_EQUAL additive_expr
                | relational_expr GREATER_THAN_OR_EQUAL additive_expr
                | additive_expr;

additive_expr: additive_expr ADD multiplicative_expr
                | additive_expr SUB multiplicative_expr
                | multiplicative_expr;

multiplicative_expr: multiplicative_expr MUL unary_expr
                    | multiplicative_expr DIV unary_expr
                    | multiplicative_expr MOD unary_expr
                    | unary_expr;

unary_expr: prefix_expr| postfix_expr;

prefix_expr: NOT unary_expr
            | ADD unary_expr
            | SUB unary_expr
            | INC unary_expr
            | DEC unary_expr;

postfix_expr: primary_expr
            | postfix_expr postfix_suffix;

postfix_suffix
    : LP argument_list RP
    | DOT ID
    | INC
    | DEC;

primary_expr: ID
            | INTLIT
            | FLOATLIT
            | STRINGLIT
            | LP expr RP
            | struct_literal;

struct_literal: LB argument_list RB;

argument_list: expr argument_tail | ;
argument_tail: COMMA expr argument_tail | ;

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';
EQUAL: '==';
ASSIGN: '=';
INC: '++';
DEC: '--';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT_EQUAL: '!=';
LESS_THAN: '<';
GREATER_THAN: '>';
OR: '||';
AND: '&&';
NOT: '!';

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

INTLIT: [0-9]+;
FLOATLIT: ( [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)? | '.' [0-9]+ ([eE] [+-]? [0-9]+)? | [0-9]+ [eE] [+-]? [0-9]+ ) ;

ILLEGAL_ESCAPE: '"' ( ESC_SEQ | ~["\\\r\n] )* '\\' ~[bfrnt"\\\r\n] { self.text = self.text[1:]; };
UNCLOSE_STRING: '"' (ESC_SEQ | ~["\\\r\n])* { self.text = self.text[1:] };
STRINGLIT : '"' ( ESC_SEQ | ~["\\\r\n] )* '"' { self.text = self.text[1:-1]; };

fragment ESC_SEQ: '\\' [bfrnt"\\];

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs

ERROR_CHAR: . ;
