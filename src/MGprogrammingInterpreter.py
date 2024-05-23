from MGprogrammingListener import MGprogrammingListener
from MGprogrammingParser import MGprogrammingParser

class MGprogrammingInterpreter(MGprogrammingListener):
    def __init__(self):
        self.variables = {}

    def exitAssign(self, ctx: MGprogrammingParser.AssignContext):
        var_type = ctx.VAR_TYPE().getText()
        var_name = ctx.VARIABLE().getText()
        value = ctx.NUMBER().getText() if ctx.NUMBER() else ctx.VARIABLE().getText()

        parsed_value = self.parse_value(var_type, value)
        self.variables[var_name] = parsed_value

    def exitPrint(self, ctx: MGprogrammingParser.PrintContext):
        var_name = ctx.VARIABLE().getText()
        if var_name in self.variables:
            print(self.variables[var_name])
        else:
            print(f"Variable {var_name} not found.")

    def parse_value(self, var_type, value):
        if var_type == "buhel":
            return int(value)
        elif var_type == "urt":
            return int(value)
        elif var_type == "butarhai":
            return float(value)
        elif var_type == "ih_butarhai":
            return float(value)
        elif var_type == "temdegt":
            return value[0]
        elif var_type == "mor":
            return value
        elif var_type == "tiim_ugui":
            return value.lower() == "true"
        return value
