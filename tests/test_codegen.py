from src.utils.nodes import *

from utils import CodeGenerator


def test_001():
    """Test basic print statement"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"), [StringLiteral("Hello World")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_002():
    """Test if statement with print"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    IfStmt(
                        BooleanLiteral(True),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"), [StringLiteral("True branch")]
                                )
                            )
                        ]),
                        [],  # No elif branches
                        None  # No else branch
                    )
                ],
            )
        ],
    )
    expected = "True branch"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_003():
    """Test variable declaration and print with int2str"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(42)),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"), 
                            [FunctionCall(Identifier("int2str"), [Identifier("x")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_004():
    """Test arithmetic expression with print"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"),
                                [BinaryOp(IntegerLiteral(5), "+", IntegerLiteral(3))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
def test_005():
    """Test while loop with correct newline output"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("i", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<", IntegerLiteral(3)),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"), [StringLiteral("Loop")]
                                )
                            ),
                            Assignment(
                                IdLValue("i"),
                                BinaryOp(Identifier("i"), "+", IntegerLiteral(1))
                            )
                        ])
                    )
                ],
            )
        ],
    )
    """
HLang Code Generation Test Suite
Tests basic language features for bytecode generation.
These tests are based on the HLang specification and assume no existing codegen implementation.
"""

from src.utils.nodes import *
from utils import CodeGenerator


# ============================================================================
# BASIC LITERAL AND PRINT TESTS
# ============================================================================

def test_001():
    """Test basic string literal with print"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"), [StringLiteral("Hello World")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_002():
    """Test integer literal with conversion and print"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [IntegerLiteral(42)])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_003():
    """Test float literal with conversion and print"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [FloatLiteral(3.14)])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_004():
    """Test boolean literal true with conversion and print"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("bool2str"), [BooleanLiteral(True)])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_005():
    """Test boolean literal false with conversion and print"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("bool2str"), [BooleanLiteral(False)])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "false"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ============================================================================
# VARIABLE DECLARATION AND ASSIGNMENT TESTS
# ============================================================================

def test_006():
    """Test variable declaration with integer"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(25)),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("x")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "25"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_007():
    """Test variable declaration with string"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("name", StringType(), StringLiteral("Alice")),
                    ExprStmt(
                        FunctionCall(Identifier("print"), [Identifier("name")])
                    )
                ],
            )
        ],
    )
    expected = "Alice"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_008():
    """Test variable assignment after declaration"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(10)),
                    Assignment(IdLValue("x"), IntegerLiteral(20)),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("x")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ============================================================================
# ARITHMETIC EXPRESSION TESTS
# ============================================================================

def test_009():
    """Test integer addition"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"),
                                [BinaryOp(IntegerLiteral(5), "+", IntegerLiteral(3))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_010():
    """Test integer subtraction"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"),
                                [BinaryOp(IntegerLiteral(10), "-", IntegerLiteral(4))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_011():
    """Test integer multiplication"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"),
                                [BinaryOp(IntegerLiteral(6), "*", IntegerLiteral(7))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_012():
    """Test integer division"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"),
                                [BinaryOp(IntegerLiteral(15), "/", IntegerLiteral(3))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_013():
    """Test complex arithmetic expression with variables"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", IntType(), IntegerLiteral(5)),
                    VarDecl("b", IntType(), IntegerLiteral(3)),
                    VarDecl("result", IntType(), 
                        BinaryOp(
                            BinaryOp(Identifier("a"), "+", Identifier("b")),
                            "*",
                            IntegerLiteral(2)
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("result")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "16"  # (5 + 3) * 2 = 16
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ============================================================================
# COMPARISON AND BOOLEAN TESTS
# ============================================================================

def test_014():
    """Test integer comparison (less than)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", BoolType(), 
                        BinaryOp(IntegerLiteral(5), "<", IntegerLiteral(10))
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("bool2str"), [Identifier("result")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_015():
    """Test integer equality comparison"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", BoolType(), 
                        BinaryOp(IntegerLiteral(42), "==", IntegerLiteral(42))
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("bool2str"), [Identifier("result")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ============================================================================
# CONTROL FLOW TESTS
# ============================================================================

def test_016():
    """Test simple if statement with true condition"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    IfStmt(
                        BooleanLiteral(True),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"), [StringLiteral("True branch")]
                                )
                            )
                        ]),
                        [],  # No elif branches
                        None  # No else branch
                    )
                ],
            )
        ],
    )
    expected = "True branch"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_017():
    """Test if-else statement with false condition"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    IfStmt(
                        BooleanLiteral(False),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"), [StringLiteral("True branch")]
                                )
                            )
                        ]),
                        [],  # No elif branches
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"), [StringLiteral("False branch")]
                                )
                            )
                        ])  # Else branch
                    )
                ],
            )
        ],
    )
    expected = "False branch"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_018():
    """Test simple while loop with counter"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("i", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<", IntegerLiteral(3)),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"), [StringLiteral("Loop")]
                                )
                            ),
                            Assignment(
                                IdLValue("i"),
                                BinaryOp(Identifier("i"), "+", IntegerLiteral(1))
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "Loop\nLoop\nLoop"  # print adds newlines
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ============================================================================
# FUNCTION TESTS
# ============================================================================

def test_019():
    """Test user-defined function with parameters and return"""
    ast = Program(
        [],
        [
            FuncDecl(
                "add",
                [Param("a", IntType()), Param("b", IntType())],
                IntType(),
                [
                    ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", IntType(), 
                        FunctionCall(
                            Identifier("add"), 
                            [IntegerLiteral(15), IntegerLiteral(27)]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("result")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_020():
    """Test string concatenation"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("greeting", StringType(), StringLiteral("Hello")),
                    VarDecl("name", StringType(), StringLiteral("World")),
                    VarDecl("message", StringType(), 
                        BinaryOp(
                            BinaryOp(Identifier("greeting"), "+", StringLiteral(" ")),
                            "+",
                            Identifier("name")
                        )
                    ),
                    ExprStmt(
                        FunctionCall(Identifier("print"), [Identifier("message")])
                    )
                ],
            )
        ],
    )
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_021():
    """Test complex arithmetic expression with proper stack management: (a + b) * (c - d)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", IntType(), IntegerLiteral(5)),
                    VarDecl("b", IntType(), IntegerLiteral(3)),
                    VarDecl("c", IntType(), IntegerLiteral(10)),
                    VarDecl("d", IntType(), IntegerLiteral(2)),
                    VarDecl("result", IntType(),
                        BinaryOp(
                            BinaryOp(Identifier("a"), "+", Identifier("b")),  # (5 + 3) = 8
                            "*",
                            BinaryOp(Identifier("c"), "-", Identifier("d"))   # (10 - 2) = 8
                        )  # 8 * 8 = 64
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("result")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "64"  # (5 + 3) * (10 - 2) = 8 * 8 = 64
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
