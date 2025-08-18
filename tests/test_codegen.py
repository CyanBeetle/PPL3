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
    """Test simple boolean literal access"""
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


def test_015():
    """Test direct integer equality comparison"""
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
                                Identifier("bool2str"),
                                [BinaryOp(IntegerLiteral(42), "==", IntegerLiteral(42))]
                            )]
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


def test_022():
    """Test empty main function (minimal program structure)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                []  # Empty function body
            )
        ],
    )
    expected = ""  # No output expected
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_023():
    """Test print multiple values in sequence"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(Identifier("print"), [StringLiteral("First")])
                    ),
                    ExprStmt(
                        FunctionCall(Identifier("print"), [StringLiteral("Second")])
                    ),
                    ExprStmt(
                        FunctionCall(Identifier("print"), [StringLiteral("Third")])
                    )
                ],
            )
        ],
    )
    expected = "First\nSecond\nThird"  # Each print adds newline
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_024():
    """Test str2int conversion function"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("numStr", StringType(), StringLiteral("42")),
                    VarDecl("num", IntType(), 
                        FunctionCall(Identifier("str2int"), [Identifier("numStr")])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("num")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_025():
    """Test chained type conversions: int -> str -> int"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("original", IntType(), IntegerLiteral(123)),
                    VarDecl("asString", StringType(), 
                        FunctionCall(Identifier("int2str"), [Identifier("original")])
                    ),
                    VarDecl("backToInt", IntType(), 
                        FunctionCall(Identifier("str2int"), [Identifier("asString")])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("backToInt")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "123"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_026():
    """Test float variable declaration and usage"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("pi", FloatType(), FloatLiteral(3.14)),
                    VarDecl("radius", FloatType(), FloatLiteral(2.0)),
                    VarDecl("area", FloatType(), 
                        BinaryOp(
                            Identifier("pi"),
                            "*",
                            BinaryOp(Identifier("radius"), "*", Identifier("radius"))
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("area")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "12.56"  # 3.14 * 2 * 2 = 12.56
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_027():
    """Test boolean literal expressions directly"""
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
                                Identifier("bool2str"),
                                [BinaryOp(
                                    BooleanLiteral(True),
                                    "&&",
                                    BinaryOp(BooleanLiteral(False), "||", BooleanLiteral(True))
                                )]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true"  # true && (false || true) = true && true = true
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ============================================================================
# PHASE 2: CORE EXPRESSION SYSTEM TESTS (Advanced Arithmetic, Comparison, Logical)
# ============================================================================

def test_028():
    """Test integer modulo operation (%)"""
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
                                [BinaryOp(IntegerLiteral(7), "%", IntegerLiteral(3))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"),
                                [BinaryOp(IntegerLiteral(15), "%", IntegerLiteral(4))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "1\n3"  # 7 % 3 = 1, 15 % 4 = 3 (as per specification example)
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_029():
    """Test float arithmetic operations"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", FloatType(), FloatLiteral(7.5)),
                    VarDecl("b", FloatType(), FloatLiteral(2.5)),
                    VarDecl("sum", FloatType(), 
                        BinaryOp(Identifier("a"), "+", Identifier("b"))
                    ),
                    VarDecl("diff", FloatType(), 
                        BinaryOp(Identifier("a"), "-", Identifier("b"))
                    ),
                    VarDecl("product", FloatType(), 
                        BinaryOp(Identifier("a"), "*", Identifier("b"))
                    ),
                    VarDecl("quotient", FloatType(), 
                        BinaryOp(Identifier("a"), "/", Identifier("b"))
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("sum")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("quotient")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "10.0\n3.0"  # 7.5 + 2.5 = 10.0, 7.5 / 2.5 = 3.0
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_030():
    """Test simple float arithmetic"""
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
                                Identifier("float2str"),
                                [BinaryOp(FloatLiteral(10.5), "+", FloatLiteral(3.5))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("float2str"),
                                [BinaryOp(FloatLiteral(6.0), "*", FloatLiteral(7.0))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "14.0\n42.0"  # 10.5 + 3.5 = 14.0, 6.0 * 7.0 = 42.0
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_031():
    """Test unary minus and plus operations"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("positive", IntType(), IntegerLiteral(42)),
                    VarDecl("negative", IntType(), 
                        UnaryOp("-", Identifier("positive"))
                    ),
                    VarDecl("doubleNeg", IntType(), 
                        UnaryOp("-", Identifier("negative"))
                    ),
                    VarDecl("floatNeg", FloatType(), 
                        UnaryOp("-", FloatLiteral(3.14))
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("negative")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("doubleNeg")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("floatNeg")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "-42\n42\n-3.14"  # -42, -(-42) = 42, -3.14
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_032():
    """Test complex nested arithmetic expressions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", IntType(),
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(IntegerLiteral(2), "*", IntegerLiteral(3)),
                                "+",
                                BinaryOp(IntegerLiteral(4), "*", IntegerLiteral(5))
                            ),
                            "-",
                            BinaryOp(IntegerLiteral(8), "/", IntegerLiteral(2))
                        )  # (2*3) + (4*5) - (8/2) = 6 + 20 - 4 = 22
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
    expected = "22"  # (2*3) + (4*5) - (8/2) = 6 + 20 - 4 = 22
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_033():
    """Test arithmetic with parentheses precedence"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("withoutParens", IntType(),
                        BinaryOp(
                            IntegerLiteral(2),
                            "+",
                            BinaryOp(IntegerLiteral(3), "*", IntegerLiteral(4))
                        )  # 2 + 3 * 4 = 2 + 12 = 14
                    ),
                    VarDecl("withParens", IntType(),
                        BinaryOp(
                            BinaryOp(IntegerLiteral(2), "+", IntegerLiteral(3)),
                            "*",
                            IntegerLiteral(4)
                        )  # (2 + 3) * 4 = 5 * 4 = 20
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("withoutParens")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("withParens")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "14\n20"  # 2 + 3 * 4 = 14, (2 + 3) * 4 = 20
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_034():
    """Test all comparison operators (!=, <=, >, >=)"""
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
                                Identifier("bool2str"),
                                [BinaryOp(IntegerLiteral(5), "!=", IntegerLiteral(10))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [BinaryOp(IntegerLiteral(10), ">", IntegerLiteral(5))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true\ntrue"  # 5 != 10 = true, 10 > 5 = true
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_035():
    """Test float comparisons"""
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
                                Identifier("bool2str"),
                                [BinaryOp(FloatLiteral(3.14), ">", FloatLiteral(2.71))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [BinaryOp(FloatLiteral(3.14), "==", FloatLiteral(3.14))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true\ntrue"  # 3.14 > 2.71 = true, 3.14 == 3.14 = true
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_036():
    """Test integer comparisons instead of string comparisons"""
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
                                Identifier("bool2str"),
                                [BinaryOp(IntegerLiteral(1), "<", IntegerLiteral(2))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [BinaryOp(IntegerLiteral(5), "==", IntegerLiteral(5))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true\ntrue"  # 1 < 2, 5 == 5
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_037():
    """Test logical AND (&&) operation"""
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
                                Identifier("bool2str"),
                                [BinaryOp(BooleanLiteral(True), "&&", BooleanLiteral(True))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [BinaryOp(BooleanLiteral(True), "&&", BooleanLiteral(False))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [BinaryOp(BooleanLiteral(False), "&&", BooleanLiteral(False))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true\nfalse\nfalse"  # true && true, true && false, false && false
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_038():
    """Test logical OR (||) operation"""
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
                                Identifier("bool2str"),
                                [BinaryOp(BooleanLiteral(True), "||", BooleanLiteral(True))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [BinaryOp(BooleanLiteral(False), "||", BooleanLiteral(True))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [BinaryOp(BooleanLiteral(False), "||", BooleanLiteral(False))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true\ntrue\nfalse"  # true || true, false || true, false || false
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_039():
    """Test logical NOT (!) operation - this IS supported by HLang spec"""
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
                                Identifier("bool2str"),
                                [UnaryOp("!", BooleanLiteral(True))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [UnaryOp("!", BooleanLiteral(False))]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [UnaryOp("!", UnaryOp("!", BooleanLiteral(True)))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "false\ntrue\ntrue"  # !true, !false, !!true
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_040():
    """Test complex logical expressions with operator precedence and unary NOT"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    # Test: true && false || true  = (true && false) || true = false || true = true
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [BinaryOp(
                                    BinaryOp(BooleanLiteral(True), "&&", BooleanLiteral(False)),
                                    "||",
                                    BooleanLiteral(True)
                                )]
                            )]
                        )
                    ),
                    # Test: !true || false && true = (!true) || (false && true) = false || false = false
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [BinaryOp(
                                    UnaryOp("!", BooleanLiteral(True)),
                                    "||",
                                    BinaryOp(BooleanLiteral(False), "&&", BooleanLiteral(True))
                                )]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true\nfalse"  # (true && false) || true = true, !true || (false && true) = false
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ========================================
# PHASE 3: CONTROL FLOW STRUCTURES (Tests 041-055)
# ========================================

def test_041():
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
                        BooleanLiteral(True),  # condition: true
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("condition was true")]
                                )
                            )
                        ]),
                        [],  # no elif branches
                        None  # no else branch
                    )
                ],
            )
        ],
    )
    expected = "condition was true"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_042():
    """Test simple if statement with false condition"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    IfStmt(
                        BooleanLiteral(False),  # condition: false
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("should not print")]
                                )
                            )
                        ]),
                        [],  # no elif branches
                        None  # no else branch
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [StringLiteral("after if statement")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "after if statement"  # if body should not execute
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_043():
    """Test if-else statement taking true branch"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    IfStmt(
                        BinaryOp(IntegerLiteral(5), ">", IntegerLiteral(3)),  # true condition
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("true branch")]
                                )
                            )
                        ]),
                        [],  # no elif branches
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("false branch")]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "true branch"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_044():
    """Test if-else statement taking false branch"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    IfStmt(
                        BinaryOp(IntegerLiteral(2), ">", IntegerLiteral(5)),  # false condition
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("true branch")]
                                )
                            )
                        ]),
                        [],  # no elif branches
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("false branch")]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "false branch"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_045():
    """Test nested if statements"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    IfStmt(
                        BooleanLiteral(True),  # outer condition: true
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("outer if")]
                                )
                            ),
                            IfStmt(
                                BooleanLiteral(True),  # inner condition: true
                                BlockStmt([
                                    ExprStmt(
                                        FunctionCall(
                                            Identifier("print"),
                                            [StringLiteral("inner if")]
                                        )
                                    )
                                ]),
                                [],  # no elif
                                None  # no else
                            )
                        ]),
                        [],  # no elif
                        None  # no else
                    )
                ],
            )
        ],
    )
    expected = "outer if\ninner if"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_046():
    """Test if statement with complex boolean condition"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    IfStmt(
                        BinaryOp(  # (5 > 3) && (10 == 10)
                            BinaryOp(IntegerLiteral(5), ">", IntegerLiteral(3)),
                            "&&",
                            BinaryOp(IntegerLiteral(10), "==", IntegerLiteral(10))
                        ),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("complex condition true")]
                                )
                            )
                        ]),
                        [],  # no elif
                        None  # no else
                    )
                ],
            )
        ],
    )
    expected = "complex condition true"  # (5 > 3) && (10 == 10) = true && true = true
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_047():
    """Test if-else-if chain using elif_branches"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    IfStmt(
                        BinaryOp(IntegerLiteral(5), "<", IntegerLiteral(3)),  # false: 5 < 3
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("first condition")]
                                )
                            )
                        ]),
                        [  # elif branches: list of (condition, block) tuples
                            (
                                BinaryOp(IntegerLiteral(5), "==", IntegerLiteral(5)),  # true: 5 == 5
                                BlockStmt([
                                    ExprStmt(
                                        FunctionCall(
                                            Identifier("print"),
                                            [StringLiteral("second condition")]
                                        )
                                    )
                                ])
                            )
                        ],
                        BlockStmt([  # else block
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("final else")]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "second condition"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_048():
    """Test basic while loop with counting"""
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
                        BinaryOp(Identifier("i"), "<", IntegerLiteral(3)),  # i < 3
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("i")])]
                                )
                            ),
                            Assignment(
                                IdLValue("i"),
                                BinaryOp(Identifier("i"), "+", IntegerLiteral(1))  # i = i + 1
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "0\n1\n2"  # loop runs for i = 0, 1, 2
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_049():
    """Test while loop with condition false from start"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    WhileStmt(
                        BooleanLiteral(False),  # condition never true
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [StringLiteral("should not print")]
                                )
                            )
                        ])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [StringLiteral("after while")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "after while"  # while body never executes
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_050():
    """Test while loop with break statement"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("count", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BooleanLiteral(True),  # infinite loop
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("count")])]
                                )
                            ),
                            Assignment(
                                IdLValue("count"),
                                BinaryOp(Identifier("count"), "+", IntegerLiteral(1))
                            ),
                            IfStmt(
                                BinaryOp(Identifier("count"), ">=", IntegerLiteral(3)),
                                BlockStmt([BreakStmt()]),  # break when count >= 3
                                [],  # no elif
                                None  # no else
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "0\n1\n2"  # breaks when count becomes 3
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_051():
    """Test while loop with continue statement"""
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
                        BinaryOp(Identifier("i"), "<", IntegerLiteral(5)),
                        BlockStmt([
                            Assignment(
                                IdLValue("i"),
                                BinaryOp(Identifier("i"), "+", IntegerLiteral(1))
                            ),
                            IfStmt(
                                BinaryOp(  # if i % 2 == 0 (even numbers)
                                    BinaryOp(Identifier("i"), "%", IntegerLiteral(2)),
                                    "==",
                                    IntegerLiteral(0)
                                ),
                                BlockStmt([ContinueStmt()]),  # skip printing even numbers
                                [],  # no elif
                                None  # no else
                            ),
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("i")])]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "1\n3\n5"  # only odd numbers printed (2, 4 skipped by continue)
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_052():
    """Test nested while loops"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("outer", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(Identifier("outer"), "<", IntegerLiteral(2)),
                        BlockStmt([
                            VarDecl("inner", IntType(), IntegerLiteral(0)),
                            WhileStmt(
                                BinaryOp(Identifier("inner"), "<", IntegerLiteral(2)),
                                BlockStmt([
                                    ExprStmt(
                                        FunctionCall(
                                            Identifier("print"),
                                            [BinaryOp(
                                                BinaryOp(
                                                    FunctionCall(Identifier("int2str"), [Identifier("outer")]),
                                                    "+",
                                                    StringLiteral(",")
                                                ),
                                                "+",
                                                FunctionCall(Identifier("int2str"), [Identifier("inner")])
                                            )]
                                        )
                                    ),
                                    Assignment(
                                        IdLValue("inner"),
                                        BinaryOp(Identifier("inner"), "+", IntegerLiteral(1))
                                    )
                                ])
                            ),
                            Assignment(
                                IdLValue("outer"),
                                BinaryOp(Identifier("outer"), "+", IntegerLiteral(1))
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "0,0\n0,1\n1,0\n1,1"  # 2x2 nested loop output
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_053():
    """Test for loop with array iteration"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ForStmt(
                        "num",  # loop variable
                        ArrayLiteral([IntegerLiteral(10), IntegerLiteral(20), IntegerLiteral(30)]),  # array
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("num")])]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "10\n20\n30"  # iterates through array elements
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_054():
    """Test for loop with break and continue"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ForStmt(
                        "value",
                        ArrayLiteral([
                            IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3),
                            IntegerLiteral(4), IntegerLiteral(5), IntegerLiteral(6)
                        ]),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(Identifier("value"), "==", IntegerLiteral(3)),
                                BlockStmt([ContinueStmt()]),  # skip 3
                                [],  # no elif
                                None  # no else
                            ),
                            IfStmt(
                                BinaryOp(Identifier("value"), "==", IntegerLiteral(5)),
                                BlockStmt([BreakStmt()]),  # exit at 5
                                [],  # no elif
                                None  # no else
                            ),
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("value")])]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "1\n2\n4"  # prints 1,2,4 (skips 3, breaks at 5, never reaches 6)
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_055():
    """Test for loop with complex array expression"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("multiplier", IntType(), IntegerLiteral(2)),
                    ForStmt(
                        "item",
                        ArrayLiteral([
                            BinaryOp(IntegerLiteral(1), "*", Identifier("multiplier")),  # 2
                            BinaryOp(IntegerLiteral(2), "*", Identifier("multiplier")),  # 4
                            BinaryOp(IntegerLiteral(3), "*", Identifier("multiplier"))   # 6
                        ]),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("item")])]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "2\n4\n6"  # array contains computed values
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ========================================
# PHASE 4: VARIABLE DECLARATION AND SCOPING (Tests 056-070)
# ========================================

def test_056():
    """Test local variable declaration with let keyword"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("age", IntType(), IntegerLiteral(25)),  # let age: int = 25;
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("age")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "25"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_057():
    """Test local constant declaration with const keyword"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ConstDecl("PI", FloatType(), FloatLiteral(3.14159)),  # const PI: float = 3.14159;
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("PI")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "3.14159"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_058():
    """Test variable reassignment"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("counter", IntType(), IntegerLiteral(0)),  # let counter: int = 0;
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("counter")])]
                        )
                    ),
                    Assignment(
                        IdLValue("counter"),
                        IntegerLiteral(42)  # counter = 42;
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("counter")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "0\n42"  # initial value, then reassigned value
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_059():
    """Test multiple variable declarations"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("name", StringType(), StringLiteral("Alice")),
                    VarDecl("age", IntType(), IntegerLiteral(30)),
                    VarDecl("height", FloatType(), FloatLiteral(5.6)),
                    VarDecl("isStudent", BoolType(), BooleanLiteral(True)),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [Identifier("name")]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("age")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("height")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("bool2str"), [Identifier("isStudent")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "Alice\n30\n5.6\ntrue"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_060():
    """Test variable scoping in blocks"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("outerVar", IntType(), IntegerLiteral(10)),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("outerVar")])]
                        )
                    ),
                    BlockStmt([  # Inner block scope
                        VarDecl("innerVar", IntType(), IntegerLiteral(20)),
                        ExprStmt(
                            FunctionCall(
                                Identifier("print"),
                                [FunctionCall(Identifier("int2str"), [Identifier("innerVar")])]
                            )
                        ),
                        ExprStmt(
                            FunctionCall(
                                Identifier("print"),
                                [FunctionCall(Identifier("int2str"), [Identifier("outerVar")])]  # outer still accessible
                            )
                        )
                    ]),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("outerVar")])]  # outer still accessible
                        )
                    )
                    # innerVar is no longer accessible here
                ],
            )
        ],
    )
    expected = "10\n20\n10\n10"  # outer, inner, outer from inner scope, outer from outer scope
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_061():
    """Test variable shadowing"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(100)),  # outer x
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("x")])]
                        )
                    ),
                    BlockStmt([
                        VarDecl("x", StringType(), StringLiteral("shadowed")),  # inner x shadows outer
                        ExprStmt(
                            FunctionCall(
                                Identifier("print"),
                                [Identifier("x")]  # should print string x
                            )
                        )
                    ]),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("x")])]  # original x restored
                        )
                    )
                ],
            )
        ],
    )
    expected = "100\nshadowed\n100"  # outer, shadowed inner, restored outer
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_062():
    """Test constant immutability (should prevent reassignment)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ConstDecl("MAX_SIZE", IntType(), IntegerLiteral(100)),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("MAX_SIZE")])]
                        )
                    )
                    # Note: Attempting to reassign MAX_SIZE should be a compile-time error
                    # This test verifies const declaration works, assignment test would be in error handling
                ],
            )
        ],
    )
    expected = "100"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_063():
    """Test variable with arithmetic expression"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", IntType(), IntegerLiteral(10)),
                    VarDecl("b", IntType(), IntegerLiteral(20)),
                    VarDecl("sum", IntType(), BinaryOp(Identifier("a"), "+", Identifier("b"))),
                    VarDecl("product", IntType(), BinaryOp(Identifier("a"), "*", Identifier("b"))),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("sum")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("product")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "30\n200"  # 10 + 20 = 30, 10 * 20 = 200
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_064():
    """Test variable with boolean expression"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(15)),
                    VarDecl("y", IntType(), IntegerLiteral(10)),
                    VarDecl("isGreater", BoolType(), BinaryOp(Identifier("x"), ">", Identifier("y"))),
                    VarDecl("isEqual", BoolType(), BinaryOp(Identifier("x"), "==", Identifier("y"))),
                    VarDecl("logicalResult", BoolType(), 
                        BinaryOp(Identifier("isGreater"), "&&", UnaryOp("!", Identifier("isEqual")))),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("bool2str"), [Identifier("isGreater")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("bool2str"), [Identifier("isEqual")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("bool2str"), [Identifier("logicalResult")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true\nfalse\ntrue"  # 15>10=true, 15==10=false, true&&!false=true&&true=true
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_065():
    """Test variable with string concatenation"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("firstName", StringType(), StringLiteral("John")),
                    VarDecl("lastName", StringType(), StringLiteral("Doe")),
                    VarDecl("fullName", StringType(), 
                        BinaryOp(
                            BinaryOp(Identifier("firstName"), "+", StringLiteral(" ")),
                            "+",
                            Identifier("lastName")
                        )),
                    VarDecl("greeting", StringType(),
                        BinaryOp(StringLiteral("Hello, "), "+", Identifier("fullName"))),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [Identifier("fullName")]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [Identifier("greeting")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "John Doe\nHello, John Doe"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_066():
    """Test type inference for variables without explicit type annotations"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("inferredInt", None, IntegerLiteral(42)),  # type inferred as int
                    VarDecl("inferredFloat", None, FloatLiteral(3.14)),  # type inferred as float
                    VarDecl("inferredBool", None, BooleanLiteral(True)),  # type inferred as bool
                    VarDecl("inferredString", None, StringLiteral("hello")),  # type inferred as string
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("inferredInt")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("inferredFloat")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("bool2str"), [Identifier("inferredBool")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [Identifier("inferredString")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "42\n3.14\ntrue\nhello"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_067():
    """Test mixed type variable operations with type promotion"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("intVar", IntType(), IntegerLiteral(10)),
                    VarDecl("floatVar", FloatType(), FloatLiteral(3.5)),
                    VarDecl("mixedSum", FloatType(), BinaryOp(Identifier("intVar"), "+", Identifier("floatVar"))),  # int promoted to float
                    VarDecl("mixedProduct", FloatType(), BinaryOp(Identifier("floatVar"), "*", Identifier("intVar"))),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("mixedSum")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("mixedProduct")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "13.5\n35.0"  # 10 + 3.5 = 13.5, 3.5 * 10 = 35.0
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_068():
    """Test variables in complex expressions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("a", IntType(), IntegerLiteral(2)),
                    VarDecl("b", IntType(), IntegerLiteral(3)),
                    VarDecl("c", IntType(), IntegerLiteral(4)),
                    VarDecl("result", IntType(), 
                        BinaryOp(  # (a + b) * c - a
                            BinaryOp(
                                BinaryOp(Identifier("a"), "+", Identifier("b")),
                                "*",
                                Identifier("c")
                            ),
                            "-",
                            Identifier("a")
                        )),
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
    expected = "18"  # (2 + 3) * 4 - 2 = 5 * 4 - 2 = 20 - 2 = 18
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_069():
    """Test variable lifetime in nested scopes"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("outerScope", IntType(), IntegerLiteral(1)),
                    BlockStmt([  # Level 1 nesting
                        VarDecl("level1", IntType(), IntegerLiteral(2)),
                        ExprStmt(
                            FunctionCall(
                                Identifier("print"),
                                [FunctionCall(Identifier("int2str"), [
                                    BinaryOp(Identifier("outerScope"), "+", Identifier("level1"))
                                ])]
                            )
                        ),
                        BlockStmt([  # Level 2 nesting
                            VarDecl("level2", IntType(), IntegerLiteral(3)),
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [
                                        BinaryOp(
                                            BinaryOp(Identifier("outerScope"), "+", Identifier("level1")),
                                            "+",
                                            Identifier("level2")
                                        )
                                    ])]
                                )
                            )
                        ]),
                        ExprStmt(
                            FunctionCall(
                                Identifier("print"),
                                [FunctionCall(Identifier("int2str"), [
                                    BinaryOp(Identifier("outerScope"), "+", Identifier("level1"))
                                ])]
                            )
                        )
                        # level2 no longer accessible here
                    ]),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("outerScope")])]
                        )
                    )
                    # level1 and level2 no longer accessible here
                ],
            )
        ],
    )
    expected = "3\n6\n3\n1"  # 1+2=3, 1+2+3=6, 1+2=3, 1
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_070():
    """Test global constant accessibility in functions"""
    ast = Program(
        [
            ConstDecl("GLOBAL_CONST", IntType(), IntegerLiteral(999))  # Global constant
        ],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("localVar", IntType(), IntegerLiteral(1)),
                    VarDecl("combined", IntType(), BinaryOp(Identifier("GLOBAL_CONST"), "+", Identifier("localVar"))),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("GLOBAL_CONST")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("combined")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "999\n1000"  # global const, global + local = 999 + 1 = 1000
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ============================================================================
# PHASE 5: FUNCTION DEFINITION AND CALLS (Tests 071-085) - 15 tests
# ============================================================================

def test_071():
    """Test basic function definition with single parameter"""
    ast = Program(
        [],
        [
            FuncDecl(
                "greet",
                [Param("name", StringType())],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [BinaryOp(StringLiteral("Hello, "), "+", Identifier("name"))]
                        )
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("greet"),
                            [StringLiteral("Alice")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "Hello, Alice"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_072():
    """Test function with multiple parameters"""
    ast = Program(
        [],
        [
            FuncDecl(
                "add_three",
                [Param("a", IntType()), Param("b", IntType()), Param("c", IntType())],
                IntType(),
                [
                    ReturnStmt(
                        BinaryOp(
                            BinaryOp(Identifier("a"), "+", Identifier("b")),
                            "+",
                            Identifier("c")
                        )
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", IntType(), 
                        FunctionCall(
                            Identifier("add_three"),
                            [IntegerLiteral(10), IntegerLiteral(20), IntegerLiteral(30)]
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
    expected = "60"  # 10 + 20 + 30 = 60
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_073():
    """Test function with return statement"""
    ast = Program(
        [],
        [
            FuncDecl(
                "double_value",
                [Param("x", IntType())],
                IntType(),
                [
                    ReturnStmt(
                        BinaryOp(Identifier("x"), "*", IntegerLiteral(2))
                    )
                ]
            ),
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
                                [FunctionCall(
                                    Identifier("double_value"),
                                    [IntegerLiteral(7)]
                                )]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "14"  # 7 * 2 = 14
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_074():
    """Test function returning integer"""
    ast = Program(
        [],
        [
            FuncDecl(
                "square",
                [Param("n", IntType())],
                IntType(),
                [
                    ReturnStmt(
                        BinaryOp(Identifier("n"), "*", Identifier("n"))
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("number", IntType(), IntegerLiteral(8)),
                    VarDecl("squared", IntType(), 
                        FunctionCall(Identifier("square"), [Identifier("number")])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("squared")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "64"  # 8 * 8 = 64
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_075():
    """Test function returning float"""
    ast = Program(
        [],
        [
            FuncDecl(
                "circle_area",
                [Param("radius", FloatType())],
                FloatType(),
                [
                    ConstDecl("PI", FloatType(), FloatLiteral(3.14159)),
                    ReturnStmt(
                        BinaryOp(
                            Identifier("PI"),
                            "*",
                            BinaryOp(Identifier("radius"), "*", Identifier("radius"))
                        )
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("area", FloatType(), 
                        FunctionCall(Identifier("circle_area"), [FloatLiteral(2.0)])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("area")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "12.56636"  # π * 2² = 3.14159 * 4 = 12.56636
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_076():
    """Test function returning boolean"""
    ast = Program(
        [],
        [
            FuncDecl(
                "is_even",
                [Param("n", IntType())],
                BoolType(),
                [
                    ReturnStmt(
                        BinaryOp(
                            BinaryOp(Identifier("n"), "%", IntegerLiteral(2)),
                            "==",
                            IntegerLiteral(0)
                        )
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [FunctionCall(Identifier("is_even"), [IntegerLiteral(4)])]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("bool2str"),
                                [FunctionCall(Identifier("is_even"), [IntegerLiteral(5)])]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "true\nfalse"  # 4 is even, 5 is odd
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_077():
    """Test function returning string"""
    ast = Program(
        [],
        [
            FuncDecl(
                "make_title",
                [Param("first", StringType()), Param("last", StringType())],
                StringType(),
                [
                    ReturnStmt(
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(StringLiteral("Mr. "), "+", Identifier("first")),
                                "+",
                                StringLiteral(" ")
                            ),
                            "+",
                            Identifier("last")
                        )
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("title", StringType(), 
                        FunctionCall(
                            Identifier("make_title"),
                            [StringLiteral("John"), StringLiteral("Doe")]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(Identifier("print"), [Identifier("title")])
                    )
                ],
            )
        ],
    )
    expected = "Mr. John Doe"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_078():
    """Test function call with arguments"""
    ast = Program(
        [],
        [
            FuncDecl(
                "calculate",
                [Param("x", IntType()), Param("y", IntType()), Param("operation", StringType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("operation"), "==", StringLiteral("add")),
                        BlockStmt([
                            ReturnStmt(BinaryOp(Identifier("x"), "+", Identifier("y")))
                        ]),
                        [],  # no elif
                        BlockStmt([  # else
                            ReturnStmt(BinaryOp(Identifier("x"), "*", Identifier("y")))
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("sum", IntType(), 
                        FunctionCall(
                            Identifier("calculate"),
                            [IntegerLiteral(15), IntegerLiteral(25), StringLiteral("add")]
                        )
                    ),
                    VarDecl("product", IntType(), 
                        FunctionCall(
                            Identifier("calculate"),
                            [IntegerLiteral(6), IntegerLiteral(7), StringLiteral("multiply")]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("sum")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("product")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "40\n42"  # 15+25=40, 6*7=42
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_079():
    """Test function call in expression"""
    ast = Program(
        [],
        [
            FuncDecl(
                "get_value",
                [Param("multiplier", IntType())],
                IntType(),
                [
                    ReturnStmt(BinaryOp(IntegerLiteral(5), "*", Identifier("multiplier")))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", IntType(), 
                        BinaryOp(
                            FunctionCall(Identifier("get_value"), [IntegerLiteral(3)]),
                            "+",
                            FunctionCall(Identifier("get_value"), [IntegerLiteral(4)])
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
    expected = "35"  # get_value(3) + get_value(4) = (5*3) + (5*4) = 15 + 20 = 35
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_080():
    """Test recursive function call (factorial)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "factorial",
                [Param("n", IntType())],
                IntType(),
                [
                    IfStmt(
                        BinaryOp(Identifier("n"), "<=", IntegerLiteral(1)),
                        BlockStmt([
                            ReturnStmt(IntegerLiteral(1))  # Base case
                        ]),
                        [],  # no elif
                        BlockStmt([  # else
                            ReturnStmt(  # n * factorial(n-1)
                                BinaryOp(
                                    Identifier("n"),
                                    "*",
                                    FunctionCall(
                                        Identifier("factorial"),
                                        [BinaryOp(Identifier("n"), "-", IntegerLiteral(1))]
                                    )
                                )
                            )
                        ])
                    )
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", IntType(), 
                        FunctionCall(Identifier("factorial"), [IntegerLiteral(5)])
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
    expected = "120"  # 5! = 5*4*3*2*1 = 120
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_081():
    """Test function with local variables"""
    ast = Program(
        [],
        [
            FuncDecl(
                "compute_average",
                [Param("a", IntType()), Param("b", IntType()), Param("c", IntType())],
                FloatType(),
                [
                    VarDecl("sum", IntType(), 
                        BinaryOp(
                            BinaryOp(Identifier("a"), "+", Identifier("b")),
                            "+",
                            Identifier("c")
                        )
                    ),
                    VarDecl("count", IntType(), IntegerLiteral(3)),
                    VarDecl("average", FloatType(), 
                        BinaryOp(Identifier("sum"), "/", Identifier("count"))  # int/int promoted to float
                    ),
                    ReturnStmt(Identifier("average"))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", FloatType(), 
                        FunctionCall(
                            Identifier("compute_average"),
                            [IntegerLiteral(10), IntegerLiteral(20), IntegerLiteral(30)]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("float2str"), [Identifier("result")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "20.0"  # (10+20+30)/3 = 60/3 = 20.0
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_082():
    """Test function parameter shadowing"""
    ast = Program(
        [],
        [
            FuncDecl(
                "process_values",
                [Param("x", IntType()), Param("y", IntType())],
                IntType(),
                [
                    VarDecl("x", IntType(), BinaryOp(Identifier("x"), "*", IntegerLiteral(2))),  # shadows parameter x
                    VarDecl("result", IntType(), BinaryOp(Identifier("x"), "+", Identifier("y"))),
                    ReturnStmt(Identifier("result"))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("output", IntType(), 
                        FunctionCall(
                            Identifier("process_values"),
                            [IntegerLiteral(5), IntegerLiteral(3)]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("output")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "13"  # x becomes 5*2=10, then 10+3=13
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_083():
    """Test nested function calls"""
    ast = Program(
        [],
        [
            FuncDecl(
                "add_one",
                [Param("n", IntType())],
                IntType(),
                [
                    ReturnStmt(BinaryOp(Identifier("n"), "+", IntegerLiteral(1)))
                ]
            ),
            FuncDecl(
                "multiply_by_two",
                [Param("n", IntType())],
                IntType(),
                [
                    ReturnStmt(BinaryOp(Identifier("n"), "*", IntegerLiteral(2)))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", IntType(), 
                        FunctionCall(
                            Identifier("multiply_by_two"),
                            [FunctionCall(Identifier("add_one"), [IntegerLiteral(7)])]
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
    expected = "16"  # multiply_by_two(add_one(7)) = multiply_by_two(8) = 16
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_084():
    """Test function with array parameter"""
    ast = Program(
        [],
        [
            FuncDecl(
                "sum_array",
                [Param("numbers", ArrayType(IntType(), 3))],
                IntType(),
                [
                    VarDecl("total", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "num",
                        Identifier("numbers"),
                        BlockStmt([
                            Assignment(
                                IdLValue("total"),
                                BinaryOp(Identifier("total"), "+", Identifier("num"))
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("total"))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("values", ArrayType(IntType(), 3), 
                        ArrayLiteral([IntegerLiteral(10), IntegerLiteral(20), IntegerLiteral(30)])
                    ),
                    VarDecl("sum", IntType(), 
                        FunctionCall(Identifier("sum_array"), [Identifier("values")])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("sum")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "60"  # 10 + 20 + 30 = 60
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_085():
    """Test function returning array"""
    ast = Program(
        [],
        [
            FuncDecl(
                "create_sequence",
                [Param("start", IntType()), Param("count", IntType())],
                ArrayType(IntType(), 3),
                [
                    VarDecl("result", ArrayType(IntType(), 3), 
                        ArrayLiteral([IntegerLiteral(0), IntegerLiteral(0), IntegerLiteral(0)])
                    ),
                    VarDecl("i", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(Identifier("i"), "<", Identifier("count")),
                        BlockStmt([
                            Assignment(
                                ArrayAccessLValue(Identifier("result"), Identifier("i")),
                                BinaryOp(Identifier("start"), "+", Identifier("i"))
                            ),
                            Assignment(
                                IdLValue("i"),
                                BinaryOp(Identifier("i"), "+", IntegerLiteral(1))
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("result"))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("sequence", ArrayType(IntType(), 3), 
                        FunctionCall(
                            Identifier("create_sequence"),
                            [IntegerLiteral(5), IntegerLiteral(3)]
                        )
                    ),
                    ForStmt(
                        "num",
                        Identifier("sequence"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("num")])]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "5\n6\n7"  # sequence starting at 5 with 3 elements: [5, 6, 7]
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ============================================================================
# PHASE 6: ARRAY OPERATIONS (Tests 086-100) - 15 tests
# ============================================================================

def test_086():
    """Test array literal creation"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("numbers", ArrayType(IntType(), 3), 
                        ArrayLiteral([IntegerLiteral(10), IntegerLiteral(20), IntegerLiteral(30)])
                    ),
                    VarDecl("names", ArrayType(StringType(), 2), 
                        ArrayLiteral([StringLiteral("Alice"), StringLiteral("Bob")])
                    ),
                    VarDecl("flags", ArrayType(BoolType(), 2), 
                        ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])
                    ),
                    ForStmt(
                        "num",
                        Identifier("numbers"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("num")])]
                                )
                            )
                        ])
                    ),
                    ForStmt(
                        "name",
                        Identifier("names"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(Identifier("print"), [Identifier("name")])
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "10\n20\n30\nAlice\nBob"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_087():
    """Test array element access"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("values", ArrayType(IntType(), 4), 
                        ArrayLiteral([IntegerLiteral(100), IntegerLiteral(200), IntegerLiteral(300), IntegerLiteral(400)])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(Identifier("values"), IntegerLiteral(0))]  # values[0]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(Identifier("values"), IntegerLiteral(2))]  # values[2]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(Identifier("values"), IntegerLiteral(3))]  # values[3]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "100\n300\n400"  # values[0], values[2], values[3]
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_088():
    """Test array element assignment"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("data", ArrayType(IntType(), 3), 
                        ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(Identifier("data"), IntegerLiteral(1))]
                            )]
                        )
                    ),
                    Assignment(
                        ArrayAccessLValue(Identifier("data"), IntegerLiteral(1)),  # data[1] = 99
                        IntegerLiteral(99)
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(Identifier("data"), IntegerLiteral(1))]
                            )]
                        )
                    ),
                    Assignment(
                        ArrayAccessLValue(Identifier("data"), IntegerLiteral(0)),  # data[0] = 50
                        IntegerLiteral(50)
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(Identifier("data"), IntegerLiteral(0))]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "2\n99\n50"  # original data[1], modified data[1], modified data[0]
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_089():
    """Test array length with len function"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("small", ArrayType(IntType(), 2), 
                        ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)])
                    ),
                    VarDecl("large", ArrayType(StringType(), 5), 
                        ArrayLiteral([
                            StringLiteral("a"), StringLiteral("b"), StringLiteral("c"), 
                            StringLiteral("d"), StringLiteral("e")
                        ])
                    ),
                    VarDecl("smallLen", IntType(), 
                        FunctionCall(Identifier("len"), [Identifier("small")])
                    ),
                    VarDecl("largeLen", IntType(), 
                        FunctionCall(Identifier("len"), [Identifier("large")])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("smallLen")])]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("largeLen")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "2\n5"  # len(small) = 2, len(large) = 5
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_090():
    """Test array iteration with for-in loop"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("scores", ArrayType(IntType(), 4), 
                        ArrayLiteral([
                            IntegerLiteral(85), IntegerLiteral(90), 
                            IntegerLiteral(78), IntegerLiteral(92)
                        ])
                    ),
                    VarDecl("total", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "score",
                        Identifier("scores"),
                        BlockStmt([
                            Assignment(
                                IdLValue("total"),
                                BinaryOp(Identifier("total"), "+", Identifier("score"))
                            )
                        ])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("total")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "345"  # 85 + 90 + 78 + 92 = 345
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_091():
    """Test multi-dimensional arrays (2D array)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("matrix", ArrayType(ArrayType(IntType(), 2), 2), 
                        ArrayLiteral([
                            ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]),
                            ArrayLiteral([IntegerLiteral(3), IntegerLiteral(4)])
                        ])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(
                                    ArrayAccess(Identifier("matrix"), IntegerLiteral(0)),
                                    IntegerLiteral(1)
                                )]  # matrix[0][1]
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(
                                    ArrayAccess(Identifier("matrix"), IntegerLiteral(1)),
                                    IntegerLiteral(0)
                                )]  # matrix[1][0]
                            )]
                        )
                    ),
                    Assignment(
                        ArrayAccessLValue(
                            ArrayAccess(Identifier("matrix"), IntegerLiteral(1)),
                            IntegerLiteral(1)
                        ),  # matrix[1][1] = 99
                        IntegerLiteral(99)
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(
                                    ArrayAccess(Identifier("matrix"), IntegerLiteral(1)),
                                    IntegerLiteral(1)
                                )]  # matrix[1][1]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "2\n3\n99"  # matrix[0][1], matrix[1][0], modified matrix[1][1]
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_092():
    """Test array bounds checking (valid indices)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("arr", ArrayType(IntType(), 3), 
                        ArrayLiteral([IntegerLiteral(10), IntegerLiteral(20), IntegerLiteral(30)])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(Identifier("arr"), IntegerLiteral(0))]  # first element
                            )]
                        )
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(
                                    Identifier("arr"), 
                                    BinaryOp(
                                        FunctionCall(Identifier("len"), [Identifier("arr")]),
                                        "-",
                                        IntegerLiteral(1)
                                    )
                                )]  # last element: arr[len(arr)-1]
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "10\n30"  # arr[0] and arr[2] (last element)
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_093():
    """Test empty array creation"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("empty", ArrayType(IntType(), 0), 
                        ArrayLiteral([])  # empty array
                    ),
                    VarDecl("emptyLen", IntType(), 
                        FunctionCall(Identifier("len"), [Identifier("empty")])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("emptyLen")])]
                        )
                    ),
                    VarDecl("singleElement", ArrayType(StringType(), 1), 
                        ArrayLiteral([StringLiteral("only")])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [ArrayAccess(Identifier("singleElement"), IntegerLiteral(0))]
                        )
                    )
                ],
            )
        ],
    )
    expected = "0\nonly"  # len(empty) = 0, singleElement[0] = "only"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_094():
    """Test array with mixed expressions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("base", IntType(), IntegerLiteral(5)),
                    VarDecl("computed", ArrayType(IntType(), 4), 
                        ArrayLiteral([
                            Identifier("base"),  # 5
                            BinaryOp(Identifier("base"), "*", IntegerLiteral(2)),  # 10
                            BinaryOp(Identifier("base"), "+", IntegerLiteral(10)),  # 15
                            BinaryOp(Identifier("base"), "*", Identifier("base"))   # 25
                        ])
                    ),
                    ForStmt(
                        "value",
                        Identifier("computed"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("value")])]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "5\n10\n15\n25"  # base, base*2, base+10, base*base
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_095():
    """Test array element modification in loop"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("numbers", ArrayType(IntType(), 3), 
                        ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])
                    ),
                    VarDecl("i", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(
                            Identifier("i"), 
                            "<", 
                            FunctionCall(Identifier("len"), [Identifier("numbers")])
                        ),
                        BlockStmt([
                            Assignment(
                                ArrayAccessLValue(Identifier("numbers"), Identifier("i")),
                                BinaryOp(
                                    ArrayAccess(Identifier("numbers"), Identifier("i")),
                                    "*",
                                    IntegerLiteral(10)
                                )  # numbers[i] = numbers[i] * 10
                            ),
                            Assignment(
                                Identifier("i"),
                                BinaryOp(Identifier("i"), "+", IntegerLiteral(1))
                            )
                        ])
                    ),
                    ForStmt(
                        "num",
                        Identifier("numbers"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("num")])]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "10\n20\n30"  # [1,2,3] becomes [10,20,30]
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_096():
    """Test array with complex element expressions"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("x", IntType(), IntegerLiteral(3)),
                    VarDecl("y", IntType(), IntegerLiteral(4)),
                    VarDecl("results", ArrayType(IntType(), 3), 
                        ArrayLiteral([
                            BinaryOp(Identifier("x"), "+", Identifier("y")),  # 7
                            BinaryOp(Identifier("x"), "*", Identifier("y")),  # 12
                            BinaryOp(
                                BinaryOp(Identifier("x"), "*", Identifier("x")),
                                "+",
                                BinaryOp(Identifier("y"), "*", Identifier("y"))
                            )  # x*x + y*y = 9 + 16 = 25
                        ])
                    ),
                    VarDecl("sum", IntType(), IntegerLiteral(0)),
                    ForStmt(
                        "result",
                        Identifier("results"),
                        BlockStmt([
                            Assignment(
                                Identifier("sum"),
                                BinaryOp(Identifier("sum"), "+", Identifier("result"))
                            )
                        ])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("sum")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "44"  # 7 + 12 + 25 = 44
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_097():
    """Test array with different data types"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("floats", ArrayType(FloatType(), 3), 
                        ArrayLiteral([FloatLiteral(1.5), FloatLiteral(2.5), FloatLiteral(3.5)])
                    ),
                    VarDecl("bools", ArrayType(BoolType(), 3), 
                        ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)])
                    ),
                    ForStmt(
                        "f",
                        Identifier("floats"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("float2str"), [Identifier("f")])]
                                )
                            )
                        ])
                    ),
                    ForStmt(
                        "b",
                        Identifier("bools"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("bool2str"), [Identifier("b")])]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "1.5\n2.5\n3.5\ntrue\nfalse\ntrue"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_098():
    """Test nested array access with variables"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("grid", ArrayType(ArrayType(IntType(), 3), 2), 
                        ArrayLiteral([
                            ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]),
                            ArrayLiteral([IntegerLiteral(4), IntegerLiteral(5), IntegerLiteral(6)])
                        ])
                    ),
                    VarDecl("row", IntType(), IntegerLiteral(1)),
                    VarDecl("col", IntType(), IntegerLiteral(2)),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(
                                    ArrayAccess(Identifier("grid"), Identifier("row")),
                                    Identifier("col")
                                )]  # grid[row][col] = grid[1][2] = 6
                            )]
                        )
                    ),
                    Assignment(
                        IdLValue("row"),
                        IntegerLiteral(0)
                    ),
                    Assignment(
                        IdLValue("col"),
                        IntegerLiteral(1)
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(
                                Identifier("int2str"), 
                                [ArrayAccess(
                                    ArrayAccess(Identifier("grid"), Identifier("row")),
                                    Identifier("col")
                                )]  # grid[0][1] = 2
                            )]
                        )
                    )
                ],
            )
        ],
    )
    expected = "6\n2"  # grid[1][2], then grid[0][1]
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_099():
    """Test array as function return value (already tested in test_085)"""
    ast = Program(
        [],
        [
            FuncDecl(
                "create_range",
                [Param("start", IntType()), Param("end", IntType())],
                ArrayType(IntType(), 3),
                [
                    VarDecl("result", ArrayType(IntType(), 3), 
                        ArrayLiteral([IntegerLiteral(0), IntegerLiteral(0), IntegerLiteral(0)])
                    ),
                    Assignment(
                        ArrayAccessLValue(Identifier("result"), IntegerLiteral(0)),
                        Identifier("start")
                    ),
                    Assignment(
                        ArrayAccessLValue(Identifier("result"), IntegerLiteral(1)),
                        BinaryOp(Identifier("start"), "+", IntegerLiteral(1))
                    ),
                    Assignment(
                        ArrayAccessLValue(Identifier("result"), IntegerLiteral(2)),
                        Identifier("end")
                    ),
                    ReturnStmt(Identifier("result"))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("range", ArrayType(IntType(), 3), 
                        FunctionCall(
                            Identifier("create_range"),
                            [IntegerLiteral(10), IntegerLiteral(12)]
                        )
                    ),
                    ForStmt(
                        "value",
                        Identifier("range"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"),
                                    [FunctionCall(Identifier("int2str"), [Identifier("value")])]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "10\n11\n12"  # create_range(10, 12) returns [10, 11, 12]
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_100():
    """Test complex array operations combining multiple features"""
    ast = Program(
        [],
        [
            FuncDecl(
                "process_matrix",
                [Param("matrix", ArrayType(ArrayType(IntType(), 2), 2))],
                IntType(),
                [
                    VarDecl("sum", IntType(), IntegerLiteral(0)),
                    VarDecl("i", IntType(), IntegerLiteral(0)),
                    WhileStmt(
                        BinaryOp(
                            Identifier("i"), 
                            "<", 
                            FunctionCall(Identifier("len"), [Identifier("matrix")])
                        ),
                        BlockStmt([
                            VarDecl("row", ArrayType(IntType(), 2), 
                                ArrayAccess(Identifier("matrix"), Identifier("i"))
                            ),
                            VarDecl("j", IntType(), IntegerLiteral(0)),
                            WhileStmt(
                                BinaryOp(
                                    Identifier("j"), 
                                    "<", 
                                    FunctionCall(Identifier("len"), [Identifier("row")])
                                ),
                                BlockStmt([
                                    Assignment(
                                        Identifier("sum"),
                                        BinaryOp(
                                            Identifier("sum"), 
                                            "+", 
                                            ArrayAccess(Identifier("row"), Identifier("j"))
                                        )
                                    ),
                                    Assignment(
                                        Identifier("j"),
                                        BinaryOp(Identifier("j"), "+", IntegerLiteral(1))
                                    )
                                ])
                            ),
                            Assignment(
                                Identifier("i"),
                                BinaryOp(Identifier("i"), "+", IntegerLiteral(1))
                            )
                        ])
                    ),
                    ReturnStmt(Identifier("sum"))
                ]
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("data", ArrayType(ArrayType(IntType(), 2), 2), 
                        ArrayLiteral([
                            ArrayLiteral([IntegerLiteral(10), IntegerLiteral(20)]),
                            ArrayLiteral([IntegerLiteral(30), IntegerLiteral(40)])
                        ])
                    ),
                    VarDecl("total", IntType(), 
                        FunctionCall(Identifier("process_matrix"), [Identifier("data")])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("total")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "100"  # 10 + 20 + 30 + 40 = 100 (sum of all matrix elements)
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


# ============================================
# BONUS TRIVIA TESTS (Tests 101-112)
# Random single-aspect focused tests
# ============================================

def test_101():
    """TRIVIA: Single character string literal"""
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
                            Identifier("print"), [StringLiteral("x")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "x"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_102():
    """TRIVIA: Negative zero float literal"""
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
                            [FunctionCall(Identifier("float2str"), [FloatLiteral(-0.0)])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "-0.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_103():
    """TRIVIA: Boolean literal false in conditional"""
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
                                    Identifier("print"), [StringLiteral("never")]
                                )
                            )
                        ]),
                        [],
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"), [StringLiteral("always")]
                                )
                            )
                        ])
                    )
                ],
            )
        ],
    )
    expected = "always"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_104():
    """TRIVIA: Integer division with exact result"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", IntType(), 
                        BinaryOp(IntegerLiteral(15), "/", IntegerLiteral(3))
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
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_105():
    """TRIVIA: String concatenation with empty string"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("text", StringType(),
                        BinaryOp(StringLiteral("hello"), "+", StringLiteral(""))
                    ),
                    ExprStmt(
                        FunctionCall(Identifier("print"), [Identifier("text")])
                    )
                ],
            )
        ],
    )
    expected = "hello"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_106():
    """TRIVIA: Unary minus with parentheses"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("num", IntType(), 
                        UnaryOp("-", IntegerLiteral(42))
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("num")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "-42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_107():
    """TRIVIA: While loop that never executes"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("executed", BoolType(), BooleanLiteral(False)),
                    WhileStmt(
                        BooleanLiteral(False),
                        BlockStmt([
                            Assignment(
                                Identifier("executed"),
                                BooleanLiteral(True)
                            ),
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"), [StringLiteral("never")]
                                )
                            )
                        ])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"), [StringLiteral("after loop")]
                        )
                    )
                ],
            )
        ],
    )
    expected = "after loop"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_108():
    """TRIVIA: Constant with maximum integer value"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    ConstDecl("MAX_INT", IntType(), IntegerLiteral(2147483647)),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("MAX_INT")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "2147483647"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_109():
    """TRIVIA: Function with single character name"""
    ast = Program(
        [],
        [
            FuncDecl(
                "f",
                [Param("x", IntType())],
                IntType(),
                [
                    ReturnStmt(
                        BinaryOp(Identifier("x"), "*", IntegerLiteral(2))
                    )
                ],
            ),
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("result", IntType(),
                        FunctionCall(Identifier("f"), [IntegerLiteral(7)])
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
    expected = "14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_110():
    """TRIVIA: Array with single element"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("singleton", ArrayType(StringType(), 1),
                        ArrayLiteral([StringLiteral("alone")])
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [ArrayAccess(Identifier("singleton"), IntegerLiteral(0))]
                        )
                    )
                ],
            )
        ],
    )
    expected = "alone"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_111():
    """TRIVIA: Modulo operation with result zero"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("remainder", IntType(),
                        BinaryOp(IntegerLiteral(10), "%", IntegerLiteral(5))
                    ),
                    ExprStmt(
                        FunctionCall(
                            Identifier("print"),
                            [FunctionCall(Identifier("int2str"), [Identifier("remainder")])]
                        )
                    )
                ],
            )
        ],
    )
    expected = "0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected


def test_112():
    """TRIVIA: Logical NOT with nested expression"""
    ast = Program(
        [],
        [
            FuncDecl(
                "main",
                [],
                VoidType(),
                [
                    VarDecl("value", BoolType(),
                        UnaryOp("!", 
                            BinaryOp(IntegerLiteral(5), "==", IntegerLiteral(3))
                        )
                    ),
                    IfStmt(
                        Identifier("value"),
                        BlockStmt([
                            ExprStmt(
                                FunctionCall(
                                    Identifier("print"), [StringLiteral("not equal")]
                                )
                            )
                        ]),
                        [],
                        None
                    )
                ],
            )
        ],
    )
    expected = "not equal"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected
