grammar MGprogramming;


// Tokens

ASSIGN_VALUE: 'todorhoiloh';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: ':';
POWER: '^';
MODULO: '|';
GREATER_THAN: '>';
LESSER_THAN: '<';
GREATER_OR_EQUAL: '>=';
LESSER_OR_EQUAL: '<=';
EQUAL: '=';
NOT_EQUAL: '=/=';
NEW_LINE: '\n';
START_FUNCTION: 'ehleh';
END_FUNCTION: 'duusgah';
CLASS_DEF: 'angi';
START_CLASS: 'ehleh_angi';
END_CLASS: 'duusgah_angi';
START_LOOP: 'ehleh_davtalt';
END_LOOP: 'duusgah_davtalt';
WHILE: 'zuur';
CONTINUE: 'urgeljleh';
BREAK: 'zavsar';
FOR: 'd';
FOR_FROM: 'aas';
FOR_TO: 'tuld';
FOR_JUMP: 'nii tuld';
IF: 'hervee';
ELSE: 'mon';
FUNCT_DEF: 'ner';
RETURN: 'butsah';
PRINT: 'hevleh';
INPUT: 'orolt';
FUNCTION_CALL: 'zalgakh';
CLASS_INSTANCE: 'jishee';
ELSE_IF:'öör bol';

INT: 'buhel';
LONG: 'urt';
FLOAT: 'butarhai';
DOUBLE: 'ih_butarhai';
CHAR: 'temdegt';
STRING: 'mor';
BOOLEAN: 'tiim_ugui';
LIST: 'jagsaalt';
SET: 'bagts';
DICT: 'buleg';

AND:'bolon';
OR: 'esvel';
TRUE:'ünen';
FALSE:'khudal';
NOT: '!';


COMMENT: '>>' ~[\r\n]* -> skip;

START_LONG_COMMENT: '>>>' .*? '<<<' -> skip;

NUMBER: [0-9]+ ('.' [0-9]+)?;

VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*;

STRING_LITERAL: '"' ('\\"' | .)*? '"';


OPEN_BRACKET: '(';

CLOSE_BRACKET: ')';

OPEN_LIST_BRACKET: '[';

CLOSE_LIST_BRACKET: ']';

DICT_OPEN_BRACKET: '{';

DICT_CLOSE_BRACKET: '}';


// Skip white spaces

WS: [ \t\r\n]+ -> skip;

//Grammar rules

program: codes* EOF;

codes: class_ | function_def | statement NEW_LINE?;

class_: CLASS_DEF VARIABLE START_CLASS class_body END_CLASS;

class_instance: CLASS_INSTANCE VARIABLE OPEN_BRACKET args? CLOSE_BRACKET;

class_body: (function_def | declare)*;

function_def: FUNCT_DEF arg_types? VARIABLE OPEN_BRACKET args? CLOSE_BRACKET START_FUNCTION (statement)* (return_stmt)? END_FUNCTION;

args: arg_types VARIABLE (',' arg_types VARIABLE)*;

return_stmt: RETURN returners;

returners: TRUE | FALSE | VARIABLE | NUMBER | STRING_LITERAL;

statement: print 
    | if_statement 
    | for_loop 
    | while_loop 
    | assign 
    | declare 
    | function_call 
    | comment
    |NEW_LINE;

arg_types: INT | LONG | FLOAT | DOUBLE | CHAR | STRING | BOOLEAN | LIST | SET | DICT;

print: PRINT OPEN_BRACKET printers CLOSE_BRACKET;

printers: arithmetic_expr | bool_expr | VARIABLE | function_call | STRING_LITERAL | class_instance;

if_statement: IF OPEN_BRACKET bool_expr CLOSE_BRACKET START_LOOP loop_body  END_LOOP (else_if_statement)* (else_statement)?;

else_if_statement: ELSE_IF OPEN_BRACKET bool_expr CLOSE_BRACKET START_LOOP loop_body  END_LOOP;

else_statement: ELSE START_LOOP loop_body (return_stmt)? END_LOOP;

for_loop: FOR arg_types? VARIABLE for_statement START_LOOP loop_body END_LOOP;  

for_statement: FOR_FROM NUMBER FOR_TO NUMBER FOR_JUMP NUMBER
             | FOR_FROM NUMBER FOR_TO NUMBER
             | FOR_TO NUMBER
             | FOR_TO NUMBER FOR_JUMP NUMBER;

while_loop: WHILE OPEN_BRACKET bool_expr CLOSE_BRACKET START_LOOP loop_body (return_stmt)? END_LOOP;

loop_body: (statement)*;

assign: VARIABLE ASSIGN_VALUE printers;

declare: arg_types VARIABLE | arg_types VARIABLE ASSIGN_VALUE printers;

variables: (VARIABLE|NUMBER|STRING_LITERAL) (',' (VARIABLE|NUMBER|STRING_LITERAL))*;

function_call: FUNCTION_CALL VARIABLE OPEN_BRACKET variables? CLOSE_BRACKET;

comment: COMMENT  NEW_LINE | START_LONG_COMMENT;

bool_expr: bool_expr (AND | OR) bool_expr 
                           | arithmetic_expr (GREATER_THAN | LESSER_THAN | GREATER_OR_EQUAL | LESSER_OR_EQUAL | EQUAL | NOT_EQUAL) arithmetic_expr
                           | TRUE 
                           | FALSE 
                           | VARIABLE 
                           | NOT bool_expr 
                           | OPEN_BRACKET bool_expr CLOSE_BRACKET 
                           | function_call;

arithmetic_expr: VARIABLE
                 | NUMBER
                 | function_call
                 | OPEN_BRACKET arithmetic_expr CLOSE_BRACKET
                 | arithmetic_expr ( PLUS | MINUS | MULTIPLY | DIVIDE | POWER | MODULO ) arithmetic_expr;
                 
array: OPEN_LIST_BRACKET (STRING_LITERAL | NUMBER) (',' (STRING_LITERAL | NUMBER))* CLOSE_LIST_BRACKET;

table: OPEN_LIST_BRACKET array* CLOSE_LIST_BRACKET;

dictionary: DICT_OPEN_BRACKET (VARIABLE ':' (STRING_LITERAL | NUMBER | array) (',' VARIABLE ':' (STRING_LITERAL | NUMBER | array))*)? DICT_CLOSE_BRACKET;
