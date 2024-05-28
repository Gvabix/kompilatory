from antlr4 import *
from MGprogrammingLexer import MGprogrammingLexer
from MGprogrammingParser import MGprogrammingParser

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def visit(self, node):
        method_name = 'visit' + type(node).__name__.replace('Context', '')
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        if hasattr(node, 'children'):
            for child in node.children:
                self.visit(child)

    def visitAssign(self, ctx):
        var_type = ctx.var_type().getText()
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.value())
        self.variables[var_name] = value
        return None

    def visitValue(self, ctx):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.STRING_LITERAL():
            return str(ctx.STRING_LITERAL().getText().strip('"'))
        elif ctx.VARIABLE():
            var_name = ctx.VARIABLE().getText()
            return self.variables.get(var_name, None)
        elif ctx.arithmeticExpression():
            return self.visit(ctx.arithmeticExpression())
        return None

    def visitArithmeticExpression(self, ctx):
        if ctx.PLUS():
            left = self.visit(ctx.arithmeticExpression(0))
            right = self.visit(ctx.arithmeticExpression(1))
            return left + right
        elif ctx.MINUS():
            left = self.visit(ctx.arithmeticExpression(0))
            right = self.visit(ctx.arithmeticExpression(1))
            return left - right
        elif ctx.MULTIPLY():
            left = self.visit(ctx.arithmeticExpression(0))
            right = self.visit(ctx.arithmeticExpression(1))
            return left * right
        elif ctx.DIVIDE():
            left = self.visit(ctx.arithmeticExpression(0))
            right = self.visit(ctx.arithmeticExpression(1))
            return left / right
        elif ctx.POWER():
            left = self.visit(ctx.arithmeticExpression(0))
            right = self.visit(ctx.arithmeticExpression(1))
            return left ** right
        elif ctx.MODULO():
            left = self.visit(ctx.arithmeticExpression(0))
            right = self.visit(ctx.arithmeticExpression(1))
            return left % right
        elif len(ctx.arithmeticExpression()) == 1:
            return self.visit(ctx.arithmeticExpression(0))
        elif ctx.VARIABLE():
            var_name = ctx.VARIABLE().getText()
            return self.variables.get(var_name, None)
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.OPEN_BRACKET():
            return self.visit(ctx.arithmeticExpression(0))
        return None

    def visitPrint(self, ctx):
        value = self.visit(ctx.value())
        print(value)
        return value

    def visitIf_stmt(self, ctx):
        condition = self.visit(ctx.condition())
        if condition:
            self.visit(ctx.loop_body())
        return None

    def visitCondition(self, ctx):
        left = self.variables.get(ctx.VARIABLE().getText(), None)
        right = self.visit(ctx.value())
        if ctx.EQUAL():
            return left == right
        elif ctx.GREATER_THAN():
            return left > right
        elif ctx.LESSER_THAN():
            return left < right
        elif ctx.GREATER_OR_EQUAL():
            return left >= right
        elif ctx.LESSER_OR_EQUAL():
            return left <= right
        elif ctx.NOT_EQUAL():
            return left != right
        return False

    def visitWhile_loop(self, ctx):
        while self.variables.get(ctx.VARIABLE().getText(), False):
            self.visit(ctx.loop_body())
        return None

    def visitFor_loop(self, ctx):
        var_name = ctx.VARIABLE().getText()
        start = int(ctx.NUMBER(0).getText())
        end = int(ctx.NUMBER(1).getText())
        step = int(ctx.NUMBER(2).getText())
        for i in range(start, end, step):
            self.variables[var_name] = i
            self.visit(ctx.loop_body())
        return None

    def visitFunction_def(self, ctx):
        func_name = ctx.VARIABLE().getText()
        self.functions[func_name] = ctx
        return None

    def visitFunction_call(self, ctx):
        func_name = ctx.VARIABLE().getText()
        func_def = self.functions.get(func_name)
        if func_def is not None:
            self.visit(func_def.function_body())
        return None

    def visitReturn_stmt(self, ctx):
        return self.visit(ctx.value())

    def visitProgram(self, ctx):
        for child in ctx.children:
            self.visit(child)
        return None

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = MGprogrammingLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MGprogrammingParser(stream)
    tree = parser.program()

    interpreter = Interpreter()
    interpreter.visit(tree)

if __name__ == "__main__":
    input_stream = FileStream("sample_program.mg")
    lexer = MGprogrammingLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MGprogrammingParser(token_stream)
    tree = parser.program()

    interpreter = Interpreter()
    interpreter.visit(tree)
