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
FUNCT_NAME: 'ner';
RETURN: 'butsah';
PRINT: 'hevleh';
INPUT: 'orolt';

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


COMMENT: '>>' ~[\r\n]* -> skip;
START_LONG_COMMENT: '>>>' ~[\r\n]* '<<<' -> skip;

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

// Grammar rules
program: (class_def | function_def | statement)+ EOF;
var_type: INT | LONG | FLOAT | DOUBLE | CHAR | STRING | BOOLEAN | LIST | SET | DICT;

statement: assign
         | print
         | for_loop 
         | if_stmt 
         | while_loop 
         | return_stmt 
         | function_call;

class_def: CLASS_DEF VARIABLE START_CLASS (function_def | statement)* END_CLASS NEW_LINE;

function_def: FUNCT_NAME VARIABLE OPEN_BRACKET args? CLOSE_BRACKET START_FUNCTION function_body END_FUNCTION NEW_LINE;

args: var_type VARIABLE (',' var_type VARIABLE)* ;

function_body: (assign | for_loop | if_stmt | while_loop | return_stmt | function_call)+;

value: VARIABLE | NUMBER | STRING_LITERAL NEW_LINE;
assign: var_type VARIABLE ASSIGN_VALUE value NEW_LINE;

print: PRINT OPEN_BRACKET value CLOSE_BRACKET NEW_LINE;

for_loop: FOR VARIABLE FOR_FROM NUMBER FOR_TO NUMBER FOR_JUMP NUMBER OPEN_BRACKET loop_body CLOSE_BRACKET;

if_stmt: IF OPEN_BRACKET VARIABLE (EQUAL | GREATER_THAN | LESSER_THAN | GREATER_OR_EQUAL | LESSER_OR_EQUAL) (NUMBER | STRING_LITERAL) CLOSE_BRACKET START_LOOP loop_body END_LOOP;

while_loop: WHILE OPEN_BRACKET VARIABLE CLOSE_BRACKET START_LOOP loop_body END_LOOP;

loop_body: (statement | function_call)+;

return_stmt: RETURN (VARIABLE | NUMBER | STRING_LITERAL) NEW_LINE;

function_call: FUNCT_NAME VARIABLE OPEN_BRACKET (VARIABLE (',' VARIABLE)*)? CLOSE_BRACKET NEW_LINE;

array: OPEN_LIST_BRACKET (STRING_LITERAL | NUMBER) (',' (STRING_LITERAL | NUMBER))* CLOSE_LIST_BRACKET;

table: OPEN_LIST_BRACKET array* CLOSE_LIST_BRACKET;

dictionary: DICT_OPEN_BRACKET (VARIABLE ':' (STRING_LITERAL | NUMBER | array) (',' VARIABLE ':' (STRING_LITERAL | NUMBER | array))*)? DICT_CLOSE_BRACKET;
