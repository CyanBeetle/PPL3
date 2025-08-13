"""
AST Generation module for HLang programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.HLangVisitor import HLangVisitor
from build.HLangParser import HLangParser
from src.utils.nodes import *


class ASTGeneration(HLangVisitor):
    """
    AST Generation visitor that converts ANTLR parse trees into HLang AST nodes.
    This class inherits from HLangVisitor and overrides visit methods to create
    appropriate AST node objects from parse tree contexts.
    """

    def visitProgram(self, ctx):
        """Visit program rule: (constDecl | funcDecl)* EOF"""
        const_decls = []
        func_decls = []
        
        for child in ctx.children:
            if hasattr(child, 'getRuleIndex'):
                if isinstance(child, HLangParser.ConstDeclContext):
                    const_decls.append(self.visit(child))
                elif isinstance(child, HLangParser.FuncDeclContext):
                    func_decls.append(self.visit(child))
        
        return Program(const_decls, func_decls)

    def visitConstDecl(self, ctx):
        """Visit constDecl rule: CONST ID (COLON type)? ASSIGN expression SEMICOLON"""
        name = ctx.ID().getText()
        type_annotation = None
        if ctx.type_():
            type_annotation = self.visit(ctx.type_())
        value = self.visit(ctx.expression())
        
        return ConstDecl(name, type_annotation, value)

    def visitFuncDecl(self, ctx):
        """Visit funcDecl rule: FUNC ID LPAREN paramList? RPAREN ARROW type blockStmt"""
        name = ctx.ID().getText()
        params = []
        if ctx.paramList():
            params = self.visit(ctx.paramList())
        return_type = self.visit(ctx.type_())
        block_stmt = self.visit(ctx.blockStmt())
        
        # Extract statements from BlockStmt for FuncDecl body
        body = block_stmt.statements if isinstance(block_stmt, BlockStmt) else []
        
        return FuncDecl(name, params, return_type, body)

    def visitParamList(self, ctx):
        """Visit paramList rule: param (COMMA param)*"""
        params = []
        for param_ctx in ctx.param():
            params.append(self.visit(param_ctx))
        return params

    def visitParam(self, ctx):
        """Visit param rule: ID COLON type"""
        name = ctx.ID().getText()
        param_type = self.visit(ctx.type_())
        return Param(name, param_type)

    def visitType(self, ctx):
        """Visit type rule: functionType"""
        return self.visit(ctx.functionType())

    def visitFunctionType(self, ctx):
        """Visit functionType rule: atomicType (ARROW functionType)?"""
        # For now, we just handle the simple case - atomic types
        # Function types would need additional node types to handle properly
        return self.visit(ctx.atomicType())

    def visitAtomicType(self, ctx):
        """Visit atomicType rule: various type options"""
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.LBRACKET() and ctx.SEMICOLON():  # Array type [type; size]
            element_type = self.visit(ctx.type_(0))  # First type child
            size = int(ctx.INTLITERAL().getText())
            return ArrayType(element_type, size)
        elif ctx.LBRACKET() and not ctx.SEMICOLON():  # Dynamic array [type]
            element_type = self.visit(ctx.type_(0))
            return ArrayType(element_type, 0)  # Use 0 to indicate dynamic
        elif ctx.LPAREN() and ctx.ARROW():  # Function type
            # For function types, we'll return a placeholder for now
            # since the nodes.py doesn't have a specific function type node
            return VoidType()  # Placeholder
        elif ctx.LPAREN() and not ctx.ARROW():  # Parenthesized type
            return self.visit(ctx.type_(0))
        
        return None

    def visitBlockStmt(self, ctx):
        """Visit blockStmt rule: LBRACE stmt* RBRACE"""
        statements = []
        for stmt_ctx in ctx.stmt():
            statements.append(self.visit(stmt_ctx))
        return BlockStmt(statements)

    def visitStmt(self, ctx):
        """Visit stmt rule: various statement types"""
        # Dispatch to appropriate statement visitor
        for child in ctx.children:
            if hasattr(child, 'getRuleIndex'):
                return self.visit(child)
        return None

    def visitVarDecl(self, ctx):
        """Visit varDecl rule: LET ID (COLON type)? ASSIGN expression SEMICOLON"""
        name = ctx.ID().getText()
        type_annotation = None
        if ctx.type_():
            type_annotation = self.visit(ctx.type_())
        value = self.visit(ctx.expression())
        
        return VarDecl(name, type_annotation, value)

    def visitAssignment(self, ctx):
        """Visit assignment rule: ID (LBRACKET expression RBRACKET)* ASSIGN expression SEMICOLON"""
        # Create appropriate LValue based on whether there are array accesses
        base_name = ctx.ID().getText()
        
        if len(ctx.expression()) == 1:  # Simple assignment: ID = expr
            lvalue = IdLValue(base_name)
            value = self.visit(ctx.expression(0))
        else:  # Array assignment: ID[expr] = expr
            # Build nested array accesses
            array_expr = Identifier(base_name)
            for i in range(len(ctx.expression()) - 1):  # All but the last expression are indices
                index_expr = self.visit(ctx.expression(i))
                array_expr = ArrayAccess(array_expr, index_expr)
            
            lvalue = ArrayAccessLValue(array_expr.array if isinstance(array_expr, ArrayAccess) else Identifier(base_name), 
                                     array_expr.index if isinstance(array_expr, ArrayAccess) else self.visit(ctx.expression(0)))
            value = self.visit(ctx.expression()[-1])  # Last expression is the value
        
        return Assignment(lvalue, value)

    def visitIfStmt(self, ctx):
        """Visit ifStmt rule: IF LPAREN expression RPAREN blockStmt (ELSE IF LPAREN expression RPAREN blockStmt)* (ELSE blockStmt)?"""
        condition = self.visit(ctx.expression(0))
        then_stmt = self.visit(ctx.blockStmt(0))
        
        elif_branches = []
        else_stmt = None
        
        # Handle elif branches
        expr_count = len(ctx.expression())
        block_count = len(ctx.blockStmt())
        
        if expr_count > 1:  # Has elif branches
            for i in range(1, expr_count):
                elif_condition = self.visit(ctx.expression(i))
                elif_block = self.visit(ctx.blockStmt(i))
                elif_branches.append((elif_condition, elif_block))
        
        # Handle else branch
        if block_count > expr_count:  # More blocks than expressions means there's an else
            else_stmt = self.visit(ctx.blockStmt(block_count - 1))  # Last block is else
        
        return IfStmt(condition, then_stmt, elif_branches, else_stmt)

    def visitWhileStmt(self, ctx):
        """Visit whileStmt rule: WHILE LPAREN expression RPAREN blockStmt"""
        condition = self.visit(ctx.expression())
        body = self.visit(ctx.blockStmt())
        
        return WhileStmt(condition, body)

    def visitForStmt(self, ctx):
        """Visit forStmt rule: FOR LPAREN ID IN expression RPAREN blockStmt"""
        variable = ctx.ID().getText()
        iterable = self.visit(ctx.expression())
        body = self.visit(ctx.blockStmt())
        
        return ForStmt(variable, iterable, body)

    def visitReturnStmt(self, ctx):
        """Visit returnStmt rule: RETURN expression? SEMICOLON"""
        value = None
        if ctx.expression():
            value = self.visit(ctx.expression())
        
        return ReturnStmt(value)

    def visitBreakStmt(self, ctx):
        """Visit breakStmt rule: BREAK SEMICOLON"""
        return BreakStmt()

    def visitContinueStmt(self, ctx):
        """Visit continueStmt rule: CONTINUE SEMICOLON"""
        return ContinueStmt()

    def visitExpressionStmt(self, ctx):
        """Visit expressionStmt rule: expression SEMICOLON"""
        expr = self.visit(ctx.expression())
        return ExprStmt(expr)

    def visitExpression(self, ctx):
        """Visit expression rule: pipelineExpr"""
        return self.visit(ctx.pipelineExpr())

    def visitPipelineExpr(self, ctx):
        """Visit pipelineExpr rule: logicalOrExpr (PIPELINE logicalOrExpr)*"""
        if len(ctx.logicalOrExpr()) == 1:
            return self.visit(ctx.logicalOrExpr(0))
        
        # Build left-associative pipeline operations
        result = self.visit(ctx.logicalOrExpr(0))
        for i in range(1, len(ctx.logicalOrExpr())):
            right = self.visit(ctx.logicalOrExpr(i))
            result = BinaryOp(result, '>>', right)
        
        return result

    def visitLogicalOrExpr(self, ctx):
        """Visit logicalOrExpr rule: logicalAndExpr (OR logicalAndExpr)*"""
        if len(ctx.logicalAndExpr()) == 1:
            return self.visit(ctx.logicalAndExpr(0))
        
        # Build left-associative OR operations
        result = self.visit(ctx.logicalAndExpr(0))
        for i in range(1, len(ctx.logicalAndExpr())):
            right = self.visit(ctx.logicalAndExpr(i))
            result = BinaryOp(result, '||', right)
        
        return result

    def visitLogicalAndExpr(self, ctx):
        """Visit logicalAndExpr rule: equalityExpr (AND equalityExpr)*"""
        if len(ctx.equalityExpr()) == 1:
            return self.visit(ctx.equalityExpr(0))
        
        # Build left-associative AND operations
        result = self.visit(ctx.equalityExpr(0))
        for i in range(1, len(ctx.equalityExpr())):
            right = self.visit(ctx.equalityExpr(i))
            result = BinaryOp(result, '&&', right)
        
        return result

    def visitEqualityExpr(self, ctx):
        """Visit equalityExpr rule: relationalExpr ((EQ | NE) relationalExpr)*"""
        if len(ctx.relationalExpr()) == 1:
            return self.visit(ctx.relationalExpr(0))
        
        # Build left-associative equality operations
        result = self.visit(ctx.relationalExpr(0))
        for i in range(1, len(ctx.relationalExpr())):
            # Get the operator token
            operator = '==' if ctx.EQ(i-1) else '!='
            right = self.visit(ctx.relationalExpr(i))
            result = BinaryOp(result, operator, right)
        
        return result

    def visitRelationalExpr(self, ctx):
        """Visit relationalExpr rule: additiveExpr ((LT | LE | GT | GE) additiveExpr)*"""
        if len(ctx.additiveExpr()) == 1:
            return self.visit(ctx.additiveExpr(0))
        
        # Build left-associative relational operations
        result = self.visit(ctx.additiveExpr(0))
        for i in range(1, len(ctx.additiveExpr())):
            # Determine operator
            if ctx.LT(i-1):
                operator = '<'
            elif ctx.LE(i-1):
                operator = '<='
            elif ctx.GT(i-1):
                operator = '>'
            else:  # GE
                operator = '>='
            
            right = self.visit(ctx.additiveExpr(i))
            result = BinaryOp(result, operator, right)
        
        return result

    def visitAdditiveExpr(self, ctx):
        """Visit additiveExpr rule: multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*"""
        if len(ctx.multiplicativeExpr()) == 1:
            return self.visit(ctx.multiplicativeExpr(0))
        
        # Build left-associative additive operations
        result = self.visit(ctx.multiplicativeExpr(0))
        for i in range(1, len(ctx.multiplicativeExpr())):
            operator = '+' if ctx.PLUS(i-1) else '-'
            right = self.visit(ctx.multiplicativeExpr(i))
            result = BinaryOp(result, operator, right)
        
        return result

    def visitMultiplicativeExpr(self, ctx):
        """Visit multiplicativeExpr rule: unaryExpr ((MULT | DIV | MOD) unaryExpr)*"""
        if len(ctx.unaryExpr()) == 1:
            return self.visit(ctx.unaryExpr(0))
        
        # Build left-associative multiplicative operations
        result = self.visit(ctx.unaryExpr(0))
        for i in range(1, len(ctx.unaryExpr())):
            if ctx.MULT(i-1):
                operator = '*'
            elif ctx.DIV(i-1):
                operator = '/'
            else:  # MOD
                operator = '%'
            
            right = self.visit(ctx.unaryExpr(i))
            result = BinaryOp(result, operator, right)
        
        return result

    def visitUnaryExpr(self, ctx):
        """Visit unaryExpr rule: (MINUS | PLUS | NOT) unaryExpr | postfixExpr"""
        if ctx.MINUS() or ctx.PLUS() or ctx.NOT():
            if ctx.MINUS():
                operator = '-'
            elif ctx.PLUS():
                operator = '+'
            else:  # NOT
                operator = '!'
            
            operand = self.visit(ctx.unaryExpr())
            return UnaryOp(operator, operand)
        else:
            return self.visit(ctx.postfixExpr())

    def visitPostfixExpr(self, ctx):
        """Visit postfixExpr rule: primaryExpr (LBRACKET expression RBRACKET | LPAREN argList? RPAREN)*"""
        result = self.visit(ctx.primaryExpr())
        
        # Process postfix operations (array access and function calls)
        expr_index = 0
        
        # Look for actual brackets and parentheses in children
        i = 1  # Skip primaryExpr
        while i < len(ctx.children):
            child = ctx.children[i]
            if hasattr(child, 'symbol') and child.symbol:
                if child.symbol.text == '[':  # Array access
                    if expr_index < len(ctx.expression()):
                        index = self.visit(ctx.expression(expr_index))
                        result = ArrayAccess(result, index)
                        expr_index += 1
                elif child.symbol.text == '(':  # Function call
                    args = []
                    # Check if there's an argList - should only be one
                    if ctx.argList():
                        args = self.visit(ctx.argList(0))  # Get the first (and only) argList
                    result = FunctionCall(result, args)
            i += 1
        
        return result

    def visitPrimaryExpr(self, ctx):
        """Visit primaryExpr rule: literals, identifiers, parenthesized expressions"""
        if ctx.INTLITERAL():
            return IntegerLiteral(int(ctx.INTLITERAL().getText()))
        elif ctx.FLOATLITERAL():
            return FloatLiteral(float(ctx.FLOATLITERAL().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.STRINGLITERAL():
            # The lexer already removes quotes, so we can use the text directly
            return StringLiteral(ctx.STRINGLITERAL().getText())
        elif ctx.arrayLiteral():
            return self.visit(ctx.arrayLiteral())
        elif ctx.functionExpr():
            return self.visit(ctx.functionExpr())
        elif ctx.ID():
            return Identifier(ctx.ID().getText())
        elif ctx.expression():  # Parenthesized expression
            return self.visit(ctx.expression())
        
        return None

    def visitArrayLiteral(self, ctx):
        """Visit arrayLiteral rule: LBRACKET (expression (COMMA expression)*)? RBRACKET"""
        elements = []
        for expr_ctx in ctx.expression():
            elements.append(self.visit(expr_ctx))
        
        return ArrayLiteral(elements)

    def visitFunctionExpr(self, ctx):
        """Visit functionExpr rule: FUNC LPAREN paramList? RPAREN ARROW type blockStmt"""
        # Function expressions are lambda functions - create an anonymous function
        params = []
        if ctx.paramList():
            params = self.visit(ctx.paramList())
        return_type = self.visit(ctx.type_())
        block_stmt = self.visit(ctx.blockStmt())
        
        # Extract statements from BlockStmt for function body
        body = block_stmt.statements if isinstance(block_stmt, BlockStmt) else []
        
        # Use an empty name for lambda functions
        return FuncDecl("", params, return_type, body)

    def visitArgList(self, ctx):
        """Visit argList rule: expression (COMMA expression)*"""
        args = []
        for expr_ctx in ctx.expression():
            args.append(self.visit(expr_ctx))
        
        return args