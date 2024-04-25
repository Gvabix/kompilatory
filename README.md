# MGProgramming

## Tokens:
- ASSIGN_VALUE: 'todorhoiloh'
- PLUS: '+'
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
- START_FUNCTION: 'ehleh'
- END_FUNCTION: 'duusgah'
- CLASS_DEF: 'angi'
- START_CLASS: 'ehleh_angi'
- END_CLASS: 'duusgah_angi'
- START_LOOP: 'ehleh_davtalt'
- END_LOOP:'duusgah_davtalt'
- WHILE: 'zuur'
- CONTINUE: 'urgeljleh'
- BREAK: 'zavsar' 
- FOR: 'd'
- FOR_FROM: 'aas'
- FOR_TO: 'tuld'
- FOR_JUMP: 'nii tuld'
- IF: 'hervee'
- FUNCT_NAME: 'ner'
- RETURN: 'butsah'
- PRINT: 'hevleh'
- INPUT: 'orolt'
- VAR_TYPE:
  - INT:'buhel'
  - LONG:'urt'
  - FLOAT:'butarhai'
  - DOUBLE: 'ih_butarhai'
  - CHAR: 'temdegt'
  - STRING: 'mor'
  - BOOLEAN: 'tiim_ugui'
  - LIST: 'jagsaalt'
  - SET: 'bagts'
  - DICT: 'buleg'
- COMMENT:'>>'
- START_LONG_COMMENT: '>>>'
- END_LONG_COMMENT: '<<<'
- NUMBER: '[0- 9]+ (' .' [0- 9]+)?'
- VARIABLE: '[a- zA- Z_]+'
- OPEN_BRACKET: '('
- CLOSE_BRACKET: ')'
- OPEN_LIST_BRACKET: '['
- CLOSE_LIST_BRACKET : ']'
- DICT_OPEN_BRACKET: '{'
- DICT_CLOSE_BRACKET: '}'
## Grammar:
```g4
program: (class_def | function | statement | comment)+ **Sain baina uu?**

statement: assign | for | if | while | return | embedded_func | comment

class_def: CLASS_DEF VARIABLE START_CLASS (function | statement | comment)* END_CLASS NEW_LINE

function: FUNCT_NAME VARIABLE OPEN_BRACKET args? CLOSE_BRACKET START_FUNCTION function_body END_FUNCTION NEW_LINE

args: VAR_TYPE VARIABLE (',' VAR_TYPE VARIABLE)* NEW_LINE

function_body: (assign | for | if | while | return | function_call | comment)+

assign: VAR_TYPE VARIABLE ASSIGN_VALUE (VARIABLE|DECIMAL_NUMBER) NEW_LINE

for: FOR VARIABLE FOR_FROM NUMBER FOR_TO NUMBER FOR_JUMP NUMBER OPEN_BRACKET loop_body CLOSE_BRACKET

if: IF OPEN_BRACKET VARIABLE (EQUAL | GREATER_THAN | LESSER_THAN | GREATER_OR_EQUAL | SMALLER_OR_EQUAL) (NUMBER | STRING) CLOSE_BRACKET OPEN_LOOP loop_body CLOSE_LOOP

while: WHILE OPEN_BRACKET variable CLOSE_BRACKET OPEN_LOOP loop_body CLOSE_LOOP

loop_body: (statement | function_call)+ NEW_LINE

return: RETURN (VARIABLE | NUMBER | STRING) NEW_LINE

function_call: FUNCT_NAME OPEN_BRACET args? CLOSE_BRACKET NEW_LINE

comment: COMMENT STRING NEW_LINE | START_LONG_COMMENT STRING END_LONG_COMMENT

list: OPEN_LIST_BRACKET 'STRING' | NUMBER (',' 'STRING' | NUMBER)* CLOSE_LIST_BRACKET

table : OPEN_LIST_BRACKET list* CLOSE_LIST_BRACKET

dictionary: DICT_OPEN_BRACKET (' VARIABLE ' : 'STRING' | INT | list)? (, 'VARIABLE' : 'STRING' | INT | list )* DICT_CLOSE_BRACKET

```


