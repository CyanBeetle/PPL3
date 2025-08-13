from utils import ASTGenerator


def test_001():
    """Test basic constant declaration AST generation"""
    source = "const x: int = 42;"
    expected = "Program(consts=[ConstDecl(x, int, IntegerLiteral(42))])"
    # Just check that it doesn't return an error
    assert str(ASTGenerator(source).generate()) == expected


def test_002():
    """Test function declaration AST generation"""
    source = "func main() -> void {}"
    expected = "Program(funcs=[FuncDecl(main, [], void, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_003():
    """Test function with parameters AST generation"""
    source = "func add(a: int, b: int) -> int { return a + b; }"
    expected = "Program(funcs=[FuncDecl(add, [Param(a, int), Param(b, int)], int, [ReturnStmt(BinaryOp(Identifier(a), +, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_004():
    """Test multiple declarations AST generation"""
    source = """const PI: float = 3.14;
    func square(x: int) -> int { return x * x; }"""
    expected = "Program(consts=[ConstDecl(PI, float, FloatLiteral(3.14))], funcs=[FuncDecl(square, [Param(x, int)], int, [ReturnStmt(BinaryOp(Identifier(x), *, Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_005():
    """Test variable declaration with type inference"""
    source = """func main() -> void { let name = "Alice"; }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(name, StringLiteral('Alice'))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_006():
    """Test if-else statement AST generation"""
    source = """func main() -> void { 
        if (x > 0) { 
            return x;
        } else { 
            return 0;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(Identifier(x))]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(0))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_007():
    """Test while loop AST generation"""
    source = """func main() -> void { 
        while (i < 10) { 
            i = i + 1; 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(10)), BlockStmt([Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_008():
    """Test array operations AST generation"""
    source = """func main() -> void { 
        let arr = [1, 2, 3];
        let first = arr[0];
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])), VarDecl(first, ArrayAccess(Identifier(arr), IntegerLiteral(0)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_009():
    """Test pipeline operator AST generation"""
    source = """func main() -> void { 
        let result = data >> process;
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(Identifier(data), >>, Identifier(process)))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# Constants and Basic Declarations (test_010 - test_019)
# ============================================================================

def test_010():
    """Test constant declaration without type annotation"""
    source = "const x = 42;"
    expected = "Program(consts=[ConstDecl(x, IntegerLiteral(42))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_011():
    """Test float constant declaration"""
    source = "const PI: float = 3.14159;"
    expected = "Program(consts=[ConstDecl(PI, float, FloatLiteral(3.14159))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_012():
    """Test boolean constant declaration"""
    source = "const DEBUG: bool = true;"
    expected = "Program(consts=[ConstDecl(DEBUG, bool, BooleanLiteral(True))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_013():
    """Test string constant declaration"""
    source = "const MESSAGE: string = \"Hello World\";"
    expected = "Program(consts=[ConstDecl(MESSAGE, string, StringLiteral('Hello World'))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_014():
    """Test multiple constant declarations"""
    source = """const A = 1;
    const B = 2;
    const C = 3;"""
    expected = "Program(consts=[ConstDecl(A, IntegerLiteral(1)), ConstDecl(B, IntegerLiteral(2)), ConstDecl(C, IntegerLiteral(3))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_015():
    """Test constant with negative value"""
    source = "const NEG: int = -42;"
    expected = "Program(consts=[ConstDecl(NEG, int, UnaryOp(-, IntegerLiteral(42)))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_016():
    """Test constant with expression"""
    source = "const SUM = 10 + 5;"
    expected = "Program(consts=[ConstDecl(SUM, BinaryOp(IntegerLiteral(10), +, IntegerLiteral(5)))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_017():
    """Test constant with boolean expression"""
    source = "const RESULT = true && false;"
    expected = "Program(consts=[ConstDecl(RESULT, BinaryOp(BooleanLiteral(True), &&, BooleanLiteral(False)))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_018():
    """Test constant with string concatenation"""
    source = "const GREETING = \"Hello\" + \" World\";"
    expected = "Program(consts=[ConstDecl(GREETING, BinaryOp(StringLiteral('Hello'), +, StringLiteral(' World')))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_019():
    """Test constant with float expression"""
    source = "const AREA = 3.14 * 2.5;"
    expected = "Program(consts=[ConstDecl(AREA, BinaryOp(FloatLiteral(3.14), *, FloatLiteral(2.5)))])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# Function Declarations (test_020 - test_029)
# ============================================================================

def test_020():
    """Test function with single parameter"""
    source = "func square(x: int) -> int { return x * x; }"
    expected = "Program(funcs=[FuncDecl(square, [Param(x, int)], int, [ReturnStmt(BinaryOp(Identifier(x), *, Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_021():
    """Test function with multiple parameters"""
    source = "func add(a: int, b: int, c: int) -> int { return a + b + c; }"
    expected = "Program(funcs=[FuncDecl(add, [Param(a, int), Param(b, int), Param(c, int)], int, [ReturnStmt(BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), +, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_022():
    """Test void function"""
    source = "func print_hello() -> void { return; }"
    expected = "Program(funcs=[FuncDecl(print_hello, [], void, [ReturnStmt()])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_023():
    """Test function with bool parameter"""
    source = "func toggle(flag: bool) -> bool { return !flag; }"
    expected = "Program(funcs=[FuncDecl(toggle, [Param(flag, bool)], bool, [ReturnStmt(UnaryOp(!, Identifier(flag)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_024():
    """Test function with string parameter"""
    source = "func greet(name: string) -> string { return \"Hello \" + name; }"
    expected = "Program(funcs=[FuncDecl(greet, [Param(name, string)], string, [ReturnStmt(BinaryOp(StringLiteral('Hello '), +, Identifier(name)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_025():
    """Test function with float parameter"""
    source = "func circle_area(radius: float) -> float { return 3.14 * radius * radius; }"
    expected = "Program(funcs=[FuncDecl(circle_area, [Param(radius, float)], float, [ReturnStmt(BinaryOp(BinaryOp(FloatLiteral(3.14), *, Identifier(radius)), *, Identifier(radius)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_026():
    """Test function with mixed parameter types"""
    source = "func format_number(value: int, precision: int, show_sign: bool) -> string { return \"formatted\"; }"
    expected = "Program(funcs=[FuncDecl(format_number, [Param(value, int), Param(precision, int), Param(show_sign, bool)], string, [ReturnStmt(StringLiteral('formatted'))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_027():
    """Test function with array parameter"""
    source = "func sum_array(arr: [int; 5]) -> int { return 0; }"
    expected = "Program(funcs=[FuncDecl(sum_array, [Param(arr, [int; 5])], int, [ReturnStmt(IntegerLiteral(0))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_028():
    """Test function with multiple statements"""
    source = """func complex_func() -> int { 
        let x = 10;
        let y = 20;
        return x + y;
    }"""
    expected = "Program(funcs=[FuncDecl(complex_func, [], int, [VarDecl(x, IntegerLiteral(10)), VarDecl(y, IntegerLiteral(20)), ReturnStmt(BinaryOp(Identifier(x), +, Identifier(y)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_029():
    """Test function with empty body"""
    source = "func empty_func() -> void {}"
    expected = "Program(funcs=[FuncDecl(empty_func, [], void, [])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# Variable Declarations (test_030 - test_039)
# ============================================================================

def test_030():
    """Test variable declaration with explicit type"""
    source = "func main() -> void { let x: int = 42; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, int, IntegerLiteral(42))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_031():
    """Test variable declaration with type inference"""
    source = "func main() -> void { let x = 42; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(x, IntegerLiteral(42))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_032():
    """Test string variable declaration"""
    source = "func main() -> void { let name: string = \"Alice\"; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(name, string, StringLiteral('Alice'))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_033():
    """Test boolean variable declaration"""
    source = "func main() -> void { let flag: bool = true; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(flag, bool, BooleanLiteral(True))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_034():
    """Test float variable declaration"""
    source = "func main() -> void { let pi: float = 3.14; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(pi, float, FloatLiteral(3.14))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_035():
    """Test multiple variable declarations"""
    source = """func main() -> void { 
        let a = 1;
        let b = 2;
        let c = 3;
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(a, IntegerLiteral(1)), VarDecl(b, IntegerLiteral(2)), VarDecl(c, IntegerLiteral(3))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_036():
    """Test variable with expression initialization"""
    source = "func main() -> void { let sum = 10 + 20; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(sum, BinaryOp(IntegerLiteral(10), +, IntegerLiteral(20)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_037():
    """Test variable with function call initialization"""
    source = "func main() -> void { let result = calculate(); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, FunctionCall(Identifier(calculate), []))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_038():
    """Test variable with array initialization"""
    source = "func main() -> void { let arr = [1, 2, 3]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(arr, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_039():
    """Test array variable with type annotation"""
    source = "func main() -> void { let numbers: [int; 3] = [1, 2, 3]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(numbers, [int; 3], ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# Assignment Statements (test_040 - test_049)
# ============================================================================

def test_040():
    """Test simple assignment"""
    source = "func main() -> void { x = 42; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(x), IntegerLiteral(42))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_041():
    """Test assignment with expression"""
    source = "func main() -> void { x = y + z; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(x), BinaryOp(Identifier(y), +, Identifier(z)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_042():
    """Test array element assignment"""
    source = "func main() -> void { arr[0] = 42; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(ArrayAccessLValue(Identifier(arr), IntegerLiteral(0)), IntegerLiteral(42))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_043():
    """Test nested array assignment"""
    source = "func main() -> void { matrix[i][j] = value; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(ArrayAccessLValue(ArrayAccess(Identifier(matrix), Identifier(i)), Identifier(j)), Identifier(value))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_044():
    """Test assignment with function call"""
    source = "func main() -> void { result = calculate(x, y); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(result), FunctionCall(Identifier(calculate), [Identifier(x), Identifier(y)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_045():
    """Test assignment with arithmetic expression"""
    source = "func main() -> void { result = a * b + c; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(result), BinaryOp(BinaryOp(Identifier(a), *, Identifier(b)), +, Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_046():
    """Test assignment with logical expression"""
    source = "func main() -> void { flag = x > 0 && y < 10; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(flag), BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), &&, BinaryOp(Identifier(y), <, IntegerLiteral(10))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_047():
    """Test assignment with unary expression"""
    source = "func main() -> void { result = -x; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(result), UnaryOp(-, Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_048():
    """Test assignment with pipeline expression"""
    source = "func main() -> void { result = data >> process >> format; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(result), BinaryOp(BinaryOp(Identifier(data), >>, Identifier(process)), >>, Identifier(format)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_049():
    """Test assignment with array access"""
    source = "func main() -> void { value = arr[index]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [Assignment(IdLValue(value), ArrayAccess(Identifier(arr), Identifier(index)))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# Control Flow - If Statements (test_050 - test_059)
# ============================================================================

def test_050():
    """Test simple if statement"""
    source = """func main() -> void { 
        if (x > 0) { 
            return x; 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(Identifier(x))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_051():
    """Test if-else statement"""
    source = """func main() -> void { 
        if (x > 0) { 
            return x; 
        } else { 
            return 0;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(Identifier(x))]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(0))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_052():
    """Test if with multiple statements"""
    source = """func main() -> void { 
        if (condition) { 
            let x = 10;
            let y = 20;
            result = x + y;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=Identifier(condition), then_stmt=BlockStmt([VarDecl(x, IntegerLiteral(10)), VarDecl(y, IntegerLiteral(20)), Assignment(IdLValue(result), BinaryOp(Identifier(x), +, Identifier(y)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_053():
    """Test if with complex condition"""
    source = """func main() -> void { 
        if (x > 0 && y < 10) { 
            process(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), &&, BinaryOp(Identifier(y), <, IntegerLiteral(10))), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(process), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_054():
    """Test nested if statements"""
    source = """func main() -> void { 
        if (x > 0) { 
            if (y > 0) { 
                return x + y; 
            }
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([IfStmt(condition=BinaryOp(Identifier(y), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(BinaryOp(Identifier(x), +, Identifier(y)))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_055():
    """Test if with boolean literal condition"""
    source = """func main() -> void { 
        if (true) { 
            execute(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BooleanLiteral(True), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(execute), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_056():
    """Test if with negated condition"""
    source = """func main() -> void { 
        if (!flag) { 
            handle_false(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=UnaryOp(!, Identifier(flag)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(handle_false), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_057():
    """Test if with function call condition"""
    source = """func main() -> void { 
        if (is_valid()) { 
            proceed(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=FunctionCall(Identifier(is_valid), []), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(proceed), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_058():
    """Test if with comparison condition"""
    source = """func main() -> void { 
        if (a == b) { 
            equal(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(Identifier(a), ==, Identifier(b)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(equal), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_059():
    """Test if with parenthesized condition"""
    source = """func main() -> void { 
        if ((x + y) > z) { 
            process(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [IfStmt(condition=BinaryOp(BinaryOp(Identifier(x), +, Identifier(y)), >, Identifier(z)), then_stmt=BlockStmt([ExprStmt(FunctionCall(Identifier(process), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# Control Flow - While Loops (test_060 - test_069)
# ============================================================================

def test_060():
    """Test basic while loop"""
    source = """func main() -> void { 
        while (i < 10) { 
            i = i + 1; 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(10)), BlockStmt([Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_061():
    """Test while loop with complex condition"""
    source = """func main() -> void { 
        while (x > 0 && y < 100) { 
            process(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BinaryOp(BinaryOp(Identifier(x), >, IntegerLiteral(0)), &&, BinaryOp(Identifier(y), <, IntegerLiteral(100))), BlockStmt([ExprStmt(FunctionCall(Identifier(process), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_062():
    """Test while loop with multiple statements"""
    source = """func main() -> void { 
        while (condition) { 
            let temp = calculate();
            update(temp);
            i = i + 1;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(Identifier(condition), BlockStmt([VarDecl(temp, FunctionCall(Identifier(calculate), [])), ExprStmt(FunctionCall(Identifier(update), [Identifier(temp)])), Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_063():
    """Test nested while loops"""
    source = """func main() -> void { 
        while (i < 10) { 
            while (j < 5) { 
                process(i, j);
                j = j + 1;
            }
            i = i + 1;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(10)), BlockStmt([WhileStmt(BinaryOp(Identifier(j), <, IntegerLiteral(5)), BlockStmt([ExprStmt(FunctionCall(Identifier(process), [Identifier(i), Identifier(j)])), Assignment(IdLValue(j), BinaryOp(Identifier(j), +, IntegerLiteral(1)))])), Assignment(IdLValue(i), BinaryOp(Identifier(i), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_064():
    """Test while loop with boolean condition"""
    source = """func main() -> void { 
        while (true) { 
            work(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BooleanLiteral(True), BlockStmt([ExprStmt(FunctionCall(Identifier(work), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_065():
    """Test while loop with function call condition"""
    source = """func main() -> void { 
        while (has_more()) { 
            next(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(FunctionCall(Identifier(has_more), []), BlockStmt([ExprStmt(FunctionCall(Identifier(next), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_066():
    """Test while loop with break statement"""
    source = """func main() -> void { 
        while (true) { 
            if (should_exit) { 
                break; 
            }
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BooleanLiteral(True), BlockStmt([IfStmt(condition=Identifier(should_exit), then_stmt=BlockStmt([BreakStmt()]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_067():
    """Test while loop with continue statement"""
    source = """func main() -> void { 
        while (i < 10) { 
            if (skip_condition) { 
                continue; 
            }
            process(i);
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BinaryOp(Identifier(i), <, IntegerLiteral(10)), BlockStmt([IfStmt(condition=Identifier(skip_condition), then_stmt=BlockStmt([ContinueStmt()])), ExprStmt(FunctionCall(Identifier(process), [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_068():
    """Test while loop with array access"""
    source = """func main() -> void { 
        while (arr[index] > 0) { 
            process(arr[index]); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BinaryOp(ArrayAccess(Identifier(arr), Identifier(index)), >, IntegerLiteral(0)), BlockStmt([ExprStmt(FunctionCall(Identifier(process), [ArrayAccess(Identifier(arr), Identifier(index))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_069():
    """Test while loop with empty body"""
    source = """func main() -> void { 
        while (wait_condition()) { 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(FunctionCall(Identifier(wait_condition), []), BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# Control Flow - For Loops (test_070 - test_079)
# ============================================================================

def test_070():
    """Test basic for loop"""
    source = """func main() -> void { 
        for (i in range) { 
            process(i); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(i, Identifier(range), BlockStmt([ExprStmt(FunctionCall(Identifier(process), [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_071():
    """Test for loop with array literal"""
    source = """func main() -> void { 
        for (item in [1, 2, 3, 4, 5]) { 
            print(item); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(item, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)]), BlockStmt([ExprStmt(FunctionCall(Identifier(print), [Identifier(item)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_072():
    """Test for loop with function call iterable"""
    source = """func main() -> void { 
        for (element in get_items()) { 
            handle(element); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(element, FunctionCall(Identifier(get_items), []), BlockStmt([ExprStmt(FunctionCall(Identifier(handle), [Identifier(element)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_073():
    """Test nested for loops"""
    source = """func main() -> void { 
        for (i in rows) { 
            for (j in cols) { 
                matrix[i][j] = 0; 
            }
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(i, Identifier(rows), BlockStmt([ForStmt(j, Identifier(cols), BlockStmt([Assignment(ArrayAccessLValue(ArrayAccess(Identifier(matrix), Identifier(i)), Identifier(j)), IntegerLiteral(0))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_074():
    """Test for loop with multiple statements"""
    source = """func main() -> void { 
        for (item in collection) { 
            let processed = transform(item);
            store(processed);
            count = count + 1;
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(item, Identifier(collection), BlockStmt([VarDecl(processed, FunctionCall(Identifier(transform), [Identifier(item)])), ExprStmt(FunctionCall(Identifier(store), [Identifier(processed)])), Assignment(IdLValue(count), BinaryOp(Identifier(count), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_075():
    """Test for loop with break"""
    source = """func main() -> void { 
        for (item in items) { 
            if (item == target) { 
                break; 
            }
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(item, Identifier(items), BlockStmt([IfStmt(condition=BinaryOp(Identifier(item), ==, Identifier(target)), then_stmt=BlockStmt([BreakStmt()]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_076():
    """Test for loop with continue"""
    source = """func main() -> void { 
        for (item in items) { 
            if (should_skip(item)) { 
                continue; 
            }
            process(item);
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(item, Identifier(items), BlockStmt([IfStmt(condition=FunctionCall(Identifier(should_skip), [Identifier(item)]), then_stmt=BlockStmt([ContinueStmt()])), ExprStmt(FunctionCall(Identifier(process), [Identifier(item)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_077():
    """Test for loop with array access iterable"""
    source = """func main() -> void { 
        for (element in data[index]) { 
            work(element); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(element, ArrayAccess(Identifier(data), Identifier(index)), BlockStmt([ExprStmt(FunctionCall(Identifier(work), [Identifier(element)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_078():
    """Test for loop with pipeline expression"""
    source = """func main() -> void { 
        for (item in data >> filter >> transform) { 
            use(item); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(item, BinaryOp(BinaryOp(Identifier(data), >>, Identifier(filter)), >>, Identifier(transform)), BlockStmt([ExprStmt(FunctionCall(Identifier(use), [Identifier(item)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_079():
    """Test for loop with empty body"""
    source = """func main() -> void { 
        for (item in items) { 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ForStmt(item, Identifier(items), BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# Expressions and Operators (test_080 - test_089)
# ============================================================================

def test_080():
    """Test arithmetic expressions"""
    source = "func main() -> void { let result = a + b - c * d / e % f; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), -, BinaryOp(BinaryOp(BinaryOp(Identifier(c), *, Identifier(d)), /, Identifier(e)), %, Identifier(f))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_081():
    """Test comparison expressions"""
    source = "func main() -> void { let result = a < b && c > d || e == f && g != h; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(BinaryOp(Identifier(a), <, Identifier(b)), &&, BinaryOp(Identifier(c), >, Identifier(d))), ||, BinaryOp(BinaryOp(Identifier(e), ==, Identifier(f)), &&, BinaryOp(Identifier(g), !=, Identifier(h)))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_082():
    """Test unary expressions"""
    source = "func main() -> void { let result = -x + !flag; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(UnaryOp(-, Identifier(x)), +, UnaryOp(!, Identifier(flag))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_083():
    """Test function call expressions"""
    source = "func main() -> void { let result = func1() + func2(a, b) - func3(x, y, z); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(FunctionCall(Identifier(func1), []), +, FunctionCall(Identifier(func2), [Identifier(a), Identifier(b)])), -, FunctionCall(Identifier(func3), [Identifier(x), Identifier(y), Identifier(z)])))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_084():
    """Test array access expressions"""
    source = "func main() -> void { let result = arr[0] + matrix[i][j] - data[index + 1]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(ArrayAccess(Identifier(arr), IntegerLiteral(0)), +, ArrayAccess(ArrayAccess(Identifier(matrix), Identifier(i)), Identifier(j))), -, ArrayAccess(Identifier(data), BinaryOp(Identifier(index), +, IntegerLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_085():
    """Test parenthesized expressions"""
    source = "func main() -> void { let result = (a + b) * (c - d); }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, BinaryOp(Identifier(c), -, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_086():
    """Test pipeline expressions"""
    source = "func main() -> void { let result = data >> filter >> map >> collect; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(BinaryOp(Identifier(data), >>, Identifier(filter)), >>, Identifier(map)), >>, Identifier(collect)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_087():
    """Test mixed expression precedence"""
    source = "func main() -> void { let result = a && b || c >> d + e * f; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(BinaryOp(Identifier(a), &&, Identifier(b)), ||, Identifier(c)), >>, BinaryOp(Identifier(d), +, BinaryOp(Identifier(e), *, Identifier(f)))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_088():
    """Test complex nested expressions"""
    source = "func main() -> void { let result = calculate(a[i] + b, (c * d) >> process) >= threshold; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(FunctionCall(Identifier(calculate), [BinaryOp(ArrayAccess(Identifier(a), Identifier(i)), +, Identifier(b)), BinaryOp(BinaryOp(Identifier(c), *, Identifier(d)), >>, Identifier(process))]), >=, Identifier(threshold)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_089():
    """Test expression with all literal types"""
    source = "func main() -> void { let result = 42 + 3.14 + true + \"hello\" + [1, 2, 3]; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(BinaryOp(BinaryOp(IntegerLiteral(42), +, FloatLiteral(3.14)), +, BooleanLiteral(True)), +, StringLiteral('hello')), +, ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)])))])])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# Advanced Features and Edge Cases (test_090 - test_100)
# ============================================================================

def test_090():
    """Test return statements"""
    source = """func test() -> int { 
        if (condition) { 
            return 42; 
        } else { 
            return calculate(); 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(test, [], int, [IfStmt(condition=Identifier(condition), then_stmt=BlockStmt([ReturnStmt(IntegerLiteral(42))]), else_stmt=BlockStmt([ReturnStmt(FunctionCall(Identifier(calculate), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_091():
    """Test break and continue statements"""
    source = """func main() -> void { 
        while (true) { 
            if (should_break) { 
                break; 
            }
            if (should_continue) { 
                continue; 
            }
            work();
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [WhileStmt(BooleanLiteral(True), BlockStmt([IfStmt(condition=Identifier(should_break), then_stmt=BlockStmt([BreakStmt()])), IfStmt(condition=Identifier(should_continue), then_stmt=BlockStmt([ContinueStmt()])), ExprStmt(FunctionCall(Identifier(work), []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_092():
    """Test array type declarations"""
    source = """func process(data: [int; 10]) -> [float; 5] { 
        let result: [float; 5] = create_array();
        return result;
    }"""
    expected = "Program(funcs=[FuncDecl(process, [Param(data, [int; 10])], [float; 5], [VarDecl(result, [float; 5], FunctionCall(Identifier(create_array), [])), ReturnStmt(Identifier(result))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_093():
    """Test empty array literal"""
    source = "func main() -> void { let empty = []; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(empty, ArrayLiteral([]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_094():
    """Test string literals with content"""
    source = "func main() -> void { let msg = \"Hello, World!\"; }"
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(msg, StringLiteral('Hello, World!'))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_095():
    """Test expression statements"""
    source = """func main() -> void { 
        calculate();
        process(data);
        x + y;
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [ExprStmt(FunctionCall(Identifier(calculate), [])), ExprStmt(FunctionCall(Identifier(process), [Identifier(data)])), ExprStmt(BinaryOp(Identifier(x), +, Identifier(y)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_096():
    """Test mixed declarations and statements"""
    source = """const MAX = 100;
    func main() -> void { 
        let count = 0;
        while (count < MAX) { 
            process(count);
            count = count + 1;
        }
    }"""
    expected = "Program(consts=[ConstDecl(MAX, IntegerLiteral(100))], funcs=[FuncDecl(main, [], void, [VarDecl(count, IntegerLiteral(0)), WhileStmt(BinaryOp(Identifier(count), <, Identifier(MAX)), BlockStmt([ExprStmt(FunctionCall(Identifier(process), [Identifier(count)])), Assignment(IdLValue(count), BinaryOp(Identifier(count), +, IntegerLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_097():
    """Test complex function with all features"""
    source = """func complex_function(arr: [int; 10], threshold: int) -> bool { 
        let sum = 0;
        for (value in arr) { 
            if (value > threshold) { 
                sum = sum + value;
            }
        }
        return sum > 0;
    }"""
    expected = "Program(funcs=[FuncDecl(complex_function, [Param(arr, [int; 10]), Param(threshold, int)], bool, [VarDecl(sum, IntegerLiteral(0)), ForStmt(value, Identifier(arr), BlockStmt([IfStmt(condition=BinaryOp(Identifier(value), >, Identifier(threshold)), then_stmt=BlockStmt([Assignment(IdLValue(sum), BinaryOp(Identifier(sum), +, Identifier(value)))]))])), ReturnStmt(BinaryOp(Identifier(sum), >, IntegerLiteral(0)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_098():
    """Test multiple function parameters and return"""
    source = """func calculate(a: int, b: float, c: bool, d: string) -> float { 
        if (c) { 
            return a + b; 
        } else { 
            return b - a; 
        }
    }"""
    expected = "Program(funcs=[FuncDecl(calculate, [Param(a, int), Param(b, float), Param(c, bool), Param(d, string)], float, [IfStmt(condition=Identifier(c), then_stmt=BlockStmt([ReturnStmt(BinaryOp(Identifier(a), +, Identifier(b)))]), else_stmt=BlockStmt([ReturnStmt(BinaryOp(Identifier(b), -, Identifier(a)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_099():
    """Test nested block statements"""
    source = """func main() -> void { 
        { 
            let x = 10;
            { 
                let y = 20;
                result = x + y;
            }
        }
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [BlockStmt([VarDecl(x, IntegerLiteral(10)), BlockStmt([VarDecl(y, IntegerLiteral(20)), Assignment(IdLValue(result), BinaryOp(Identifier(x), +, Identifier(y)))])])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_100():
    """Test comprehensive program with all language features"""
    source = """const PI: float = 3.14159;
    const MAX_SIZE = 1000;
    
    func factorial(n: int) -> int { 
        if (n <= 1) { 
            return 1; 
        } else { 
            return n * factorial(n - 1); 
        }
    }
    
    func main() -> void { 
        let numbers: [int; 5] = [1, 2, 3, 4, 5];
        let result = 0;
        
        for (num in numbers) { 
            result = result + factorial(num);
        }
        
        while (result > 0) { 
            if (result % 2 == 0) { 
                result = result / 2; 
            } else { 
                break; 
            }
        }
    }"""
    expected = "Program(consts=[ConstDecl(PI, float, FloatLiteral(3.14159)), ConstDecl(MAX_SIZE, IntegerLiteral(1000))], funcs=[FuncDecl(factorial, [Param(n, int)], int, [IfStmt(condition=BinaryOp(Identifier(n), <=, IntegerLiteral(1)), then_stmt=BlockStmt([ReturnStmt(IntegerLiteral(1))]), else_stmt=BlockStmt([ReturnStmt(BinaryOp(Identifier(n), *, FunctionCall(Identifier(factorial), [BinaryOp(Identifier(n), -, IntegerLiteral(1))])))])]), FuncDecl(main, [], void, [VarDecl(numbers, [int; 5], ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)])), VarDecl(result, IntegerLiteral(0)), ForStmt(num, Identifier(numbers), BlockStmt([Assignment(IdLValue(result), BinaryOp(Identifier(result), +, FunctionCall(Identifier(factorial), [Identifier(num)])))])), WhileStmt(BinaryOp(Identifier(result), >, IntegerLiteral(0)), BlockStmt([IfStmt(condition=BinaryOp(BinaryOp(Identifier(result), %, IntegerLiteral(2)), ==, IntegerLiteral(0)), then_stmt=BlockStmt([Assignment(IdLValue(result), BinaryOp(Identifier(result), /, IntegerLiteral(2)))]), else_stmt=BlockStmt([BreakStmt()]))]))])])"
    actual = str(ASTGenerator(source).generate())
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    assert actual == expected


# ============================================================================
# Additional Test Cases 101-110 (Assignment 2)
# ============================================================================

def test_101():
    """Test function with lambda/anonymous function expression"""
    source = """func main() -> void {
        let f = func(x: int) -> int { return x * 2; };
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(f, FuncDecl(, [Param(x, int)], int, [ReturnStmt(BinaryOp(Identifier(x), *, IntegerLiteral(2)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_102():
    """Test dynamic array type annotation"""
    source = """func process(data: [int]) -> void {
        let item = data[0];
    }"""
    expected = "Program(funcs=[FuncDecl(process, [Param(data, [int; 0])], void, [VarDecl(item, ArrayAccess(Identifier(data), IntegerLiteral(0)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_103():
    """Test function type annotation"""
    source = """const processor: int -> string = func(x: int) -> string { return "result"; };"""
    expected = "Program(consts=[ConstDecl(processor, int, FuncDecl(, [Param(x, int)], string, [ReturnStmt(StringLiteral('result'))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_104():
    """Test complex function type with multiple parameters"""
    source = """func higher_order(f: (int, bool) -> string) -> void {
        let result = f(42, true);
    }"""
    expected = "Program(funcs=[FuncDecl(higher_order, [Param(f, void)], void, [VarDecl(result, FunctionCall(Identifier(f), [IntegerLiteral(42), BooleanLiteral(True)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_105():
    """Test nested function calls with multiple arguments"""
    source = """func main() -> void {
        let result = outer(inner(1, 2), middle(3, 4, 5));
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, FunctionCall(Identifier(outer), [FunctionCall(Identifier(inner), [IntegerLiteral(1), IntegerLiteral(2)]), FunctionCall(Identifier(middle), [IntegerLiteral(3), IntegerLiteral(4), IntegerLiteral(5)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_106():
    """Test complex pipeline expression with multiple stages"""
    source = """func main() -> void {
        let result = input >> validate >> transform >> output;
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(result, BinaryOp(BinaryOp(BinaryOp(Identifier(input), >>, Identifier(validate)), >>, Identifier(transform)), >>, Identifier(output)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_107():
    """Test multi-dimensional array access and assignment"""
    source = """func main() -> void {
        let matrix: [[int; 3]; 2] = [[1, 2, 3], [4, 5, 6]];
        matrix[0][1] = 10;
    }"""
    expected = "Program(funcs=[FuncDecl(main, [], void, [VarDecl(matrix, [[int; 3]; 2], ArrayLiteral([ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2), IntegerLiteral(3)]), ArrayLiteral([IntegerLiteral(4), IntegerLiteral(5), IntegerLiteral(6)])])), Assignment(ArrayAccessLValue(ArrayAccess(Identifier(matrix), IntegerLiteral(0)), IntegerLiteral(1)), IntegerLiteral(10))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_108():
    """Test else-if chain with multiple conditions"""
    source = """func classify(x: int) -> string {
        if (x < 0) {
            return "negative";
        } else if (x == 0) {
            return "zero";
        } else if (x > 100) {
            return "large";
        } else {
            return "positive";
        }
    }"""
    expected = "Program(funcs=[FuncDecl(classify, [Param(x, int)], string, [IfStmt(condition=BinaryOp(Identifier(x), <, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(StringLiteral('negative'))]), elif_branches=[(BinaryOp(Identifier(x), ==, IntegerLiteral(0)), BlockStmt([ReturnStmt(StringLiteral('zero'))])), (BinaryOp(Identifier(x), >, IntegerLiteral(100)), BlockStmt([ReturnStmt(StringLiteral('large'))]))], else_stmt=BlockStmt([ReturnStmt(StringLiteral('positive'))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_109():
    """Test mixed constant and function declarations with complex expressions"""
    source = """const THRESHOLD: float = 3.14159 * 2.0;
    const ENABLED: bool = true && !false;
    func calculate(base: float) -> float {
        return base * THRESHOLD;
    }"""
    expected = "Program(consts=[ConstDecl(THRESHOLD, float, BinaryOp(FloatLiteral(3.14159), *, FloatLiteral(2.0))), ConstDecl(ENABLED, bool, BinaryOp(BooleanLiteral(True), &&, UnaryOp(!, BooleanLiteral(False))))], funcs=[FuncDecl(calculate, [Param(base, float)], float, [ReturnStmt(BinaryOp(Identifier(base), *, Identifier(THRESHOLD)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_110():
    """Test function with void return type and complex control flow"""
    source = """func process_data(arr: [int; 10]) -> void {
        for (item in arr) {
            if (item > 0) {
                if (item % 2 == 0) {
                    continue;
                }
                process(item);
            } else {
                break;
            }
        }
    }"""
    expected = "Program(funcs=[FuncDecl(process_data, [Param(arr, [int; 10])], void, [ForStmt(item, Identifier(arr), BlockStmt([IfStmt(condition=BinaryOp(Identifier(item), >, IntegerLiteral(0)), then_stmt=BlockStmt([IfStmt(condition=BinaryOp(BinaryOp(Identifier(item), %, IntegerLiteral(2)), ==, IntegerLiteral(0)), then_stmt=BlockStmt([ContinueStmt()])), ExprStmt(FunctionCall(Identifier(process), [Identifier(item)]))]), else_stmt=BlockStmt([BreakStmt()]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

