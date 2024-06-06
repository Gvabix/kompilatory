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


    # Enter a parse tree produced by MGprogrammingParser#codes.
    def enterCodes(self, ctx:MGprogrammingParser.CodesContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#codes.
    def exitCodes(self, ctx:MGprogrammingParser.CodesContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#class_.
    def enterClass_(self, ctx:MGprogrammingParser.Class_Context):
        pass

    # Exit a parse tree produced by MGprogrammingParser#class_.
    def exitClass_(self, ctx:MGprogrammingParser.Class_Context):
        pass


    # Enter a parse tree produced by MGprogrammingParser#class_instance.
    def enterClass_instance(self, ctx:MGprogrammingParser.Class_instanceContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#class_instance.
    def exitClass_instance(self, ctx:MGprogrammingParser.Class_instanceContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#class_body.
    def enterClass_body(self, ctx:MGprogrammingParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#class_body.
    def exitClass_body(self, ctx:MGprogrammingParser.Class_bodyContext):
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


    # Enter a parse tree produced by MGprogrammingParser#return_stmt.
    def enterReturn_stmt(self, ctx:MGprogrammingParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#return_stmt.
    def exitReturn_stmt(self, ctx:MGprogrammingParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#returners.
    def enterReturners(self, ctx:MGprogrammingParser.ReturnersContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#returners.
    def exitReturners(self, ctx:MGprogrammingParser.ReturnersContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#statement.
    def enterStatement(self, ctx:MGprogrammingParser.StatementContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#statement.
    def exitStatement(self, ctx:MGprogrammingParser.StatementContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#arg_types.
    def enterArg_types(self, ctx:MGprogrammingParser.Arg_typesContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#arg_types.
    def exitArg_types(self, ctx:MGprogrammingParser.Arg_typesContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#print.
    def enterPrint(self, ctx:MGprogrammingParser.PrintContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#print.
    def exitPrint(self, ctx:MGprogrammingParser.PrintContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#printers.
    def enterPrinters(self, ctx:MGprogrammingParser.PrintersContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#printers.
    def exitPrinters(self, ctx:MGprogrammingParser.PrintersContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#if_statement.
    def enterIf_statement(self, ctx:MGprogrammingParser.If_statementContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#if_statement.
    def exitIf_statement(self, ctx:MGprogrammingParser.If_statementContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#else_if_statement.
    def enterElse_if_statement(self, ctx:MGprogrammingParser.Else_if_statementContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#else_if_statement.
    def exitElse_if_statement(self, ctx:MGprogrammingParser.Else_if_statementContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#else_statement.
    def enterElse_statement(self, ctx:MGprogrammingParser.Else_statementContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#else_statement.
    def exitElse_statement(self, ctx:MGprogrammingParser.Else_statementContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#for_loop.
    def enterFor_loop(self, ctx:MGprogrammingParser.For_loopContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#for_loop.
    def exitFor_loop(self, ctx:MGprogrammingParser.For_loopContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#for_statement.
    def enterFor_statement(self, ctx:MGprogrammingParser.For_statementContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#for_statement.
    def exitFor_statement(self, ctx:MGprogrammingParser.For_statementContext):
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


    # Enter a parse tree produced by MGprogrammingParser#assign.
    def enterAssign(self, ctx:MGprogrammingParser.AssignContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#assign.
    def exitAssign(self, ctx:MGprogrammingParser.AssignContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#declare.
    def enterDeclare(self, ctx:MGprogrammingParser.DeclareContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#declare.
    def exitDeclare(self, ctx:MGprogrammingParser.DeclareContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#variables.
    def enterVariables(self, ctx:MGprogrammingParser.VariablesContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#variables.
    def exitVariables(self, ctx:MGprogrammingParser.VariablesContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#function_call.
    def enterFunction_call(self, ctx:MGprogrammingParser.Function_callContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#function_call.
    def exitFunction_call(self, ctx:MGprogrammingParser.Function_callContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#comment.
    def enterComment(self, ctx:MGprogrammingParser.CommentContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#comment.
    def exitComment(self, ctx:MGprogrammingParser.CommentContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#bool_expr.
    def enterBool_expr(self, ctx:MGprogrammingParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#bool_expr.
    def exitBool_expr(self, ctx:MGprogrammingParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by MGprogrammingParser#arithmetic_expr.
    def enterArithmetic_expr(self, ctx:MGprogrammingParser.Arithmetic_exprContext):
        pass

    # Exit a parse tree produced by MGprogrammingParser#arithmetic_expr.
    def exitArithmetic_expr(self, ctx:MGprogrammingParser.Arithmetic_exprContext):
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



del MGprogrammingParser
