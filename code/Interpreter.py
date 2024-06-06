from antlr4 import *
from MGprogrammingLexer import MGprogrammingLexer
from MGprogrammingParser import MGprogrammingParser
from MGprogrammingVisitor import MGprogrammingVisitor


class Interpreter(MGprogrammingVisitor):
    def __init__(self):
        self.variables = {}
        self.loop_stack = []
        self.classes = {}
        self.functions = {}

    def visitProgram(self, ctx:MGprogrammingParser.ProgramContext):
        for code in ctx.codes():
            self.visit(code)

    def visitCodes(self, ctx:MGprogrammingParser.CodesContext):
        if ctx.class_():
            self.visit(ctx.class_())
        elif ctx.function_def():
            self.visit(ctx.function_def())
        elif ctx.statement():
            self.visit(ctx.statement())

    def visitClass_(self, ctx:MGprogrammingParser.Class_Context):
        class_name = ctx.VARIABLE().getText()
        self.classes[class_name] = {}
        self.visit(ctx.class_body())

    def visitClass_instance(self, ctx:MGprogrammingParser.Class_instanceContext):
        class_name = ctx.CLASS_INSTANCE().getText()
        instance_name = ctx.VARIABLE().getText()
        self.variables[instance_name] = self.classes[class_name]

    def visitClass_body(self, ctx:MGprogrammingParser.Class_bodyContext):
        for code in ctx.function_def():
            self.visit(code)
        for code in ctx.declare():
            self.visit(code)

    def visitFunction_def(self, ctx: MGprogrammingParser.Function_defContext):
        func_name = ctx.VARIABLE().getText()
        args = self.visit(ctx.args()) if ctx.args() else []
        statements = ctx.statement()
        return_stmt = ctx.return_stmt()
        self.variables[func_name] = {
            'args': args,
            'body': statements,
            'return': return_stmt  # Zapisz instrukcję return, jeśli istnieje
        }



    def visitArgs(self, ctx:MGprogrammingParser.ArgsContext):
        return [arg.getText() for arg in ctx.VARIABLE()]

    def visitReturn(self, ctx:MGprogrammingParser.ReturnersContext):
        if ctx.returners() is None:
            return None  # No return value, returning None
        return self.visitReturners(ctx.returners())

    def visitReturners(self, ctx: MGprogrammingParser.ReturnersContext):
        if ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False
        elif ctx.VARIABLE():
            var = self.variables.get(ctx.VARIABLE().getText())
            return var['value'] if var else None
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()
    
    def visitLoop_body(self, ctx:MGprogrammingParser.Loop_bodyContext):
        for statement in ctx.statement():
            self.visit(statement)

    def visitStatement(self, ctx:MGprogrammingParser.StatementContext):
        if ctx.print_():
            self.visit(ctx.print_())
        elif ctx.if_statement():
            self.visit(ctx.if_statement())
        elif ctx.for_loop():
            self.visit(ctx.for_loop())
        elif ctx.while_loop():
            self.visit(ctx.while_loop())
        elif ctx.assign():
            self.visit(ctx.assign())
        elif ctx.declare():
            self.visit(ctx.declare())
        elif ctx.function_call():
            self.visit(ctx.function_call())
        elif ctx.comment():
            self.visit(ctx.comment())

    def visitPrint(self, ctx:MGprogrammingParser.PrintContext):
        value = self.visit(ctx.printers())
        print(value)

    def visitPrinters(self, ctx:MGprogrammingParser.PrintersContext):
        if ctx.arithmetic_expr():
            return self.visit(ctx.arithmetic_expr())
        elif ctx.bool_expr():
            return self.visit(ctx.bool_expr())
        elif ctx.VARIABLE():
            return self.variables.get(ctx.VARIABLE().getText())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()

    def visitIf_statement(self, ctx:MGprogrammingParser.If_statementContext):
        if_condition = self.visit(ctx.bool_expr())
        if if_condition:
            self.visit(ctx.loop_body())
        else:
            # Sprawdź, czy są dostępne bloki else if
            for else_if_statement in ctx.else_if_statement():
                if_condition = self.visit(else_if_statement.bool_expr())
                if if_condition:
                    self.visit(else_if_statement.loop_body())
                    return  # Jeśli spełniono warunek, przerywamy dalsze sprawdzanie
            # Jeśli nie spełniono żadnego warunku, wykonujemy blok else, jeśli istnieje
            if ctx.else_statement():
                self.visit(ctx.else_statement().loop_body())

    def visitElse_if_statement(self, ctx:MGprogrammingParser.Else_if_statementContext):
        if_condition = self.visit(ctx.bool_expr())
        if if_condition:
            self.visit(ctx.loop_body())
    
    def visitElse_statement(self, ctx:MGprogrammingParser.Else_statementContext):
        self.visit(ctx.loop_body())

    def visitFor_statement(self, ctx: MGprogrammingParser.For_statementContext):
        start_value = self.visit(ctx.start) if ctx.start else None
        end_value = self.visit(ctx.end) if ctx.end else None
        step_value = self.visit(ctx.step) if ctx.step else 1
        return start_value, end_value, step_value

    def visitFor_loop(self, ctx: MGprogrammingParser.For_loopContext):
        start_value, end_value, step_value = self.visit(ctx.for_statement())
        variable_name = ctx.VARIABLE().getText()
    
        if start_value is None or end_value is None:
            return
    
        # Pętla for
        for i in range(start_value, end_value + 1, step_value):
            # Zaktualizuj wartość zmiennej pętli
            self.variables[variable_name] = {'type': 'int', 'value': i}
    
            # Wykonaj ciało pętli
            self.visit(ctx.loop_body())



    def visitWhile_loop(self, ctx:MGprogrammingParser.While_loopContext):
        iteration_limit = 10000  # Limit iteracji
        iteration_count = 0
        while self.visit(ctx.bool_expr()):
            if iteration_count >= iteration_limit:
                print("Przekroczono limit iteracji pętli while.")
                break
            self.visit(ctx.loop_body())
            iteration_count += 1
    
            # Wyświetlanie wartości zmiennej x
            x_value = self.variables.get('x')
            if x_value:
                print(f"x = {x_value['value']}")


    def visitDeclare(self, ctx:MGprogrammingParser.DeclareContext):
        var_type = ctx.arg_types().getText()
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.printers()) if ctx.ASSIGN_VALUE() else None
        self.variables[var_name] = {'type': var_type, 'value': value}


    def visitAssign(self, ctx:MGprogrammingParser.AssignContext):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.printers())
        self.variables[var_name] = {'type': 'int', 'value': value}

    def visitFunction_call(self, ctx: MGprogrammingParser.Function_callContext):
        func_name = ctx.VARIABLE().getText()
        args = self.visit(ctx.variables()) if ctx.variables() else []
    
        # Wywołaj funkcję i przekaż jej argumenty
        return self.call_function(func_name, args)
    
    def call_function(self, func_name, args):
        func_def = self.variables.get(func_name)
        if not func_def:
            raise Exception(f"Function {func_name} not found")
    
        # Ustaw argumenty w lokalnym zakresie
        local_vars = dict(zip(func_def['args'], args))
        self.variables.update(local_vars)
    
        # Wykonaj ciało funkcji
        for statement in func_def['body']:
            self.visit(statement)
    
        # Sprawdź, czy jest instrukcja return
        if func_def['return']:
            return_value = self.visit(func_def['return'].returners())
            return return_value
        else:
            # Jeśli nie ma instrukcji return, zwróć None
            return None




    def visitVariables(self, ctx: MGprogrammingParser.VariablesContext):
        return [self.visit(var) for var in ctx.VARIABLE()]

    def visitBool_expr(self, ctx:MGprogrammingParser.Bool_exprContext):
        if ctx.AND() or ctx.OR():
            left = self.visit(ctx.bool_expr(0))
            right = self.visit(ctx.bool_expr(1))
            if ctx.AND():
                return left and right
            elif ctx.OR():
                return left or right
        elif ctx.GREATER_THAN() or ctx.LESSER_THAN() or ctx.GREATER_OR_EQUAL() or ctx.LESSER_OR_EQUAL() or ctx.EQUAL() or ctx.NOT_EQUAL():
            left = self.visit(ctx.arithmetic_expr(0))
            right = self.visit(ctx.arithmetic_expr(1))
            if ctx.GREATER_THAN():
                return left > right
            elif ctx.LESSER_THAN():
                return left < right
            elif ctx.GREATER_OR_EQUAL():
                return left >= right
            elif ctx.LESSER_OR_EQUAL():
                return left <= right
            elif ctx.EQUAL():
                return left == right
            elif ctx.NOT_EQUAL():
                return left != right
        elif ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False
        elif ctx.VARIABLE():
            return self.variables.get(ctx.VARIABLE().getText())
        elif ctx.NOT():
            return not self.visit(ctx.bool_expr(0))
        elif ctx.OPEN_BRACKET():
            return self.visit(ctx.bool_expr(0))

    def visitArithmetic_expr(self, ctx:MGprogrammingParser.Arithmetic_exprContext):
        if ctx.VARIABLE():
            return self.variables.get(ctx.VARIABLE().getText())['value']
        elif ctx.NUMBER():
            return self.parse_number(ctx.NUMBER().getText())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.OPEN_BRACKET():
            return self.visit(ctx.arithmetic_expr(0))
        else:
            left = self.visit(ctx.arithmetic_expr(0))
            right = self.visit(ctx.arithmetic_expr(1))
            if ctx.PLUS():
                return left + right
            elif ctx.MINUS():
                return left - right
            elif ctx.MULTIPLY():
                return left * right
            elif ctx.DIVIDE():
                return left / right
            elif ctx.POWER():
                return left ** right
            elif ctx.MODULO():
                return left % right

    def parse_number(self, text):
        if '.' in text:
            return float(text) if 'f' in text or 'F' in text else float(text)
        elif 'L' in text or 'l' in text:
            return int(text[:-1])  # Handle long integers
        else:
            return int(text)

    def visitComment(self, ctx:MGprogrammingParser.CommentContext):
        pass  # Ignore comments

    def visitArray(self, ctx: MGprogrammingParser.ArrayContext):
        elements = [self.visit(element) for element in ctx.STRING_LITERAL() or ctx.NUMBER()]
        return elements

    def visitTable(self, ctx: MGprogrammingParser.TableContext):
        arrays = [self.visit(array) for array in ctx.array()]
        return arrays

    def visitDictionary(self, ctx: MGprogrammingParser.DictionaryContext):
        dictionary = {}
        for pair in ctx.VARIABLE():
            key = pair.VARIABLE().getText()
            value = self.visit(pair.STRING_LITERAL() or pair.NUMBER() or pair.array())
            dictionary[key] = value
        return dictionary



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
 
