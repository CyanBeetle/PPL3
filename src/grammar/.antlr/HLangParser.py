# Generated from c:/Users/admin/Desktop/hlang-compiler/src/grammar/HLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,55,369,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,5,0,69,8,0,10,0,12,0,72,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,80,8,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,90,8,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,5,3,100,8,3,10,3,12,3,103,9,3,1,4,1,4,1,4,1,4,1,5,1,
        5,1,6,1,6,1,6,3,6,114,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,135,8,7,10,7,12,7,138,
        9,7,3,7,140,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,149,8,7,1,8,1,8,
        5,8,153,8,8,10,8,12,8,156,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,3,9,170,8,9,1,10,1,10,1,10,1,10,3,10,176,8,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,5,11,187,8,11,10,11,12,11,
        190,9,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,5,12,208,8,12,10,12,12,12,211,9,12,1,12,
        1,12,3,12,215,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,15,1,15,3,15,233,8,15,1,15,1,15,1,16,
        1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,
        5,20,251,8,20,10,20,12,20,254,9,20,1,21,1,21,1,21,5,21,259,8,21,
        10,21,12,21,262,9,21,1,22,1,22,1,22,5,22,267,8,22,10,22,12,22,270,
        9,22,1,23,1,23,1,23,5,23,275,8,23,10,23,12,23,278,9,23,1,24,1,24,
        1,24,5,24,283,8,24,10,24,12,24,286,9,24,1,25,1,25,1,25,5,25,291,
        8,25,10,25,12,25,294,9,25,1,26,1,26,1,26,5,26,299,8,26,10,26,12,
        26,302,9,26,1,27,1,27,1,27,3,27,307,8,27,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,3,28,316,8,28,1,28,5,28,319,8,28,10,28,12,28,322,9,28,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,
        336,8,29,1,30,1,30,1,30,1,30,5,30,342,8,30,10,30,12,30,345,9,30,
        3,30,347,8,30,1,30,1,30,1,31,1,31,1,31,3,31,354,8,31,1,31,1,31,1,
        31,1,31,1,31,1,32,1,32,1,32,5,32,364,8,32,10,32,12,32,367,9,32,1,
        32,0,0,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,0,5,1,0,24,25,1,0,26,29,1,
        0,19,20,1,0,21,23,2,0,19,20,32,32,389,0,70,1,0,0,0,2,75,1,0,0,0,
        4,85,1,0,0,0,6,96,1,0,0,0,8,104,1,0,0,0,10,108,1,0,0,0,12,110,1,
        0,0,0,14,148,1,0,0,0,16,150,1,0,0,0,18,169,1,0,0,0,20,171,1,0,0,
        0,22,181,1,0,0,0,24,195,1,0,0,0,26,216,1,0,0,0,28,222,1,0,0,0,30,
        230,1,0,0,0,32,236,1,0,0,0,34,239,1,0,0,0,36,242,1,0,0,0,38,245,
        1,0,0,0,40,247,1,0,0,0,42,255,1,0,0,0,44,263,1,0,0,0,46,271,1,0,
        0,0,48,279,1,0,0,0,50,287,1,0,0,0,52,295,1,0,0,0,54,306,1,0,0,0,
        56,308,1,0,0,0,58,335,1,0,0,0,60,337,1,0,0,0,62,350,1,0,0,0,64,360,
        1,0,0,0,66,69,3,2,1,0,67,69,3,4,2,0,68,66,1,0,0,0,68,67,1,0,0,0,
        69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,1,
        0,0,0,73,74,5,0,0,1,74,1,1,0,0,0,75,76,5,3,0,0,76,79,5,49,0,0,77,
        78,5,34,0,0,78,80,3,10,5,0,79,77,1,0,0,0,79,80,1,0,0,0,80,81,1,0,
        0,0,81,82,5,33,0,0,82,83,3,38,19,0,83,84,5,44,0,0,84,3,1,0,0,0,85,
        86,5,9,0,0,86,87,5,49,0,0,87,89,5,37,0,0,88,90,3,6,3,0,89,88,1,0,
        0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,38,0,0,92,93,5,35,0,0,93,
        94,3,10,5,0,94,95,3,16,8,0,95,5,1,0,0,0,96,101,3,8,4,0,97,98,5,43,
        0,0,98,100,3,8,4,0,99,97,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,
        101,102,1,0,0,0,102,7,1,0,0,0,103,101,1,0,0,0,104,105,5,49,0,0,105,
        106,5,34,0,0,106,107,3,10,5,0,107,9,1,0,0,0,108,109,3,12,6,0,109,
        11,1,0,0,0,110,113,3,14,7,0,111,112,5,35,0,0,112,114,3,12,6,0,113,
        111,1,0,0,0,113,114,1,0,0,0,114,13,1,0,0,0,115,149,5,12,0,0,116,
        149,5,7,0,0,117,149,5,1,0,0,118,149,5,15,0,0,119,149,5,17,0,0,120,
        121,5,39,0,0,121,122,3,10,5,0,122,123,5,44,0,0,123,124,5,46,0,0,
        124,125,5,40,0,0,125,149,1,0,0,0,126,127,5,39,0,0,127,128,3,10,5,
        0,128,129,5,40,0,0,129,149,1,0,0,0,130,139,5,37,0,0,131,136,3,10,
        5,0,132,133,5,43,0,0,133,135,3,10,5,0,134,132,1,0,0,0,135,138,1,
        0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,140,1,0,0,0,138,136,1,
        0,0,0,139,131,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,5,
        38,0,0,142,143,5,35,0,0,143,149,3,10,5,0,144,145,5,37,0,0,145,146,
        3,10,5,0,146,147,5,38,0,0,147,149,1,0,0,0,148,115,1,0,0,0,148,116,
        1,0,0,0,148,117,1,0,0,0,148,118,1,0,0,0,148,119,1,0,0,0,148,120,
        1,0,0,0,148,126,1,0,0,0,148,130,1,0,0,0,148,144,1,0,0,0,149,15,1,
        0,0,0,150,154,5,41,0,0,151,153,3,18,9,0,152,151,1,0,0,0,153,156,
        1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,157,1,0,0,0,156,154,
        1,0,0,0,157,158,5,42,0,0,158,17,1,0,0,0,159,170,3,20,10,0,160,170,
        3,22,11,0,161,170,3,24,12,0,162,170,3,26,13,0,163,170,3,28,14,0,
        164,170,3,30,15,0,165,170,3,32,16,0,166,170,3,34,17,0,167,170,3,
        16,8,0,168,170,3,36,18,0,169,159,1,0,0,0,169,160,1,0,0,0,169,161,
        1,0,0,0,169,162,1,0,0,0,169,163,1,0,0,0,169,164,1,0,0,0,169,165,
        1,0,0,0,169,166,1,0,0,0,169,167,1,0,0,0,169,168,1,0,0,0,170,19,1,
        0,0,0,171,172,5,13,0,0,172,175,5,49,0,0,173,174,5,34,0,0,174,176,
        3,10,5,0,175,173,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,
        5,33,0,0,178,179,3,38,19,0,179,180,5,44,0,0,180,21,1,0,0,0,181,188,
        5,49,0,0,182,183,5,39,0,0,183,184,3,38,19,0,184,185,5,40,0,0,185,
        187,1,0,0,0,186,182,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,
        189,1,0,0,0,189,191,1,0,0,0,190,188,1,0,0,0,191,192,5,33,0,0,192,
        193,3,38,19,0,193,194,5,44,0,0,194,23,1,0,0,0,195,196,5,10,0,0,196,
        197,5,37,0,0,197,198,3,38,19,0,198,199,5,38,0,0,199,209,3,16,8,0,
        200,201,5,5,0,0,201,202,5,10,0,0,202,203,5,37,0,0,203,204,3,38,19,
        0,204,205,5,38,0,0,205,206,3,16,8,0,206,208,1,0,0,0,207,200,1,0,
        0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,214,1,0,
        0,0,211,209,1,0,0,0,212,213,5,5,0,0,213,215,3,16,8,0,214,212,1,0,
        0,0,214,215,1,0,0,0,215,25,1,0,0,0,216,217,5,18,0,0,217,218,5,37,
        0,0,218,219,3,38,19,0,219,220,5,38,0,0,220,221,3,16,8,0,221,27,1,
        0,0,0,222,223,5,8,0,0,223,224,5,37,0,0,224,225,5,49,0,0,225,226,
        5,11,0,0,226,227,3,38,19,0,227,228,5,38,0,0,228,229,3,16,8,0,229,
        29,1,0,0,0,230,232,5,14,0,0,231,233,3,38,19,0,232,231,1,0,0,0,232,
        233,1,0,0,0,233,234,1,0,0,0,234,235,5,44,0,0,235,31,1,0,0,0,236,
        237,5,2,0,0,237,238,5,44,0,0,238,33,1,0,0,0,239,240,5,4,0,0,240,
        241,5,44,0,0,241,35,1,0,0,0,242,243,3,38,19,0,243,244,5,44,0,0,244,
        37,1,0,0,0,245,246,3,40,20,0,246,39,1,0,0,0,247,252,3,42,21,0,248,
        249,5,36,0,0,249,251,3,42,21,0,250,248,1,0,0,0,251,254,1,0,0,0,252,
        250,1,0,0,0,252,253,1,0,0,0,253,41,1,0,0,0,254,252,1,0,0,0,255,260,
        3,44,22,0,256,257,5,31,0,0,257,259,3,44,22,0,258,256,1,0,0,0,259,
        262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,43,1,0,0,0,262,260,
        1,0,0,0,263,268,3,46,23,0,264,265,5,30,0,0,265,267,3,46,23,0,266,
        264,1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,
        45,1,0,0,0,270,268,1,0,0,0,271,276,3,48,24,0,272,273,7,0,0,0,273,
        275,3,48,24,0,274,272,1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,276,
        277,1,0,0,0,277,47,1,0,0,0,278,276,1,0,0,0,279,284,3,50,25,0,280,
        281,7,1,0,0,281,283,3,50,25,0,282,280,1,0,0,0,283,286,1,0,0,0,284,
        282,1,0,0,0,284,285,1,0,0,0,285,49,1,0,0,0,286,284,1,0,0,0,287,292,
        3,52,26,0,288,289,7,2,0,0,289,291,3,52,26,0,290,288,1,0,0,0,291,
        294,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,51,1,0,0,0,294,292,
        1,0,0,0,295,300,3,54,27,0,296,297,7,3,0,0,297,299,3,54,27,0,298,
        296,1,0,0,0,299,302,1,0,0,0,300,298,1,0,0,0,300,301,1,0,0,0,301,
        53,1,0,0,0,302,300,1,0,0,0,303,304,7,4,0,0,304,307,3,54,27,0,305,
        307,3,56,28,0,306,303,1,0,0,0,306,305,1,0,0,0,307,55,1,0,0,0,308,
        320,3,58,29,0,309,310,5,39,0,0,310,311,3,38,19,0,311,312,5,40,0,
        0,312,319,1,0,0,0,313,315,5,37,0,0,314,316,3,64,32,0,315,314,1,0,
        0,0,315,316,1,0,0,0,316,317,1,0,0,0,317,319,5,38,0,0,318,309,1,0,
        0,0,318,313,1,0,0,0,319,322,1,0,0,0,320,318,1,0,0,0,320,321,1,0,
        0,0,321,57,1,0,0,0,322,320,1,0,0,0,323,336,5,46,0,0,324,336,5,47,
        0,0,325,336,5,16,0,0,326,336,5,6,0,0,327,336,5,48,0,0,328,336,3,
        60,30,0,329,336,3,62,31,0,330,336,5,49,0,0,331,332,5,37,0,0,332,
        333,3,38,19,0,333,334,5,38,0,0,334,336,1,0,0,0,335,323,1,0,0,0,335,
        324,1,0,0,0,335,325,1,0,0,0,335,326,1,0,0,0,335,327,1,0,0,0,335,
        328,1,0,0,0,335,329,1,0,0,0,335,330,1,0,0,0,335,331,1,0,0,0,336,
        59,1,0,0,0,337,346,5,39,0,0,338,343,3,38,19,0,339,340,5,43,0,0,340,
        342,3,38,19,0,341,339,1,0,0,0,342,345,1,0,0,0,343,341,1,0,0,0,343,
        344,1,0,0,0,344,347,1,0,0,0,345,343,1,0,0,0,346,338,1,0,0,0,346,
        347,1,0,0,0,347,348,1,0,0,0,348,349,5,40,0,0,349,61,1,0,0,0,350,
        351,5,9,0,0,351,353,5,37,0,0,352,354,3,6,3,0,353,352,1,0,0,0,353,
        354,1,0,0,0,354,355,1,0,0,0,355,356,5,38,0,0,356,357,5,35,0,0,357,
        358,3,10,5,0,358,359,3,16,8,0,359,63,1,0,0,0,360,365,3,38,19,0,361,
        362,5,43,0,0,362,364,3,38,19,0,363,361,1,0,0,0,364,367,1,0,0,0,365,
        363,1,0,0,0,365,366,1,0,0,0,366,65,1,0,0,0,367,365,1,0,0,0,32,68,
        70,79,89,101,113,136,139,148,154,169,175,188,209,214,232,252,260,
        268,276,284,292,300,306,315,318,320,335,343,346,353,365
    ]

class HLangParser ( Parser ):

    grammarFileName = "HLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'bool'", "'break'", "'const'", "'continue'", 
                     "'else'", "'false'", "'float'", "'for'", "'func'", 
                     "'if'", "'in'", "'int'", "'let'", "'return'", "'string'", 
                     "'true'", "'void'", "'while'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'&&'", "'||'", "'!'", "'='", "':'", "'->'", 
                     "'>>'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
                     "';'", "'.'" ]

    symbolicNames = [ "<INVALID>", "BOOL", "BREAK", "CONST", "CONTINUE", 
                      "ELSE", "FALSE", "FLOAT", "FOR", "FUNC", "IF", "IN", 
                      "INT", "LET", "RETURN", "STRING", "TRUE", "VOID", 
                      "WHILE", "PLUS", "MINUS", "MULT", "DIV", "MOD", "EQ", 
                      "NE", "LT", "LE", "GT", "GE", "AND", "OR", "NOT", 
                      "ASSIGN", "COLON", "ARROW", "PIPELINE", "LPAREN", 
                      "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", 
                      "COMMA", "SEMICOLON", "DOT", "INTLITERAL", "FLOATLITERAL", 
                      "STRINGLITERAL", "ID", "COMMENT", "BLOCK_COMMENT", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_constDecl = 1
    RULE_funcDecl = 2
    RULE_paramList = 3
    RULE_param = 4
    RULE_type = 5
    RULE_functionType = 6
    RULE_atomicType = 7
    RULE_blockStmt = 8
    RULE_stmt = 9
    RULE_varDecl = 10
    RULE_assignment = 11
    RULE_ifStmt = 12
    RULE_whileStmt = 13
    RULE_forStmt = 14
    RULE_returnStmt = 15
    RULE_breakStmt = 16
    RULE_continueStmt = 17
    RULE_expressionStmt = 18
    RULE_expression = 19
    RULE_pipelineExpr = 20
    RULE_logicalOrExpr = 21
    RULE_logicalAndExpr = 22
    RULE_equalityExpr = 23
    RULE_relationalExpr = 24
    RULE_additiveExpr = 25
    RULE_multiplicativeExpr = 26
    RULE_unaryExpr = 27
    RULE_postfixExpr = 28
    RULE_primaryExpr = 29
    RULE_arrayLiteral = 30
    RULE_functionExpr = 31
    RULE_argList = 32

    ruleNames =  [ "program", "constDecl", "funcDecl", "paramList", "param", 
                   "type", "functionType", "atomicType", "blockStmt", "stmt", 
                   "varDecl", "assignment", "ifStmt", "whileStmt", "forStmt", 
                   "returnStmt", "breakStmt", "continueStmt", "expressionStmt", 
                   "expression", "pipelineExpr", "logicalOrExpr", "logicalAndExpr", 
                   "equalityExpr", "relationalExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "postfixExpr", "primaryExpr", "arrayLiteral", 
                   "functionExpr", "argList" ]

    EOF = Token.EOF
    BOOL=1
    BREAK=2
    CONST=3
    CONTINUE=4
    ELSE=5
    FALSE=6
    FLOAT=7
    FOR=8
    FUNC=9
    IF=10
    IN=11
    INT=12
    LET=13
    RETURN=14
    STRING=15
    TRUE=16
    VOID=17
    WHILE=18
    PLUS=19
    MINUS=20
    MULT=21
    DIV=22
    MOD=23
    EQ=24
    NE=25
    LT=26
    LE=27
    GT=28
    GE=29
    AND=30
    OR=31
    NOT=32
    ASSIGN=33
    COLON=34
    ARROW=35
    PIPELINE=36
    LPAREN=37
    RPAREN=38
    LBRACKET=39
    RBRACKET=40
    LBRACE=41
    RBRACE=42
    COMMA=43
    SEMICOLON=44
    DOT=45
    INTLITERAL=46
    FLOATLITERAL=47
    STRINGLITERAL=48
    ID=49
    COMMENT=50
    BLOCK_COMMENT=51
    WS=52
    ILLEGAL_ESCAPE=53
    UNCLOSE_STRING=54
    ERROR_TOKEN=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HLangParser.EOF, 0)

        def constDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ConstDeclContext)
            else:
                return self.getTypedRuleContext(HLangParser.ConstDeclContext,i)


        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(HLangParser.FuncDeclContext,i)


        def getRuleIndex(self):
            return HLangParser.RULE_program




    def program(self):

        localctx = HLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==9:
                self.state = 68
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 66
                    self.constDecl()
                    pass
                elif token in [9]:
                    self.state = 67
                    self.funcDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(HLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(HLangParser.CONST, 0)

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(HLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(HLangParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def COLON(self):
            return self.getToken(HLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(HLangParser.TypeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_constDecl




    def constDecl(self):

        localctx = HLangParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_constDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(HLangParser.CONST)
            self.state = 76
            self.match(HLangParser.ID)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 77
                self.match(HLangParser.COLON)
                self.state = 78
                self.type_()


            self.state = 81
            self.match(HLangParser.ASSIGN)
            self.state = 82
            self.expression()
            self.state = 83
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(HLangParser.FUNC, 0)

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(HLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(HLangParser.RPAREN, 0)

        def ARROW(self):
            return self.getToken(HLangParser.ARROW, 0)

        def type_(self):
            return self.getTypedRuleContext(HLangParser.TypeContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(HLangParser.BlockStmtContext,0)


        def paramList(self):
            return self.getTypedRuleContext(HLangParser.ParamListContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_funcDecl




    def funcDecl(self):

        localctx = HLangParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(HLangParser.FUNC)
            self.state = 86
            self.match(HLangParser.ID)
            self.state = 87
            self.match(HLangParser.LPAREN)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 88
                self.paramList()


            self.state = 91
            self.match(HLangParser.RPAREN)
            self.state = 92
            self.match(HLangParser.ARROW)
            self.state = 93
            self.type_()
            self.state = 94
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(HLangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.COMMA)
            else:
                return self.getToken(HLangParser.COMMA, i)

        def getRuleIndex(self):
            return HLangParser.RULE_paramList




    def paramList(self):

        localctx = HLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.param()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 97
                self.match(HLangParser.COMMA)
                self.state = 98
                self.param()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def COLON(self):
            return self.getToken(HLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(HLangParser.TypeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_param




    def param(self):

        localctx = HLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(HLangParser.ID)
            self.state = 105
            self.match(HLangParser.COLON)
            self.state = 106
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionType(self):
            return self.getTypedRuleContext(HLangParser.FunctionTypeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_type




    def type_(self):

        localctx = HLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.functionType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomicType(self):
            return self.getTypedRuleContext(HLangParser.AtomicTypeContext,0)


        def ARROW(self):
            return self.getToken(HLangParser.ARROW, 0)

        def functionType(self):
            return self.getTypedRuleContext(HLangParser.FunctionTypeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_functionType




    def functionType(self):

        localctx = HLangParser.FunctionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.atomicType()
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 111
                self.match(HLangParser.ARROW)
                self.state = 112
                self.functionType()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomicTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(HLangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(HLangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(HLangParser.STRING, 0)

        def VOID(self):
            return self.getToken(HLangParser.VOID, 0)

        def LBRACKET(self):
            return self.getToken(HLangParser.LBRACKET, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.TypeContext)
            else:
                return self.getTypedRuleContext(HLangParser.TypeContext,i)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def INTLITERAL(self):
            return self.getToken(HLangParser.INTLITERAL, 0)

        def RBRACKET(self):
            return self.getToken(HLangParser.RBRACKET, 0)

        def LPAREN(self):
            return self.getToken(HLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(HLangParser.RPAREN, 0)

        def ARROW(self):
            return self.getToken(HLangParser.ARROW, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.COMMA)
            else:
                return self.getToken(HLangParser.COMMA, i)

        def getRuleIndex(self):
            return HLangParser.RULE_atomicType




    def atomicType(self):

        localctx = HLangParser.AtomicTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atomicType)
        self._la = 0 # Token type
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(HLangParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(HLangParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.match(HLangParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 118
                self.match(HLangParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.match(HLangParser.VOID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 120
                self.match(HLangParser.LBRACKET)
                self.state = 121
                self.type_()
                self.state = 122
                self.match(HLangParser.SEMICOLON)
                self.state = 123
                self.match(HLangParser.INTLITERAL)
                self.state = 124
                self.match(HLangParser.RBRACKET)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 126
                self.match(HLangParser.LBRACKET)
                self.state = 127
                self.type_()
                self.state = 128
                self.match(HLangParser.RBRACKET)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 130
                self.match(HLangParser.LPAREN)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 687194935426) != 0):
                    self.state = 131
                    self.type_()
                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==43:
                        self.state = 132
                        self.match(HLangParser.COMMA)
                        self.state = 133
                        self.type_()
                        self.state = 138
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 141
                self.match(HLangParser.RPAREN)
                self.state = 142
                self.match(HLangParser.ARROW)
                self.state = 143
                self.type_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 144
                self.match(HLangParser.LPAREN)
                self.state = 145
                self.type_()
                self.state = 146
                self.match(HLangParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(HLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(HLangParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(HLangParser.StmtContext,i)


        def getRuleIndex(self):
            return HLangParser.RULE_blockStmt




    def blockStmt(self):

        localctx = HLangParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(HLangParser.LBRACE)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1058421677582164) != 0):
                self.state = 151
                self.stmt()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(HLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(HLangParser.VarDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(HLangParser.AssignmentContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(HLangParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(HLangParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(HLangParser.ForStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(HLangParser.ReturnStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(HLangParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(HLangParser.ContinueStmtContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(HLangParser.BlockStmtContext,0)


        def expressionStmt(self):
            return self.getTypedRuleContext(HLangParser.ExpressionStmtContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_stmt




    def stmt(self):

        localctx = HLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmt)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.whileStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.forStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 164
                self.returnStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 165
                self.breakStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 166
                self.continueStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 167
                self.blockStmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 168
                self.expressionStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(HLangParser.LET, 0)

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(HLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(HLangParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def COLON(self):
            return self.getToken(HLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(HLangParser.TypeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_varDecl




    def varDecl(self):

        localctx = HLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(HLangParser.LET)
            self.state = 172
            self.match(HLangParser.ID)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 173
                self.match(HLangParser.COLON)
                self.state = 174
                self.type_()


            self.state = 177
            self.match(HLangParser.ASSIGN)
            self.state = 178
            self.expression()
            self.state = 179
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(HLangParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HLangParser.ExpressionContext,i)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.LBRACKET)
            else:
                return self.getToken(HLangParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.RBRACKET)
            else:
                return self.getToken(HLangParser.RBRACKET, i)

        def getRuleIndex(self):
            return HLangParser.RULE_assignment




    def assignment(self):

        localctx = HLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(HLangParser.ID)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 182
                self.match(HLangParser.LBRACKET)
                self.state = 183
                self.expression()
                self.state = 184
                self.match(HLangParser.RBRACKET)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
            self.match(HLangParser.ASSIGN)
            self.state = 192
            self.expression()
            self.state = 193
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.IF)
            else:
                return self.getToken(HLangParser.IF, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.LPAREN)
            else:
                return self.getToken(HLangParser.LPAREN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HLangParser.ExpressionContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.RPAREN)
            else:
                return self.getToken(HLangParser.RPAREN, i)

        def blockStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.BlockStmtContext)
            else:
                return self.getTypedRuleContext(HLangParser.BlockStmtContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.ELSE)
            else:
                return self.getToken(HLangParser.ELSE, i)

        def getRuleIndex(self):
            return HLangParser.RULE_ifStmt




    def ifStmt(self):

        localctx = HLangParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(HLangParser.IF)
            self.state = 196
            self.match(HLangParser.LPAREN)
            self.state = 197
            self.expression()
            self.state = 198
            self.match(HLangParser.RPAREN)
            self.state = 199
            self.blockStmt()
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 200
                    self.match(HLangParser.ELSE)
                    self.state = 201
                    self.match(HLangParser.IF)
                    self.state = 202
                    self.match(HLangParser.LPAREN)
                    self.state = 203
                    self.expression()
                    self.state = 204
                    self.match(HLangParser.RPAREN)
                    self.state = 205
                    self.blockStmt() 
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 212
                self.match(HLangParser.ELSE)
                self.state = 213
                self.blockStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(HLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(HLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(HLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(HLangParser.RPAREN, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(HLangParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_whileStmt




    def whileStmt(self):

        localctx = HLangParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(HLangParser.WHILE)
            self.state = 217
            self.match(HLangParser.LPAREN)
            self.state = 218
            self.expression()
            self.state = 219
            self.match(HLangParser.RPAREN)
            self.state = 220
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(HLangParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(HLangParser.LPAREN, 0)

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def IN(self):
            return self.getToken(HLangParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(HLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(HLangParser.RPAREN, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(HLangParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_forStmt




    def forStmt(self):

        localctx = HLangParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(HLangParser.FOR)
            self.state = 223
            self.match(HLangParser.LPAREN)
            self.state = 224
            self.match(HLangParser.ID)
            self.state = 225
            self.match(HLangParser.IN)
            self.state = 226
            self.expression()
            self.state = 227
            self.match(HLangParser.RPAREN)
            self.state = 228
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(HLangParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(HLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_returnStmt




    def returnStmt(self):

        localctx = HLangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(HLangParser.RETURN)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056222654038592) != 0):
                self.state = 231
                self.expression()


            self.state = 234
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(HLangParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_breakStmt




    def breakStmt(self):

        localctx = HLangParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(HLangParser.BREAK)
            self.state = 237
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(HLangParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_continueStmt




    def continueStmt(self):

        localctx = HLangParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(HLangParser.CONTINUE)
            self.state = 240
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(HLangParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_expressionStmt




    def expressionStmt(self):

        localctx = HLangParser.ExpressionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expressionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.expression()
            self.state = 243
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipelineExpr(self):
            return self.getTypedRuleContext(HLangParser.PipelineExprContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_expression




    def expression(self):

        localctx = HLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.pipelineExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipelineExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.LogicalOrExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.LogicalOrExprContext,i)


        def PIPELINE(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.PIPELINE)
            else:
                return self.getToken(HLangParser.PIPELINE, i)

        def getRuleIndex(self):
            return HLangParser.RULE_pipelineExpr




    def pipelineExpr(self):

        localctx = HLangParser.PipelineExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_pipelineExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.logicalOrExpr()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 248
                self.match(HLangParser.PIPELINE)
                self.state = 249
                self.logicalOrExpr()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.LogicalAndExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.LogicalAndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.OR)
            else:
                return self.getToken(HLangParser.OR, i)

        def getRuleIndex(self):
            return HLangParser.RULE_logicalOrExpr




    def logicalOrExpr(self):

        localctx = HLangParser.LogicalOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logicalOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.logicalAndExpr()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 256
                self.match(HLangParser.OR)
                self.state = 257
                self.logicalAndExpr()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.EqualityExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.EqualityExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.AND)
            else:
                return self.getToken(HLangParser.AND, i)

        def getRuleIndex(self):
            return HLangParser.RULE_logicalAndExpr




    def logicalAndExpr(self):

        localctx = HLangParser.LogicalAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_logicalAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.equalityExpr()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 264
                self.match(HLangParser.AND)
                self.state = 265
                self.equalityExpr()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.RelationalExprContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.EQ)
            else:
                return self.getToken(HLangParser.EQ, i)

        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.NE)
            else:
                return self.getToken(HLangParser.NE, i)

        def getRuleIndex(self):
            return HLangParser.RULE_equalityExpr




    def equalityExpr(self):

        localctx = HLangParser.EqualityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_equalityExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.relationalExpr()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 272
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 273
                self.relationalExpr()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.AdditiveExprContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.LT)
            else:
                return self.getToken(HLangParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.LE)
            else:
                return self.getToken(HLangParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.GT)
            else:
                return self.getToken(HLangParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.GE)
            else:
                return self.getToken(HLangParser.GE, i)

        def getRuleIndex(self):
            return HLangParser.RULE_relationalExpr




    def relationalExpr(self):

        localctx = HLangParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.additiveExpr()
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0):
                self.state = 280
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 281
                self.additiveExpr()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.MultiplicativeExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.PLUS)
            else:
                return self.getToken(HLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.MINUS)
            else:
                return self.getToken(HLangParser.MINUS, i)

        def getRuleIndex(self):
            return HLangParser.RULE_additiveExpr




    def additiveExpr(self):

        localctx = HLangParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.multiplicativeExpr()
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 288
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 289
                self.multiplicativeExpr()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.UnaryExprContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.MULT)
            else:
                return self.getToken(HLangParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.DIV)
            else:
                return self.getToken(HLangParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.MOD)
            else:
                return self.getToken(HLangParser.MOD, i)

        def getRuleIndex(self):
            return HLangParser.RULE_multiplicativeExpr




    def multiplicativeExpr(self):

        localctx = HLangParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.unaryExpr()
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0):
                self.state = 296
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 297
                self.unaryExpr()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(HLangParser.UnaryExprContext,0)


        def MINUS(self):
            return self.getToken(HLangParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(HLangParser.PLUS, 0)

        def NOT(self):
            return self.getToken(HLangParser.NOT, 0)

        def postfixExpr(self):
            return self.getTypedRuleContext(HLangParser.PostfixExprContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_unaryExpr




    def unaryExpr(self):

        localctx = HLangParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4296540160) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 304
                self.unaryExpr()
                pass
            elif token in [6, 9, 16, 37, 39, 46, 47, 48, 49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.postfixExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(HLangParser.PrimaryExprContext,0)


        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.LBRACKET)
            else:
                return self.getToken(HLangParser.LBRACKET, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HLangParser.ExpressionContext,i)


        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.RBRACKET)
            else:
                return self.getToken(HLangParser.RBRACKET, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.LPAREN)
            else:
                return self.getToken(HLangParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.RPAREN)
            else:
                return self.getToken(HLangParser.RPAREN, i)

        def argList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ArgListContext)
            else:
                return self.getTypedRuleContext(HLangParser.ArgListContext,i)


        def getRuleIndex(self):
            return HLangParser.RULE_postfixExpr




    def postfixExpr(self):

        localctx = HLangParser.PostfixExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_postfixExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.primaryExpr()
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37 or _la==39:
                self.state = 318
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [39]:
                    self.state = 309
                    self.match(HLangParser.LBRACKET)
                    self.state = 310
                    self.expression()
                    self.state = 311
                    self.match(HLangParser.RBRACKET)
                    pass
                elif token in [37]:
                    self.state = 313
                    self.match(HLangParser.LPAREN)
                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056222654038592) != 0):
                        self.state = 314
                        self.argList()


                    self.state = 317
                    self.match(HLangParser.RPAREN)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLITERAL(self):
            return self.getToken(HLangParser.INTLITERAL, 0)

        def FLOATLITERAL(self):
            return self.getToken(HLangParser.FLOATLITERAL, 0)

        def TRUE(self):
            return self.getToken(HLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(HLangParser.FALSE, 0)

        def STRINGLITERAL(self):
            return self.getToken(HLangParser.STRINGLITERAL, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(HLangParser.ArrayLiteralContext,0)


        def functionExpr(self):
            return self.getTypedRuleContext(HLangParser.FunctionExprContext,0)


        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(HLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(HLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(HLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_primaryExpr




    def primaryExpr(self):

        localctx = HLangParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_primaryExpr)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(HLangParser.INTLITERAL)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(HLangParser.FLOATLITERAL)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.match(HLangParser.TRUE)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
                self.match(HLangParser.FALSE)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 5)
                self.state = 327
                self.match(HLangParser.STRINGLITERAL)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 328
                self.arrayLiteral()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 7)
                self.state = 329
                self.functionExpr()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 8)
                self.state = 330
                self.match(HLangParser.ID)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 9)
                self.state = 331
                self.match(HLangParser.LPAREN)
                self.state = 332
                self.expression()
                self.state = 333
                self.match(HLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(HLangParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(HLangParser.RBRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.COMMA)
            else:
                return self.getToken(HLangParser.COMMA, i)

        def getRuleIndex(self):
            return HLangParser.RULE_arrayLiteral




    def arrayLiteral(self):

        localctx = HLangParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(HLangParser.LBRACKET)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056222654038592) != 0):
                self.state = 338
                self.expression()
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==43:
                    self.state = 339
                    self.match(HLangParser.COMMA)
                    self.state = 340
                    self.expression()
                    self.state = 345
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 348
            self.match(HLangParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(HLangParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(HLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(HLangParser.RPAREN, 0)

        def ARROW(self):
            return self.getToken(HLangParser.ARROW, 0)

        def type_(self):
            return self.getTypedRuleContext(HLangParser.TypeContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(HLangParser.BlockStmtContext,0)


        def paramList(self):
            return self.getTypedRuleContext(HLangParser.ParamListContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_functionExpr




    def functionExpr(self):

        localctx = HLangParser.FunctionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(HLangParser.FUNC)
            self.state = 351
            self.match(HLangParser.LPAREN)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 352
                self.paramList()


            self.state = 355
            self.match(HLangParser.RPAREN)
            self.state = 356
            self.match(HLangParser.ARROW)
            self.state = 357
            self.type_()
            self.state = 358
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.COMMA)
            else:
                return self.getToken(HLangParser.COMMA, i)

        def getRuleIndex(self):
            return HLangParser.RULE_argList




    def argList(self):

        localctx = HLangParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.expression()
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 361
                self.match(HLangParser.COMMA)
                self.state = 362
                self.expression()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





