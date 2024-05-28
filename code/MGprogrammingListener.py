# Generated from MGprogramming.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MGprogrammingParser import MGprogrammingParser
else:
    from MGprogrammingParser import MGprogrammingParser

# This class defines a complete listener for a parse tree produced by MGprogrammingParser.
class MGprogrammingListener(ParseTreeListener):

    # Enter a parse tree produced by MGprogrammingParser#program.
    def enterProgram(self, ctx:MGprogrammingParser.ProgramContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#program.
    def exitProgram(self, ctx:MGprogrammingParser.ProgramContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#var_type.
    def enterVar_type(self, ctx:MGprogrammingParser.Var_typeContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#var_type.
    def exitVar_type(self, ctx:MGprogrammingParser.Var_typeContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#statement.
    def enterStatement(self, ctx:MGprogrammingParser.StatementContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#statement.
    def exitStatement(self, ctx:MGprogrammingParser.StatementContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#class_def.
    def enterClass_def(self, ctx:MGprogrammingParser.Class_defContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#class_def.
    def exitClass_def(self, ctx:MGprogrammingParser.Class_defContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#function_def.
    def enterFunction_def(self, ctx:MGprogrammingParser.Function_defContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#function_def.
    def exitFunction_def(self, ctx:MGprogrammingParser.Function_defContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#args.
    def enterArgs(self, ctx:MGprogrammingParser.ArgsContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#args.
    def exitArgs(self, ctx:MGprogrammingParser.ArgsContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#function_body.
    def enterFunction_body(self, ctx:MGprogrammingParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#function_body.
    def exitFunction_body(self, ctx:MGprogrammingParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#value.
    def enterValue(self, ctx:MGprogrammingParser.ValueContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#value.
    def exitValue(self, ctx:MGprogrammingParser.ValueContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#declaration.
    def enterDeclaration(self, ctx:MGprogrammingParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#declaration.
    def exitDeclaration(self, ctx:MGprogrammingParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#assign.
    def enterAssign(self, ctx:MGprogrammingParser.AssignContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#assign.
    def exitAssign(self, ctx:MGprogrammingParser.AssignContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#print.
    def enterPrint(self, ctx:MGprogrammingParser.PrintContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#print.
    def exitPrint(self, ctx:MGprogrammingParser.PrintContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#for_loop.
    def enterFor_loop(self, ctx:MGprogrammingParser.For_loopContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#for_loop.
    def exitFor_loop(self, ctx:MGprogrammingParser.For_loopContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#if_stmt.
    def enterIf_stmt(self, ctx:MGprogrammingParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#if_stmt.
    def exitIf_stmt(self, ctx:MGprogrammingParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#while_loop.
    def enterWhile_loop(self, ctx:MGprogrammingParser.While_loopContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#while_loop.
    def exitWhile_loop(self, ctx:MGprogrammingParser.While_loopContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#loop_body.
    def enterLoop_body(self, ctx:MGprogrammingParser.Loop_bodyContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#loop_body.
    def exitLoop_body(self, ctx:MGprogrammingParser.Loop_bodyContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#return_stmt.
    def enterReturn_stmt(self, ctx:MGprogrammingParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#return_stmt.
    def exitReturn_stmt(self, ctx:MGprogrammingParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#function_call.
    def enterFunction_call(self, ctx:MGprogrammingParser.Function_callContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#function_call.
    def exitFunction_call(self, ctx:MGprogrammingParser.Function_callContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#array.
    def enterArray(self, ctx:MGprogrammingParser.ArrayContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#array.
    def exitArray(self, ctx:MGprogrammingParser.ArrayContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#table.
    def enterTable(self, ctx:MGprogrammingParser.TableContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#table.
    def exitTable(self, ctx:MGprogrammingParser.TableContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#dictionary.
    def enterDictionary(self, ctx:MGprogrammingParser.DictionaryContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#dictionary.
    def exitDictionary(self, ctx:MGprogrammingParser.DictionaryContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:MGprogrammingParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:MGprogrammingParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#comment.
    def enterComment(self, ctx:MGprogrammingParser.CommentContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#comment.
    def exitComment(self, ctx:MGprogrammingParser.CommentContext):
        pass



del MGprogrammingParser