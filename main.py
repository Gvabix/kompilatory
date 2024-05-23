import sys
from antlr4 import *
from tmp.MGprogrammingLexer import MGprogrammingLexer
from tmp.MGprogrammingParser import MGprogrammingParser
from tmp.MGprogrammingInterpreter import MGprogrammingInterpreter

# Define interpreter object globally
interpreter = MGprogrammingInterpreter()

def main(argv):
    if len(argv) < 2:
        print("Usage: python main.py <file.mgp>")
        return
    
    inputfile = argv[1]
    inputstream = FileStream(inputfile, encoding='utf-8')
    lexer = MGprogrammingLexer(inputstream)
    stream = CommonTokenStream(lexer)
    parser = MGprogrammingParser(stream)
    tree = parser.program()

    # Reset interpreter before each run
    # interpreter.reset()
    
    walker = ParseTreeWalker()
    walker.walk(interpreter, tree)

if __name__ == '__main__':
    main(sys.argv)
    # print("Output:", interpreter.output)
    interpreter.save_variables_to_file("output.txt")
