# MGProgramming

## Tokens:
- ASSIGN_VALUE: '<- '(MONGOLIAN 'ASSIGN' OR STH LIKE THAT)
- PLUS: '+';
- MINUS: '- '
- MULTIPLY: '*'
- DIVIDE: ':'
- POWER: '^'
- MODULO: '|'
- GREATER_THAN: '>'
- LESSER_THAN: '<'
- GREATER_OR_EQUAL: '>='
- LESSER_OR_EQUAL: '<='
- EQUAL: '='
- NOT_EQUAL: '=/='
- NEW_LINE: '\n'
- START_FUNCTION: '{'**start and finish in mongolian**
- END_FUNCTION: '}'
- CLASS_DEF:
- START_CLASS:
- END_CLASS:
- START_LOOP:
- END_LOOP:
- WHILE:
- CONTINUE:
- BREAK:
- FOR:
- FOR_FROM:
- FOR_TO:
- FOR_JUMP:
- IF:
- FUNCT_NAME:
- RETURN:
- PRINT:
- INPUT:
- VAR_TYPE:
  - INT:
  - LONG:
  - FLOAT:
  - DOUBLE:
  - CHAR:
  - STR:
  - BOOLEAN:
  - LIST:
  - SET:
  - DICT:
- COMMENT:'>>'
- START_LONG_COMMENT: '>>>'
- END_LONG_COMMENT: '<<<'
- NUMBER: '[0- 9]+ (' .' [0- 9]+)?'
- VARIABLE: '[a- zA- Z_]+'
- OPEN_BRACET: '('
- CLOSE_BRACKET: ')'
## Grammar:
```g4
program: (class_def | function | statement | comment)+ **something in mongolian to end the proram**

statement: statement: assign
         | for
         | if
         | while
         | return
         | embedded_func
         | comment
         ;

class_def: CLASS_DEF VARIABLE START_CLASS (function | statement | comment)* END_CLASS NEW_LINE

function: FUNCT_NAME VARIABLE OPEN_BRACET args? CLOSE_BRACKET START_FUNCTION function_body END_FUNCTION NEW_LINE

args: VAR_TYPE VARIABLE (',' VAR_TYPE VARIABLE)* NEW_LINE

function_body: (assign | for | if | while | return | function_call | comment)+

assign: VAR_TYPE VARIABLE ASSIGN_VALUE (VARIABLE|DECIMAL_NUMBER) NEW_LINE

for: FOR VARIABLE FOR_FROM NUMBER FOR_TO NUMBER FOR_JUMP NUMBER OPEN_BRACKET loop_body CLOSE_BRACKET

if: IF OPEN_BRACKET VARIABLE (EQUAL | GREATER_THAN | LESSER_THAN | GREATER_OR_EQUAL | SMALLER_OR_EQUAL) (NUMBER | STRING) CLOSE_BRACKET OPEN_LOOP loop_body CLOSE_LOOP

while: WHILE OPEN_BRACKET variable CLOSE_BRACKET OPEN_LOOP loop_body CLOSE_LOOP

loop_body: (statement | function_call)+ NEW_LINE;

return: RETURN (VARIABLE | NUMBER | STRING) NEW_LINE;

function_call: FUNCT_NAME OPEN_BRACET args? CLOSE_BRACKET NEW_LINE;

comment: COMMENT STRING NEW_LINE | START_LONG_COMMENT STRING END_LONG_COMMENT
```


