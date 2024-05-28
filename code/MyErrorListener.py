from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Syntax error at line {line}, column {column}: {msg}"
        self.errors.append(error_message)

    def semanticError(self, line, column, msg):
        error_message = f"Semantic error at line {line}, column {column}: {msg}"
        self.errors.append(error_message)

    def runtimeError(self, msg):
        error_message = f"Runtime error: {msg}"
        self.errors.append(error_message)

    def logicalError(self, msg):
        error_message = f"Logical error: {msg}"
        self.errors.append(error_message)

    def getErrors(self):
        return self.errors
