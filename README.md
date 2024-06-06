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
    hevleh(2 ^ 3)
    hevleh(3 ^ 2)
    hevleh(3 ^ 1)
    hevleh(11 ^ 0)
    hevleh(2 ^ 0)
    hevleh(4 ^ 4)

duusgah


zalgakh main()
```
```plaintext
ner buhel main() ehleh
    hevleh(5 > 3)
    hevleh(2 < 4)
    hevleh(5 >= 5)
    hevleh(4 <= 6)
    hevleh(7 = 7)
    hevleh(8 =/= 9)
    hevleh(3 < 5 bolon 5 > 2)
    hevleh(3 < 5 esvel 5 > 8)
    hevleh(!ünen)
duusgah
zalgakh main()
```
```plaintext
ex.1
hevleh(2+3)
buhel x todorhoiloh 2
buhel y todorhoiloh 3
buhel a todorhoiloh x+y
buhel b todorhoiloh x^y

hevleh(a)
hevleh(x)
hevleh(y)
hevleh(b)


```
```
buhel a todorhoiloh 1

zuur (a <= 8) ehleh_davtalt
hevleh("We can count till:") 
hevleh(a)

a todorhoiloh a+1 duusgah_davtalt
```
```
ner buhel arytmetyczne() ehleh
buhel x todorhoiloh 2
buhel z todorhoiloh 4
butarhai a todorhoiloh 2.3
butarhai b todorhoiloh 1.7

hevleh("Addition:")
hevleh(x+z)

hevleh("Multiplication:")
hevleh(a*b)
duusgah


zalgakh arytmetyczne()


hevleh(2^3)

buhel g
g todorhoiloh 3
hevleh(g)

```
```
ner buhel function() ehleh
buhel x todorhoiloh 2
butsah x
duusgah

hevleh(zalgakh function())
```
```
ner buhel main() ehleh
    buhel a todorhoiloh 5
    buhel b todorhoiloh 10
    butarhai c todorhoiloh 3.14
    mor message todorhoiloh "Hello, MGprogramming!"

    hevleh("Value of a: ")
    hevleh(a)

    hevleh("Value of b: ")
    hevleh(b)

    hevleh("Sum of a and b: ")
    hevleh(a + b)

    hevleh("Value of c: ")
    hevleh(c)

    hevleh("Message: ")
    hevleh(message)
duusgah

zalgakh main()

```
```
buhel x todorhoiloh 12
buhel c todorhoiloh 2^x
hervee (x <= 5) ehleh_davtalt
    hevleh("Our number is smaller than 5. Its is")
hevleh(x)
duusgah_davtalt

öör bol ( x>5 bolon x <= 10) ehleh_davtalt
    hevleh("hi")
duusgah_davtalt

mon ehleh_davtalt
    hevleh(c)
duusgah_davtalt

```
Przykład- parse tree

![image](https://github.com/Gvabix/kompilatory/assets/115698237/803616a6-e052-432f-8a3c-95874466b1f1)

## MGprogramming Хэлний Граммар
Програмын Ерөнхий Бүтэц
MGprogramming хэл нь программчлалын үндсэн элементүүдийг агуулсан бөгөөд доорх бүтэцтэй байна:

1. Програм: program нь олон codes-ийг агуулдаг.
2. Кодууд: codes нь анги, функцийн тодорхойлолт эсвэл үйлдлийн мөрийг илэрхийлнэ.
3. Анги: class_ нь ангийг тодорхойлдог бөгөөд ангид функцийн тодорхойлолт болон зарлал орно.
4. Функцийн Тодорхойлолт: function_def нь функцийн нэр, аргументүүд болон үйлдлийн мөрийг агуулна.
5. Үйлдэл: statement нь хэвлэх, нөхцөл шалгах, давталт хийх зэрэг үйлдлүүдийг илэрхийлнэ.

## Граммарын Дэлгэрэнгүй
# MGprogramming Interpreter

## 1. Төслийн тайлбар

### Товч танилцуулга
MGprogramming хэмээх программчлалын хэлний interpreter юм. Төслийн зорилго нь Монгол хүүхдүүдэд англи хэл мэдэхгүйгээр шинэ программчлалын хэл сурч, код бичих боломжийг олгох хэрэгсэл бүтээхэд оршино.

#### Программын ерөнхий зорилтууд
- **Кодын тайлал**: MGprogramming хэл дээр бичигдсэн кодыг тайлж, гүйцэтгэнэ.
- **Матрицын үйлдлүүд**: Матрицын үйлдлүүдийг гүйцэтгэж, үр дүнг консол болон график интерфейс дээр харуулна.
- **CLI болон GUI**: Программыг командын мөрөөс болон график интерфейсээр ашиглах боломжтой.
- **Интерпретерийн төрөл**: Interpreter – програм кодыг шууд гүйцэтгэдэг, машин эсвэл завсрын код үүсгэдэггүй.

#### Төлөвлөсөн үр дүн
MGprogramming хэлний интерпретер: Математик үйлдлүүд, давталтууд, нөхцөлүүд болон бусад хэлний бүтэцүүдийг гүйцэтгэж, үр дүнг консол болон GUI дээр харуулна.

#### Төлөвлөсөн програмчлалын хэл
Python: Программыг Python хэл дээр бичнэ. Энэ нь синтакс анализ хийх хэрэгслүүд болон CLI болон GUI хэрэгслүүдтэй хялбар интеграцлах боломжтой.

#### Сканер болон парсер үүсгэх арга
ANTLR: MGprogramming хэлний синтакс анализ хийхэд ANTLR хэрэгслийг ашиглана.

## 2. Спесификаци

### Токенууд
```plaintext
ASSIGN_VALUE: 'todorhoiloh'
PLUS: '+'
MINUS: '-'
MULTIPLY: '*'
DIVIDE: ':'
POWER: '^'
MODULO: '|'
GREATER_THAN: '>'
LESSER_THAN: '<'
GREATER_OR_EQUAL: '>='
LESSER_OR_EQUAL: '<='
EQUAL: '='
NOT_EQUAL: '=/='
NEW_LINE: '\n'
START_FUNCTION: 'ehleh'
END_FUNCTION: 'duusgah'
CLASS_DEF: 'angi'
START_CLASS: 'ehleh_angi'
END_CLASS: 'duusgah_angi'
START_LOOP: 'ehleh_davtalt'
END_LOOP: 'duusgah_davtalt'
WHILE: 'zuur'
CONTINUE: 'urgeljleh'
BREAK: 'zavsar'
FOR: 'd'
FOR_FROM: 'aas'
FOR_TO: 'tuld'
FOR_JUMP: 'nii tuld'
IF: 'hervee'
ELSE: 'mon'
FUNCT_DEF: 'ner'
RETURN: 'butsah'
PRINT: 'hevleh'
INPUT: 'orolt'
FUNCTION_CALL: 'zalgakh'

INT: 'buhel'
LONG: 'urt'
FLOAT: 'butarhai'
DOUBLE: 'ih_butarhai'
CHAR: 'temdegt'
STRING: 'mor'
BOOLEAN: 'tiim_ugui'
LIST: 'jagsaalt'
SET: 'bagts'
DICT: 'buleg'

AND: 'bolon'
OR: 'esvel'
TRUE: 'ünen'
FALSE: 'khudal'
NOT: '!'

Програм

program: codes* EOF;
program нь олон codes-ийг агуулдаг бөгөөд EOF нь файлын төгсгөл гэсэн үг юм.
Кодууд

a. codes: class_ | function_def | statement NEW_LINE?;
codes нь анги (class_), функцийн тодорхойлолт (function_def) эсвэл үйлдлийн мөр (statement) байж болно.
Анги

b. class_: CLASS_DEF VARIABLE START_CLASS class_body END_CLASS;
class_ нь ангийг тодорхойлдог. VARIABLE нь ангийн нэр, class_body нь ангид багтсан функцийн тодорхойлолт болон зарлалыг агуулдаг.
Функцийн Тодорхойлолт

c. function_def: FUNCT_DEF arg_types? VARIABLE OPEN_BRACKET args? CLOSE_BRACKET START_FUNCTION (statement)* (return)? END_FUNCTION;
function_def нь функцийн нэр, аргументүүд болон үйлдлийн мөрийг агуулна. arg_types нь аргументын төрлийг заана.
Аргументууд

d. args: arg_types VARIABLE (',' arg_types VARIABLE)*;
args нь олон аргумент агуулж болох бөгөөд тус бүрийн төрлийг arg_types тодорхойлно.
Үйлдэл


e. statement: print | if_statement | for_loop | while_loop | assign | declare | function_call | comment | NEW_LINE;
statement нь олон төрлийн үйлдэл байж болно: хэвлэх (print), нөхцөл шалгах (if_statement), давталт (for_loop, while_loop), хувьсагч зарлах (declare), функц дуудах (function_call), сэтгэгдэл бичих (comment) гэх мэт.
Хэвлэх


f. print: PRINT OPEN_BRACKET printers CLOSE_BRACKET;
print нь PRINT түлхүүр үгээр эхэлж, дотор нь хэвлэх утгыг (printers) агуулна.
Нөхцөл Шалгах

g. if_statement: IF OPEN_BRACKET bool_expr CLOSE_BRACKET START_LOOP loop_body return? END_LOOP (else_statement)?;
else_statement: ELSE START_LOOP loop_body (return)? END_LOOP;
if_statement нь нөхцөлийг шалгаж, үнэн тохиолдолд loop_body-г гүйцэтгэнэ. else_statement нь эсрэг тохиолдолд гүйцэтгэх үйлдлийг заана.
Давталтууд

h. for_loop: FOR arg_types? VARIABLE for_statement START_LOOP loop_body END_LOOP;
while_loop: WHILE OPEN_BRACKET bool_expr CLOSE_BRACKET START_LOOP loop_body (return)? END_LOOP;
for_loop нь тодорхой нөхцөлийг хангаж байх үед давталтыг гүйцэтгэнэ. while_loop нь тодорхой нөхцөлийг шалгаж, үнэн байвал loop_body-г давтана.
Хувьсагч Зарлах ба Оноох

i. assign: VARIABLE ASSIGN_VALUE printers;
declare: arg_types VARIABLE | arg_types VARIABLE ASSIGN_VALUE printers;
assign нь хувьсагчид утга оноох, declare нь хувьсагчийг зарлаж утга оноох үйлдлийг илэрхийлнэ.
Функц Дуудах

j. function_call: FUNCTION_CALL VARIABLE OPEN_BRACKET variables? CLOSE_BRACKET;
function_call нь функц дуудах үйлдлийг илэрхийлнэ. VARIABLE нь функцийн нэр, variables нь аргументуудыг заана.
**

```
## 4. Суулгах Заавар

1. **Хамааралтай пакет суулгах**:
   - Python болон ANTLR4 суулгасан эсэхээ шалгана уу.
   - Python пакет суулгах:
     ```sh
     pip install antlr4-python3-runtime
     ```

2. **Сканер болон парсер үүсгэх**:
   - ANTLR4 ашиглан сканер болон парсер үүсгэнэ үү:
     ```sh
     antlr4 -Dlanguage=Python3 MGprogramming.g4
     ```

3. **Програмыг ажиллуулах**:
   - MGprogramming хэл дээр код бичиж, жишээ нь `example.mg` файлд хадгална.
   - GUI ашиглан интерпретерийг ажиллуулах:
     ```sh
     python gui_interpreter.py
     ```
   - Командын мөрөөс интерпретерийг ажиллуулах:
     ```sh
     python interpreter.py example.mg
     ```
