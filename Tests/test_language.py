import unittest
from antlr4 import *
from src.MGprogrammingLexer import MGprogrammingLexer
from src.MGprogrammingParser import MGprogrammingParser
from src.MGprogrammingInterpreter import MGprogrammingInterpreter

class TestMGprogramming(unittest.TestCase):

    def setUp(self):
        self.lexer = MGprogrammingLexer
        self.parser = MGprogrammingParser
        self.interpreter = MGprogrammingInterpreter()
        self.walker = ParseTreeWalker()

    def run_code(self, code):
        input_stream = InputStream(code)
        lexer = self.lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = self.parser(stream)
        tree = parser.program()
        self.walker.walk(self.interpreter, tree)

    def test_assignment_and_print(self):
        code = "buhel x todorhoiloh 10\nhevleh x\n"
        self.run_code(code)
        self.assertEqual(self.interpreter.variables['x'], 10)

    def test_variable_operations(self):
        code = (
            "buhel a todorhoiloh 5\n"
            "buhel b todorhoiloh 10\n"
            "buhel c todorhoiloh a + b\n"
            "hevleh c\n"
        )
        self.run_code(code)
        self.assertEqual(self.interpreter.variables['a'], 5)
        self.assertEqual(self.interpreter.variables['b'], 10)
        self.assertEqual(self.interpreter.variables['c'], 15)

    def test_if_statement(self):
        code = (
            "buhel x todorhoiloh 10\n"
            "hervee (x = 10) ehleh_davtalt\n"
            "  buhel y todorhoiloh 20\n"
            "  hevleh y\n"
            "duusgah_davtalt\n"
        )
        self.run_code(code)
        self.assertEqual(self.interpreter.variables['x'], 10)
        self.assertEqual(self.interpreter.variables['y'], 20)

    def test_for_loop(self):
        code = (
            "buhel sum todorhoiloh 0\n"
            "d i aas 1 tuld 5 nii tuld 1 ehleh_davtalt\n"
            "  sum todorhoiloh sum + i\n"
            "duusgah_davtalt\n"
            "hevleh sum\n"
        )
        self.run_code(code)
        self.assertEqual(self.interpreter.variables['sum'], 15)

    def test_while_loop(self):
        code = (
            "buhel x todorhoiloh 0\n"
            "zuur (x < 5) ehleh_davtalt\n"
            "  x todorhoiloh x + 1\n"
            "duusgah_davtalt\n"
            "hevleh x\n"
        )
        self.run_code(code)
        self.assertEqual(self.interpreter.variables['x'], 5)

if __name__ == '__main__':
    unittest.main()
