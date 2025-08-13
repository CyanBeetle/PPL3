# Generated from c:/Users/admin/Desktop/hlang-compiler/src/grammar/HLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HLangParser import HLangParser
else:
    from HLangParser import HLangParser

# This class defines a complete listener for a parse tree produced by HLangParser.
class HLangListener(ParseTreeListener):

    # Enter a parse tree produced by HLangParser#program.
    def enterProgram(self, ctx:HLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by HLangParser#program.
    def exitProgram(self, ctx:HLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by HLangParser#constDecl.
    def enterConstDecl(self, ctx:HLangParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by HLangParser#constDecl.
    def exitConstDecl(self, ctx:HLangParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by HLangParser#funcDecl.
    def enterFuncDecl(self, ctx:HLangParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by HLangParser#funcDecl.
    def exitFuncDecl(self, ctx:HLangParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by HLangParser#paramList.
    def enterParamList(self, ctx:HLangParser.ParamListContext):
        pass

    # Exit a parse tree produced by HLangParser#paramList.
    def exitParamList(self, ctx:HLangParser.ParamListContext):
        pass


    # Enter a parse tree produced by HLangParser#param.
    def enterParam(self, ctx:HLangParser.ParamContext):
        pass

    # Exit a parse tree produced by HLangParser#param.
    def exitParam(self, ctx:HLangParser.ParamContext):
        pass


    # Enter a parse tree produced by HLangParser#type.
    def enterType(self, ctx:HLangParser.TypeContext):
        pass

    # Exit a parse tree produced by HLangParser#type.
    def exitType(self, ctx:HLangParser.TypeContext):
        pass


    # Enter a parse tree produced by HLangParser#functionType.
    def enterFunctionType(self, ctx:HLangParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by HLangParser#functionType.
    def exitFunctionType(self, ctx:HLangParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by HLangParser#atomicType.
    def enterAtomicType(self, ctx:HLangParser.AtomicTypeContext):
        pass

    # Exit a parse tree produced by HLangParser#atomicType.
    def exitAtomicType(self, ctx:HLangParser.AtomicTypeContext):
        pass


    # Enter a parse tree produced by HLangParser#blockStmt.
    def enterBlockStmt(self, ctx:HLangParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by HLangParser#blockStmt.
    def exitBlockStmt(self, ctx:HLangParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by HLangParser#stmt.
    def enterStmt(self, ctx:HLangParser.StmtContext):
        pass

    # Exit a parse tree produced by HLangParser#stmt.
    def exitStmt(self, ctx:HLangParser.StmtContext):
        pass


    # Enter a parse tree produced by HLangParser#varDecl.
    def enterVarDecl(self, ctx:HLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by HLangParser#varDecl.
    def exitVarDecl(self, ctx:HLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by HLangParser#assignment.
    def enterAssignment(self, ctx:HLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by HLangParser#assignment.
    def exitAssignment(self, ctx:HLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by HLangParser#ifStmt.
    def enterIfStmt(self, ctx:HLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by HLangParser#ifStmt.
    def exitIfStmt(self, ctx:HLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by HLangParser#whileStmt.
    def enterWhileStmt(self, ctx:HLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by HLangParser#whileStmt.
    def exitWhileStmt(self, ctx:HLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by HLangParser#forStmt.
    def enterForStmt(self, ctx:HLangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by HLangParser#forStmt.
    def exitForStmt(self, ctx:HLangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by HLangParser#returnStmt.
    def enterReturnStmt(self, ctx:HLangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by HLangParser#returnStmt.
    def exitReturnStmt(self, ctx:HLangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by HLangParser#breakStmt.
    def enterBreakStmt(self, ctx:HLangParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by HLangParser#breakStmt.
    def exitBreakStmt(self, ctx:HLangParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by HLangParser#continueStmt.
    def enterContinueStmt(self, ctx:HLangParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by HLangParser#continueStmt.
    def exitContinueStmt(self, ctx:HLangParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by HLangParser#expressionStmt.
    def enterExpressionStmt(self, ctx:HLangParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by HLangParser#expressionStmt.
    def exitExpressionStmt(self, ctx:HLangParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by HLangParser#expression.
    def enterExpression(self, ctx:HLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by HLangParser#expression.
    def exitExpression(self, ctx:HLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by HLangParser#pipelineExpr.
    def enterPipelineExpr(self, ctx:HLangParser.PipelineExprContext):
        pass

    # Exit a parse tree produced by HLangParser#pipelineExpr.
    def exitPipelineExpr(self, ctx:HLangParser.PipelineExprContext):
        pass


    # Enter a parse tree produced by HLangParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:HLangParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by HLangParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:HLangParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by HLangParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:HLangParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by HLangParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:HLangParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by HLangParser#equalityExpr.
    def enterEqualityExpr(self, ctx:HLangParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by HLangParser#equalityExpr.
    def exitEqualityExpr(self, ctx:HLangParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by HLangParser#relationalExpr.
    def enterRelationalExpr(self, ctx:HLangParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by HLangParser#relationalExpr.
    def exitRelationalExpr(self, ctx:HLangParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by HLangParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:HLangParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by HLangParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:HLangParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by HLangParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:HLangParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by HLangParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:HLangParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by HLangParser#unaryExpr.
    def enterUnaryExpr(self, ctx:HLangParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by HLangParser#unaryExpr.
    def exitUnaryExpr(self, ctx:HLangParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by HLangParser#postfixExpr.
    def enterPostfixExpr(self, ctx:HLangParser.PostfixExprContext):
        pass

    # Exit a parse tree produced by HLangParser#postfixExpr.
    def exitPostfixExpr(self, ctx:HLangParser.PostfixExprContext):
        pass


    # Enter a parse tree produced by HLangParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:HLangParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by HLangParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:HLangParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by HLangParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:HLangParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by HLangParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:HLangParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by HLangParser#functionExpr.
    def enterFunctionExpr(self, ctx:HLangParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by HLangParser#functionExpr.
    def exitFunctionExpr(self, ctx:HLangParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by HLangParser#argList.
    def enterArgList(self, ctx:HLangParser.ArgListContext):
        pass

    # Exit a parse tree produced by HLangParser#argList.
    def exitArgList(self, ctx:HLangParser.ArgListContext):
        pass



del HLangParser