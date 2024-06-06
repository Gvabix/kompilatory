# MGProgramming

## 1.Założenia programu
### Krótki opis
Program jest interpreterem dla języka programowania MGprogramming. Celem projektu jest pomoc mongolskim dzieciom w nauce nowego języka programowania bez konieczności znajomości języka angielskiego.
#### Ogólne cele programu
Interpretacja kodu: Program analizuje i wykonuje kod napisany w języku MGprogramming.
Obsługa macierzy: Program obsługuje operacje na macierzach i wyświetla wyniki obliczeń na konsoli.
GUI:Program umożliwia uruchamianie i testowanie kodu MGprogramming z linii poleceń oraz za pomocą interfejsu graficznego.
Rodzaj translatora: interpreter
Program jest interpreterem, co oznacza, że wykonuje kod bezpośrednio, bez generowania kodu maszynowego lub pośredniego.

## 2.Tokens:
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
## 3.Grammar:
```g4

program: codes* EOF;

codes: class_ | function_def | statement NEW_LINE?;

class_: CLASS_DEF VARIABLE START_CLASS class_body END_CLASS;

class_body: (function_def | declare)*;

function_def: FUNCT_DEF arg_types? VARIABLE OPEN_BRACKET args? CLOSE_BRACKET START_FUNCTION (statement)* (return)? END_FUNCTION;

args: arg_types VARIABLE (',' arg_types VARIABLE)*;

return: RETURN returners;

returners: TRUE | FALSE | VARIABLE | NUMBER | STRING_LITERAL;

statement: print 
    | if_statement 
    | for_loop 
    | while_loop 
    | assign 
    | declare 
    | function_call 
    | comment
    | NEW_LINE;

arg_types: INT | LONG | FLOAT | DOUBLE | CHAR | STRING | BOOLEAN | LIST | SET | DICT;

print: PRINT OPEN_BRACKET printers CLOSE_BRACKET;

printers: arithmetic_expr | bool_expr | VARIABLE | function_call | STRING_LITERAL;

if_statement: IF OPEN_BRACKET bool_expr CLOSE_BRACKET START_LOOP loop_body return? END_LOOP (else_statement)?;

else_statement: ELSE START_LOOP loop_body (return)? END_LOOP;

for_loop: FOR arg_types? VARIABLE for_statement START_LOOP loop_body END_LOOP;

for_statement: FOR_FROM arithmetic_expr FOR_TO arithmetic_expr FOR_JUMP arithmetic_expr
             | FOR_FROM arithmetic_expr FOR_TO arithmetic_expr
             | FOR_TO arithmetic_expr
             | FOR_TO arithmetic_expr FOR_JUMP arithmetic_expr;

while_loop: WHILE OPEN_BRACKET bool_expr CLOSE_BRACKET START_LOOP loop_body (return)? END_LOOP;

loop_body: (statement)*;

assign: VARIABLE ASSIGN_VALUE printers;

declare: arg_types VARIABLE | arg_types VARIABLE ASSIGN_VALUE printers;

variables: (VARIABLE | NUMBER | STRING_LITERAL) (',' (VARIABLE | NUMBER | STRING_LITERAL))*;

function_call: FUNCTION_CALL VARIABLE OPEN_BRACKET variables? CLOSE_BRACKET;

comment: COMMENT NEW_LINE | START_LONG_COMMENT;

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
                 | arithmetic_expr (PLUS | MINUS | MULTIPLY | DIVIDE | POWER | MODULO) arithmetic_expr;

array: OPEN_LIST_BRACKET (STRING_LITERAL | NUMBER) (',' (STRING_LITERAL | NUMBER))* CLOSE_LIST_BRACKET;

table: OPEN_LIST_BRACKET array* CLOSE_LIST_BRACKET;

dictionary: DICT_OPEN_BRACKET (VARIABLE ':' (STRING_LITERAL | NUMBER | array) (',' VARIABLE ':' (STRING_LITERAL | NUMBER | array))*)? DICT_CLOSE_BRACKET;


```
## 4. Informacja o stosowanych generatorach skanerów/parserów, pakietach zewnętrznych

Program korzysta z narzędzi ANTLR4 (ANother Tool for Language Recognition) do generowania skanerów i parserów na podstawie zdefiniowanej gramatyki. Dodatkowo, używane są pakiety zewnętrzne takie jak `antlr4-python3-runtime` do uruchamiania wygenerowanego kodu w języku Python oraz `tkinter` do stworzenia GUI.

### Generatory skanerów/parserów

**ANTLR (ANother Tool for Language Recognition)**:
- ANTLR jest narzędziem do generowania skanerów i parserów na podstawie zdefiniowanej gramatyki.
- Użycie ANTLR pozwala na automatyczne generowanie analizatora leksykalnego (skanera) oraz parsera dla języka MGprogramming.
- Plik gramatyki `MGprogramming.g4` jest używany przez ANTLR do wygenerowania kodu w Pythonie, który obsługuje analizę składniową.

### Pakiety zewnętrzne

**antlr4-python3-runtime**:
- Pakiet `antlr4-python3-runtime` zapewnia wsparcie uruchamiania wygenerowanych przez ANTLR skanerów i parserów w Pythonie.
- Instalacja: `pip install antlr4-python3-runtime`

**tkinter**:
- `tkinter` to standardowa biblioteka Pythona do tworzenia graficznych interfejsów użytkownika (GUI).
- Używana do stworzenia GUI dla interpretera, umożliwiając uruchamianie i testowanie kodu MGprogramming za pomocą interfejsu graficznego.

**Python**:
- Interpreter MGprogramming jest napisany w Pythonie, który jest wszechstronnym językiem programowania z szerokim wsparciem dla narzędzi do analizy składniowej i tworzenia aplikacji GUI.

## 5. Krótka instrukcja obsługi

1. **Instalacja zależności:**
   - Upewnij się, że masz zainstalowane Python oraz ANTLR4.
   - Zainstaluj wymagane pakiety Python: `pip install antlr4-python3-runtime`.

2. **Generowanie skanerów i parserów:**
   - Skorzystaj z ANTLR4, aby wygenerować skaner i parser na podstawie pliku gramatyki `MGprogramming.g4`:
     ```sh
     antlr4 -Dlanguage=Python3 MGprogramming.g4
     ```

3. **Uruchamianie programu:**
   - Napisz kod źródłowy w języku MGprogramming i zapisz go w pliku, np. `example.mg`.
   - Uruchom interpreter z GUI:
     ```sh
     python gui_interpreter.py
     ```
   - Możesz również uruchomić interpreter z linii poleceń:
     ```sh
     python interpreter.py example.mg
     ```

## 6. Przykład

Kod źródłowy w języku MGprogramming:

```plaintext
ner buhel main() ehleh
    buhel a todorhoiloh 3
    buhel b todorhoiloh 5
    buhel result todorhoiloh a + b
duusgah

zalgakh main


