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
- WHILE:
- CONTINUE:
- BREAK:
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
- DECIMAL_NUMBER: '[0- 9]+ (' .' [0- 9]+)?'
- VARIABLE: '[a- zA- Z_]+'
- OPEN_BRACET: '('
- CLOSET_BRACKET: ')'
## Grammar:
### program: (class_def | function | statement | comment) + **something in mongolian to end the proram**
### class_def
### function: FUNCT_NAME VARIABLE OPEN_BRACET args? CLOSE_BRACKET START_FUNCTION function_body END_FUNCTION
### args: VAR_TYPE VARIABLE (',' VAR_TYPE VARIABLE)*
### function_body: assign | for | if | while | return | embeded_func | comment
### assign: VAR_TYPE VARIABLE ASSIGN_VALUE (VARIABLE|DECIMAL_NUMBER)
### for: 
### if:
### while:
### return:
### embeded_func:
### comment: COMMENT STRING NEW_LINE | START_LONG_COMMENT STRING END_LONG_COMMENT


