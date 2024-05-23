import sys
from antlr4 import *
from src.MGprogrammingLexer import MGprogrammingLexer
from src.MGprogrammingParser import MGprogrammingParser
from src.MGprogrammingInterpreter import MGprogrammingInterpreter

def main():
    if len(sys.argv) != 2:
        print("Usage: mgp_cli.py <file.mgp>")
        sys.exit(1)

    file_name = sys.argv[1]
    input_stream = FileStream(file_name, encoding='utf-8')
    lexer = MGprogrammingLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MGprogrammingParser(stream)
    tree = parser.program()

    interpreter = MGprogrammingInterpreter()
    walker = ParseTreeWalker()
    walker.walk(interpreter, tree)

if __name__ == '__main__':
    main()
