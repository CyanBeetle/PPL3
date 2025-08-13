grammar HLang;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_TOKEN:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// ============================================================================
// PARSER RULES
// ============================================================================

program: (constDecl | funcDecl)* EOF;

// Constant declarations
constDecl: CONST ID (COLON type)? ASSIGN expression SEMICOLON;

// Function declarations  
funcDecl: FUNC ID LPAREN paramList? RPAREN ARROW type blockStmt;

// Parameter list
paramList: param (COMMA param)*;
param: ID COLON type;

// Type annotations with precedence (lowest to highest)
type: functionType;

functionType: atomicType (ARROW functionType)?;  // Right-associative function type

atomicType: INT | FLOAT | BOOL | STRING | VOID
    | LBRACKET type SEMICOLON INTLITERAL RBRACKET  // Fixed-size array type [type; size]
    | LBRACKET type RBRACKET  // Dynamic array type [type]
    | LPAREN (type (COMMA type)*)? RPAREN ARROW type  // Parenthesized function type (param_types...) -> return_type
    | LPAREN type RPAREN  // Parenthesized type
 ;

// Statements
blockStmt: LBRACE stmt* RBRACE;

stmt: varDecl | assignment | ifStmt | whileStmt | forStmt | returnStmt | breakStmt | continueStmt | blockStmt | expressionStmt;

varDecl: LET ID (COLON type)? ASSIGN expression SEMICOLON;
assignment: ID (LBRACKET expression RBRACKET)* ASSIGN expression SEMICOLON;
ifStmt: IF LPAREN expression RPAREN blockStmt (ELSE IF LPAREN expression RPAREN blockStmt)* (ELSE blockStmt)?;
whileStmt: WHILE LPAREN expression RPAREN blockStmt;
forStmt: FOR LPAREN ID IN expression RPAREN blockStmt;
returnStmt: RETURN expression? SEMICOLON;
breakStmt: BREAK SEMICOLON;
continueStmt: CONTINUE SEMICOLON;
expressionStmt: expression SEMICOLON;

// Expressions with precedence (lowest to highest)
expression: pipelineExpr;

pipelineExpr: logicalOrExpr (PIPELINE logicalOrExpr)*;

logicalOrExpr: logicalAndExpr (OR logicalAndExpr)*;

logicalAndExpr: equalityExpr (AND equalityExpr)*;

equalityExpr: relationalExpr ((EQ | NE) relationalExpr)*;

relationalExpr: additiveExpr ((LT | LE | GT | GE) additiveExpr)*;

additiveExpr: multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*;

multiplicativeExpr: unaryExpr ((MULT | DIV | MOD) unaryExpr)*;

unaryExpr: (MINUS | PLUS | NOT) unaryExpr | postfixExpr;

postfixExpr: primaryExpr (LBRACKET expression RBRACKET | LPAREN argList? RPAREN)*;

primaryExpr: INTLITERAL | FLOATLITERAL | TRUE | FALSE | STRINGLITERAL | arrayLiteral | functionExpr | ID | LPAREN expression RPAREN;

arrayLiteral: LBRACKET (expression (COMMA expression)*)? RBRACKET;

functionExpr: FUNC LPAREN paramList? RPAREN ARROW type blockStmt;

argList: expression (COMMA expression)*;

// ============================================================================
// LEXER RULES
// ============================================================================

// Keywords
BOOL: 'bool';
BREAK: 'break';
CONST: 'const';
CONTINUE: 'continue';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNC: 'func';
IF: 'if';
IN: 'in';
INT: 'int';
LET: 'let';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
VOID: 'void';
WHILE: 'while';

// Operators
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NE: '!=';
LT: '<'; // Less than
LE: '<='; // Less than or equal to
GT: '>'; // Greater than
GE: '>='; // Greater than or equal to
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
COLON: ':'; // Type annotation operator
ARROW: '->'; // Function return type arrow
PIPELINE: '>>';

// Separators
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';
SEMICOLON: ';';
DOT: '.';

// Literals
INTLITERAL: [0-9]+;
FLOATLITERAL: [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?;

// String literals with proper escape handling
STRINGLITERAL: '"' StringCharacter* '"' {
    # Remove the surrounding quotes from the text
    self.text = self.text[1:-1]
};
fragment StringCharacter: ~["\r\n\\] | EscapeSequence;
fragment EscapeSequence: '\\' [nt"\\r];

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Comments
COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT | .)*? '*/' -> skip;

// Whitespace
WS: [ \t\r\n]+ -> skip;

// Error handling tokens (must be at the end)
ILLEGAL_ESCAPE: '"' StringCharacter* '\\' ~[nt"\\r] {
    # Remove the opening quote and get text up to illegal escape
    self.text = self.text[1:]
};

UNCLOSE_STRING: '"' StringCharacter* {
    # Remove the opening quote from the text
    self.text = self.text[1:]
};

ERROR_TOKEN: . {
    # Capture any single character that is not a valid token
    self.text = self.text
};