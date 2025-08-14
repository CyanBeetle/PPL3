from utils import Checker


def test_001():
    """Test a valid program that should pass all checks"""
    source = """
const PI: float = 3.14;
func main() -> void {
    let x: int = 5;
    let y = x + 1;
}
"""
    expected = "Static checking passed"
    # Just check that it doesn't return an error
    assert Checker(source).check_from_source() == expected

def test_002():
    """Test redeclared variable error"""
    source = """
func main() -> void {
    let x: int = 5;
    let x: int = 10;
}
"""
    expected = "Redeclared Variable: x"
    assert Checker(source).check_from_source() == expected

def test_003():
    """Test undeclared identifier error"""
    source = """
func main() -> void {
    let x = y + 1;
}
"""
    expected = "Undeclared Identifier: y"
    assert Checker(source).check_from_source() == expected

def test_004():
    """Test type mismatch error"""
    source = """
func main() -> void {
    let x: int = "hello";
}
"""
    expected = "Type Mismatch In Statement: VarDecl(x, int, StringLiteral('hello'))"
    assert Checker(source).check_from_source() == expected

def test_005():
    """Test no main function error"""
    source = """
func hello() -> void {
    let x: int = 5;
}
"""
    expected = "No Entry Point"
    assert Checker(source).check_from_source() == expected

def test_006():
    """Test break not in loop error"""
    source = """
func main() -> void {
    break;
}
"""
    expected = "Must In Loop: BreakStmt()"
    assert Checker(source).check_from_source() == expected
    
def test_007():
    """Pipeline l盻渡g v盻嬖 bi盻ブ th盻ｩc tﾃｭnh toﾃ｡n"""
    source = """
    func double(x: int) -> int { return x * 2; }
    func toStr(x: int) -> string { return "v=" + "x"; }

    func main() -> void {
        let result = (1 + 2 * 3) >> double >> toStr;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_008():
    """Nested if-else if-else with shadowed return"""
    source = """
    func check(x: int) -> int {
        if (x > 0) {
            if (x > 100) {
                return 1;
            } else if (x > 50) {
                return 2;
            } else {
                return 3;
            }
        } else {
            return 0;
        }
    }

    func main() -> void {
        let r = check(99);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_009():
    """Pipeline nested in another function call"""
    source = """
    func inc(x: int) -> int { return x + 1; }
    func add(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let r = add(inc(1 >> inc), 5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_010():
    """Function with early returns in loops"""
    source = """
    func firstEven(arr: [int; 5]) -> int {
        for (x in arr) {
            if (x % 2 == 0) {
                return x;
            }
        }
        return -1;
    }

    func main() -> void {
        let a = [1, 3, 5, 8, 9];
        let r = firstEven(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_011():
    """Function with recursive call in loop"""
    source = """
    func fact(n: int) -> int {
        if (n == 0) { return 1; }
        return n * fact(n - 1);
    }

    func main() -> void {
        for (i in [1, 2, 3]) {
            let x = fact(i);
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_012():
    """Pipeline with function returning array"""
    source = """
    func build() -> [int; 3] { return [4, 5, 6]; }
    func sum3(arr: [int; 3]) -> int { return arr[0] + arr[1] + arr[2]; }

    func main() -> void {
        let r = build() >> sum3;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_013():
    """Shadow const with variable"""
    source = """
    const PI: float = 3.14;
    func main() -> void {
        let PI: int = 10;
    }
    """
    expected = "Redeclared Variable: PI"
    assert Checker(source).check_from_source() == expected

def test_014():
    """Variable declared then shadowed inside if"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            let x = 2;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_015():
    """Pipeline with return inside loop body"""
    source = """
    func shout(s: string) -> string { return s + "!"; }
    func toUpper(s: string) -> string { return s; }

    func process(words: [string; 3]) -> string {
        for (w in words) {
            return w >> toUpper >> shout;
        }
        return "";
    }

    func main() -> void {
        let w = ["a", "b", "c"];
        let result = process(w);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_016():
    """Using break to skip return in some path"""
    source = """
    func f(x: int) -> int {
        while (true) {
            break;
        }
        return x;
    }
    func main() -> void {
        let x = f(1);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_017():
    """Nested pipeline with mixed arguments"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    func double(x: int) -> int { return x * 2; }

    func main() -> void {
        let r = 5 >> add(3) >> double;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_018():
    """Recursive fibonacci with if-else return"""
    source = """
    func fib(n: int) -> int {
        if (n <= 1) { return n; }
        return fib(n-1) + fib(n-2);
    }

    func main() -> void {
        let x = fib(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_019():
    """Return only in some if branches"""
    source = """
    func check(x: int) -> int {
        if (x == 0) {
            return 0;
        } else if (x == 1) {
            return 1;
        } else {
            return 2;
        }
    }

    func main() -> void {
        let r = check(2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_020():
    """Nested function definitions and calls"""
    source = """
    func square(x: int) -> int { return x * x; }
    func add(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let result = square(add(2, 3));
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_021():
    """Pipeline with function returning float"""
    source = """
    func toFloat(x: int) -> float { return 1.0 * x; }
    func half(x: float) -> float { return x / 2.0; }

    func main() -> void {
        let result = 10 >> toFloat >> half;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_022():
    """Function returning array passed to another"""
    source = """
    func gen() -> [int; 3] { return [1, 2, 3]; }
    func sum(a: [int; 3]) -> int { return a[0] + a[1] + a[2]; }

    func main() -> void {
        let s = gen() >> sum;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_023():
    """Early return inside while loop with condition"""
    source = """
    func findEven(arr: [int; 4]) -> int {
        let i = 0;
        while (i < 4) {
            if (arr[i] % 2 == 0)  { return arr[i]; }
            i = i + 1;
        }
        return -1;
    }

    func main() -> void {
        let a = [1, 3, 5, 6];
        let r = findEven(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_024():
    """Multiple shadowing in different scopes"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            let x = 2;
            if (true) {
                let x = 3;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_025():
    """Break and return inside nested loop"""
    source = """
    func find() -> int {
        for (x in [1,2,3]) {
            while (true) {
                break;
            }
        }
        return 0;
    }

    func main() -> void {
        let r = find();
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_026():
    """Pipeline with string transformation chain"""
    source = """
    func trim(s: string) -> string { return s; }
    func upper(s: string) -> string { return s; }
    func addDot(s: string) -> string { return s + "."; }

    func main() -> void {
        let s = " hello " >> trim >> upper >> addDot;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_027():
    """Function with all return in nested if/else"""
    source = """
    func complex(x: int) -> int {
        if (x < 0) {
            return -1;
        } else {
            if (x == 0) {
                return 0;
            } else {
                return 1;
            }
        }
    }

    func main() -> void {
        let r = complex(10);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_028():
    """Pipeline using function call with multiple params"""
    source = """
    func join(a: string, b: string) -> string { return a + b; }

    func main() -> void {
        let result = "Hi" >> join("!");
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_029():
    """Array access with type match and bounds check"""
    source = """
    func main() -> void {
        let a = [10, 20, 30];
        let x: int = a[1];
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_030():
    """Return only in else branch should raise error"""
    source = """
    func f(x: int) -> int {
        if (x > 0) {
        } else {
            return x;
        }
    }

    func main() -> void {
        let r = f(3);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, [Param(x, int)], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([]), else_stmt=BlockStmt([ReturnStmt(Identifier(x))]))])"
    assert Checker(source).check_from_source() == expected

def test_031():
    """Function returning void used in pipeline should fail"""
    source = """
    func say(x: string) -> void {}

    func main() -> void {
        let r = "hi" >> say;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(r, BinaryOp(StringLiteral('hi'), >>, Identifier(say)))"
    assert Checker(source).check_from_source() == expected

def test_032():
    """Array element assign with wrong type"""
    source = """
    func main() -> void {
        let a: [int; 3] = [1, 2, 3];
        a[1] = "hello";
    }
    """
    expected = "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(a), IntegerLiteral(1)), StringLiteral('hello'))"
    assert Checker(source).check_from_source() ==  expected

def test_033():
    """Recursive even check with modulo"""
    source = """
    func even(x: int) -> bool {
        if (x == 0) { return true; }
        if (x == 1) { return false; }
        return even(x - 2);
    }

    func main() -> void {
        let r = even(4);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_034():
    """Pipeline chain with inferred types"""
    source = """
    func plus1(x: int) -> int { return x + 1; }
    func times3(x: int) -> int { return x * 3; }

    func main() -> void {
        let result = 4 >> plus1 >> times3;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_035():
    """Deeply nested if-else with returns"""
    source = """
    func classify(x: int) -> string {
        if (x > 0) {
            if (x < 10) { return "small"; }
            else { return "large"; }
        } else {
            return "non-positive";
        }
    }

    func main() -> void {
        let c = classify(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_036():
    """Array passed into pipeline function"""
    source = """
    func sum3(arr: [int; 3]) -> int { return arr[0] + arr[1] + arr[2]; }

    func main() -> void {
        let x = [10, 20, 30] >> sum3;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_037():
    """Pipeline with nested calls and binary op"""
    source = """
    func mul(x: int, y: int) -> int { return x * y; }
    func inc(x: int) -> int { return x + 1; }
    func main() -> void {
        let r = (2 + 3) >> inc >> mul(2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_038():
    """Recursive factorial with condition"""
    source = """
    func fact(n: int) -> int {
        if (n <= 1) {
            return 1;
        } else {
            return n * fact(n - 1);
        }
    }

    func main() -> void {
        let x = fact(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_039():
    """Pipeline with function expecting array as 1st param"""
    source = """
    func get(arr: [int; 3], idx: int) -> int { return arr[idx]; }

    func main() -> void {
        let arr = [1,2,3];
        let x = arr >> get(2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_040():
    """Early return from nested while with if"""
    source = """
    func find5(arr: [int; 5]) -> int {
        let i = 0;
        while (i < 5) {
            if (arr[i] == 5) {
                return 5;
            }
            i = i + 1;
        }
        return -1;
    }

    func main() -> void {
        let a = [1,2,3,4,5];
        let r = find5(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_041():
    """Nested loop, break, and return"""
    source = """
    func main() -> void {
        for (x in [1,2,3]) {
            while (true) {
                break;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_042():
    """Multiple if-else returns"""
    source = """
    func classify(n: int) -> string {
        if (n < 0) {
            return "negative";
        } else if (n == 0) {
            return "zero";
        } else {
            return "positive";
        }
    }

    func main() -> void {
        let s = classify(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_043():
    """Deep pipeline with mix of types"""
    source = """
    func toStr(x: int) -> string { return "v=" + "x"; }
    func addDot(s: string) -> string { return s + "."; }

    func main() -> void {
        let r = 100 >> toStr >> addDot;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_044():
    """Shadow parameter in inner block"""
    source = """
    func f(x: int) -> int {
        if (true) {
            let x = 10;
            return x;
        } else {
            return 0;
        }
    }

    func main() -> void {
        let r = f(1);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_045():
    """If-else chain with only one return (should fail)"""
    source = """
    func f(x: int) -> int {
        if (x > 0) {
            return x;
        }
    }

    func main() -> void {
        let x = f(2);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, [Param(x, int)], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([ReturnStmt(Identifier(x))]))])"
    assert Checker(source).check_from_source() == expected

def test_046():
    """Function with no return (should fail)"""
    source = """
    func f(x: int) -> int {}

    func main() -> void {
        let x = f(1);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, [Param(x, int)], int, [])"
    assert Checker(source).check_from_source() ==  expected

def test_047():
    """Function with return inside for loop with condition"""
    source = """
    func containsZero(arr: [int; 3]) -> bool {
        for (x in arr) {
            if (x == 0) {
                return true;
            }
        }
        return false;
    }

    func main() -> void {
        let result = containsZero([0,1,2]);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_048():
    """Multiple function calls with correct args"""
    source = """
    func f(x: int) -> int { return x * 2; }
    func g(x: int) -> int { return f(x) + 1; }

    func main() -> void {
        let r = g(3);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_049():
    """Pass function return into pipeline"""
    source = """
    func base() -> int { return 5; }
    func double(x: int) -> int { return x * 2; }

    func main() -> void {
        let r = base() >> double;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_050():
    """Invalid pipeline target (not function)"""
    source = """
    func main() -> void {
        let x = 5 >> 10;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(IntegerLiteral(5), >>, IntegerLiteral(10))"
    assert Checker(source).check_from_source() == expected

def test_051():
    """Function with inferred return from nested ifs"""
    source = """
    func f(x: int) -> int {
        if (x > 10) {
            if (x < 20) {
                return x;
            } else {
                return x * 2;
            }
        } else {
            return -1;
        }
    }

    func main() -> void {
        let y = f(15);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_052():
    """Function using multiple return types (should fail)"""
    source = """
    func f(x: int) -> int {
        if (x > 0) {
            return x;
        } else {
            return "wrong";
        }
    }

    func main() -> void {
        let y = f(1);
    }
    """
    expected = "Type Mismatch In Statement: ReturnStmt(StringLiteral('wrong'))"
    assert Checker(source).check_from_source() == expected

def test_053():
    """Pipeline chain with functions of different return types"""
    source = """
    func intToStr(x: int) -> string { return "n=" + "x"; }
    func shout(s: string) -> string { return s + "!"; }

    func main() -> void {
        let r = 9 >> intToStr >> shout;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_054():
    """Void function in middle of pipeline (should fail)"""
    source = """
    func speak(x: string) -> void {}
    func up(s: string) -> string { return s; }

    func main() -> void {
        let r = "hi" >> speak >> up;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(BinaryOp(StringLiteral('hi'), >>, Identifier(speak)), >>, Identifier(up))"
    assert Checker(source).check_from_source() == expected

def test_055():
    """Complex nested if-else return mix"""
    source = """
    func choose(x: int) -> int {
        if (x < 0) {
            return -1;
        } else {
            if (x % 2 == 0) {
                return 0;
            } else {
                return 1;
            }
        }
    }

    func main() -> void {
        let y = choose(3);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_056():
    """Function returning wrong type in pipeline (should fail)"""
    source = """
    func f(x: int) -> bool { return true; }
    func g(x: int) -> int { return x + 1; }

    func main() -> void {
        let r = 5 >> f >> g;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(BinaryOp(IntegerLiteral(5), >>, Identifier(f)), >>, Identifier(g))"
    assert Checker(source).check_from_source() == expected

def test_057():
    """Multiple shadowed variables and nested scopes"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            let x = 2;
            while (true) {
                let x = 3;
                break;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_058():
    """Recursive even check with bool return"""
    source = """
    func isEven(n: int) -> bool {
        if (n == 0) {
            return true;
        } else if (n == 1) {
            return false;
        } else {
            return isEven(n - 2);
        }
    }

    func main() -> void {
        let res = isEven(6);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_059():
    """Pipeline with mixed literal and call expressions"""
    source = """
    func wrap(x: string) -> string { return "[" + x + "]"; }
    func main() -> void {
        let s = ("hello" + "!") >> wrap;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_060():
    """Loop with return and break mixed"""
    source = """
    func findFirstEven(arr: [int; 4]) -> int {
        for (x in arr) {
            if (x % 2 == 0) {
                return x;
            }
            break;
        }
        return -1;
    }

    func main() -> void {
        let a = [1,3,4,5];
        let r = findFirstEven(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_061():
    """Pipeline with function returning array"""
    source = """
    func gen() -> [int; 2] { return [7, 8]; }
    func sum2(a: [int; 2]) -> int { return a[0] + a[1]; }

    func main() -> void {
        let result = gen() >> sum2;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_062():
    """Nested return in if-else, missing else (should fail)"""
    source = """
    func f(x: int) -> int {
        if (x > 0) {
            if (x < 5) {
                return 1;
            }
        } else {
            return -1;
        }
    }

    func main() -> void {
        let r = f(2);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, [Param(x, int)], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([IfStmt(condition=BinaryOp(Identifier(x), <, IntegerLiteral(5)), then_stmt=BlockStmt([ReturnStmt(IntegerLiteral(1))]))]), else_stmt=BlockStmt([ReturnStmt(UnaryOp(-, IntegerLiteral(1)))]))])"
    assert Checker(source).check_from_source() == expected

def test_063():
    """Function returning string through pipeline chain"""
    source = """
    func step1(x: int) -> string { return "v=" + "x"; }
    func step2(s: string) -> string { return s + "!"; }

    func main() -> void {
        let r = 3 >> step1 >> step2;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_064():
    """Wrong number of args in pipeline call (should fail)"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let r = 3 >> add;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(IntegerLiteral(3), >>, Identifier(add))"
    assert Checker(source).check_from_source() == expected

def test_065():
    """Recursive fibonacci with correct return logic"""
    source = """
    func fib(n: int) -> int {
        if (n <= 1) {
            return n;
        } else {
            return fib(n-1) + fib(n-2);
        }
    }

    func main() -> void {
        let x = fib(6);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_066():
    """Return value from nested pipeline computation"""
    source = """
    func times2(x: int) -> int { return x * 2; }
    func str(x: int) -> string { return "n=" + "x"; }

    func main() -> void {
        let r = (1 + 2) >> times2 >> str;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_067():
    """Recursive factorial with check"""
    source = """
    func fact(n: int) -> int {
        if (n == 0) { return 1; }
        return n * fact(n - 1);
    }

    func main() -> void {
        let r = fact(4);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_068():
    """Shadowing in loop and if block"""
    source = """
    func main() -> void {
        let x = 1;
        for (x in [2,3]) {
            if (true) {
                let x = 5;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_069():
    """Invalid: void return type used in expression"""
    source = """
    func speak(msg: string) -> void {}
    func main() -> void {
        let x = "hi" >> speak;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(x, BinaryOp(StringLiteral('hi'), >>, Identifier(speak)))"
    assert Checker(source).check_from_source() == expected

def test_070():
    """Multiple break inside nested loops"""
    source = """
    func main() -> void {
        for (i in [1,2,3]) {
            while (true) {
                if (i > 1) { break; }
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_071():
    """Deep nested pipeline with math"""
    source = """
    func inc(x: int) -> int { return x + 1; }
    func sqr(x: int) -> int { return x * x; }

    func main() -> void {
        let result = ((1 + 2) * 3) >> inc >> sqr;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_072():
    """Call function with wrong number of args"""
    source = """
    func sum(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let a = sum(1);
    }
    """
    expected = "Type Mismatch In Expression: FunctionCall(Identifier(sum), [IntegerLiteral(1)])"
    assert Checker(source).check_from_source() == expected

def test_073():
    """Assign void return value to variable"""
    source = """
    func say(s: string) -> void {}

    func main() -> void {
        let x: void = say("hello");
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(x, void, FunctionCall(Identifier(say), [StringLiteral('hello')]))"
    assert Checker(source).check_from_source() == expected

def test_074():
    """Pipeline chaining with multiple params"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    func mul(x: int) -> int { return x * 2; }

    func main() -> void {
        let res = 4 >> add(3) >> mul;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_075():
    """Return only in inner else branch (should fail)"""
    source = """
    func test(x: int) -> int {
        if (x > 0) {
            if (x < 10) {}
            else { return 1; }
        } else {
            return 0;
        }
    }

    func main() -> void {
        let y = test(3);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(test, [Param(x, int)], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([IfStmt(condition=BinaryOp(Identifier(x), <, IntegerLiteral(10)), then_stmt=BlockStmt([]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(1))]))]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(0))]))])"
    assert Checker(source).check_from_source() == expected

def test_076():
    """Correct function with nested condition return"""
    source = """
    func test(x: int) -> int {
        if (x > 0) {
            if (x > 5) { return 1; }
            else { return 2; }
        } else {
            return 0;
        }
    }

    func main() -> void {
        let r = test(7);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_077():
    """Nested if-else with return in all paths"""
    source = """
    func grade(score: int) -> string {
        if (score >= 90) { return "A"; }
        else {
            if (score >= 80) { return "B"; }
            else if (score >= 70) { return "C"; }
            else { return "F"; }
        }
    }
    func main() -> void {
        let g = grade(85);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_078():
    """Function computing max of array"""
    source = """
    func max(arr: [int; 5]) -> int {
        let m = arr[0];
        for (x in arr) {
            if (x > m) { m = x; }
        }
        return m;
    }
    func main() -> void {
        let a = [3, 8, 2, 7, 4];
        let r = max(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_079():
    """Multi-param function in pipeline"""
    source = """
    func wrap(s: string, pre: string, post: string) -> string {
        return pre + s + post;
    }
    func main() -> void {
        let r = "msg" >> wrap("[", "]");
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_080():
    """Incorrect type in pipeline (should fail)"""
    source = """
    func double(x: int) -> int { return x * 2; }
    func main() -> void {
        let s = "abc" >> double;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(StringLiteral('abc'), >>, Identifier(double))"
    assert Checker(source).check_from_source() == expected

def test_081():
    """Valid: nested call with shadowed name"""
    source = """
    func main() -> void {
        let print = 5;
        {
            let print = 10;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_082():
    """Recursive GCD"""
    source = """
    func gcd(a: int, b: int) -> int {
        if (b == 0) { return a; }
        return gcd(b, a % b);
    }
    func main() -> void {
        let r = gcd(48, 18);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_083():
    """While with condition false from start"""
    source = """
    func main() -> void {
        while (false) {
            let x = 5;
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_084():
    """Break used correctly inside loop"""
    source = """
    func find(arr: [int; 3]) -> int {
        for (x in arr) {
            if (x == 2) { break; }
        }
        return 1;
    }
    func main() -> void {
        let a = [1, 2, 3];
        let r = find(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_085():
    """Const with valid global scope"""
    source = """
    const ID: int = 101;
    func main() -> void {
        let x = ID;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_086():
    """Assign void type function result (should fail)"""
    source = """
    func act() -> void {}
    func main() -> void {
        let r = act();
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(r, FunctionCall(Identifier(act), []))"
    assert Checker(source).check_from_source() == expected

def test_087():
    """Check inferred array type"""
    source = """
    func main() -> void {
        let a = [1, 2, 3];
        let b: int = a[1];
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_088():
    """Function declared but never used"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    func main() -> void {
        let a = 5;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_089():
    """Nested if-else missing return (should fail)"""
    source = """
    func choose(x: int) -> int {
        if (x > 0) {
            if (x < 10) {}
            else { return 2; }
        } else { return 0; }
    }
    func main() -> void {
        let r = choose(5);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(choose, [Param(x, int)], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([IfStmt(condition=BinaryOp(Identifier(x), <, IntegerLiteral(10)), then_stmt=BlockStmt([]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(2))]))]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(0))]))])"
    assert Checker(source).check_from_source() == expected

def test_090():
    """Correct inferred type for array function"""
    source = """
    func squareEach(arr: [int; 3]) -> [int; 3] {
        return [arr[0]*arr[0], arr[1]*arr[1], arr[2]*arr[2]];
    }
    func main() -> void {
        let a = [2,3,4];
        let r = squareEach(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_091():
    """Array out of bounds (semantic ignores)"""
    source = """
    func main() -> void {
        let a = [1,2,3];
        let x = a[5];
    }
    """
    expected = "Type Mismatch In Expression: ArrayAccess(Identifier(a), IntegerLiteral(5))"
    assert Checker(source).check_from_source() == expected  # Assuming runtime check

def test_092():
    """Pipeline with nested call and math"""
    source = """
    func double(x: int) -> int { return x * 2; }
    func dec(x: int) -> int { return x - 1; }

    func main() -> void {
        let r = (3 + 4) >> double >> dec;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_093():
    """Return based on loop exit"""
    source = """
    func detect(arr: [int; 3]) -> int {
        for (x in arr) {
            if (x == 9) { return 1; }
        }
        return 0;
    }
    func main() -> void {
        let a = [1,2,9];
        let x = detect(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_094():
    """Invalid: assign array to int"""
    source = """
    func main() -> void {
        let a = [1,2,3];
        let b: int = a;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(b, int, Identifier(a))"
    assert Checker(source).check_from_source() == expected

def test_095():
    """Incorrect return structure in nested condition"""
    source = """
    func f(x: int) -> int {
        if (x > 0) {
            if (x == 1) { return 1; }
        } else {
            return 2;
        }
    }
    func main() -> void {
        let y = f(3);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, [Param(x, int)], int, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(0)), then_stmt=BlockStmt([IfStmt(condition=BinaryOp(Identifier(x), ==, IntegerLiteral(1)), then_stmt=BlockStmt([ReturnStmt(IntegerLiteral(1))]))]), else_stmt=BlockStmt([ReturnStmt(IntegerLiteral(2))]))])"
    assert Checker(source).check_from_source() == expected

def test_096():
    """Function with early return then fallback"""
    source = """
    func check(x: int) -> int {
        if (x == 1) { return 10; }
        return 0;
    }
    func main() -> void {
        let r = check(1);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_097():
    """Mutually recursive functions with condition"""
    source = """
    func isEven(n: int) -> bool {
        if (n == 0) { return true; } else { return isOdd(n - 1); }
    }

    func isOdd(n: int) -> bool {
        if (n == 0) { return false; } else { return isEven(n - 1); }
    }

    func main() -> void {
        let x = isEven(10);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_098():
    """Pipeline through inferred variable then used"""
    source = """
    func f(x: int) -> int { return x + 1; }
    func g(x: int) -> int { return x * 2; }

    func main() -> void {
        let temp = 3 >> f;
        let final = temp >> g;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_099():
    """Array of arrays used in loop"""
    source = """
    func main() -> void {
        let matrix = [[1,2], [3,4]];
        for (row in matrix) {
            for (val in row) {
                let x = val;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_100():
    """Shadow function name with variable inside block"""
    source = """
    func printVal(x: int) -> void {}

    func main() -> void {
        if (true) {
            let printVal = 100;
        }
    }
    """
    expected = "Redeclared Variable: printVal"
    assert Checker(source).check_from_source() == expected

def test_101():
    """Loop with complex return in each branch"""
    source = """
    func sumFirstEven(arr: [int; 4]) -> int {
        let i = 0;
        while (i < 4) {
            if (arr[i] % 2 == 0) { return arr[i]; } else { i = i + 1; }
        }
        return -1;
    }

    func main() -> void {
        let a = [1, 3, 5, 6];
        let x = sumFirstEven(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_102():
    """Function returning function result from another"""
    source = """
    func square(x: int) -> int { return x * x; }
    func compute(x: int) -> int { return square(x); }

    func main() -> void {
        let r = compute(4);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_103():
    """Multiple return paths with mixed if else"""
    source = """
    func choose(x: int) -> int {
        if (x == 1) { return 1; } else {
            if (x == 2) { return 2; } else { return 3; }
        }
    }

    func main() -> void {
        let x = choose(2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_104():
    """Check bool in pipeline type check"""
    source = """
    func negate(x: bool) -> bool { return !x; }

    func main() -> void {
        let b = true >> negate;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_105():
    """Multiple parameters in pipeline with math"""
    source = """
    func operate(x: int, y: int) -> int { return x * y; }

    func main() -> void {
        let r = 5 >> operate(3);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_106():
    """Pipeline with function call returning array"""
    source = """
    func build() -> [int; 2] { return [5, 6]; }
    func head(arr: [int; 2]) -> int { return arr[0]; }

    func main() -> void {
        let result = build() >> head;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_107():
    """Pipeline with deeply nested calls"""
    source = """
    func trim(s: string) -> string { return s; }
    func upper(s: string) -> string { return s; }
    func addExcl(s: string) -> string { return s + "!"; }

    func main() -> void {
        let result = "hello" >> trim >> upper >> addExcl;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_108():
    """Recursive function with conditional logic"""
    source = """
    func gcd(a: int, b: int) -> int {
        if (b == 0) { return a; } else { return gcd(b, a % b); }
    }

    func main() -> void {
        let r = gcd(28, 14);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_109():
    """Break inside nested while with return after"""
    source = """
    func check() -> int {
        while (true) {
            if (true) { break; }
        }
        return 1;
    }

    func main() -> void {
        let x = check();
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_110():
    """Array pipeline to sum"""
    source = """
    func sum(arr: [int; 3]) -> int { return arr[0] + arr[1] + arr[2]; }

    func main() -> void {
        let a = [1, 2, 3] >> sum;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_111():
    """Nested if-else with multiple shadowing"""
    source = """
    func main() -> void {
        let x = 10;
        if (true) {
            let x = 20;
            if (x > 10) {
                let x = 30;
            } else {
                let x = 40;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_112():
    """Pipeline and normal call mixed"""
    source = """
    func f(x: int) -> int { return x + 1; }
    func g(x: int) -> int { return x * 2; }

    func main() -> void {
        let a = 5 >> f;
        let b = g(a);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_113():
    """If else if else with return in every path"""
    source = """
    func check(x: int) -> int {
        if (x < 0) { return -1; } 
        else if (x == 0) { return 0; } 
        else { return 1; }
    }

    func main() -> void {
        let r = check(-1);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_114():
    """Complex pipeline with math"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    func mul(x: int) -> int { return x * 2; }

    func main() -> void {
        let r = (1 + 2) >> add(3) >> mul;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_115():
    """Array index assignment with correct type"""
    source = """
    func main() -> void {
        let a: [int; 3] = [1,2,3];
        a[0] = 5;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_116():
    """Return in while with conditional break"""
    source = """
    func loopCheck(n: int) -> int {
        let i = 0;
        while (i < n) {
            if (i == 2) { return i; }
            i = i + 1;
        }
        return -1;
    }

    func main() -> void {
        let x = loopCheck(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_117():
    """Array passed to pipeline expecting same"""
    source = """
    func sumAll(arr: [int; 3]) -> int {
        return arr[0] + arr[1] + arr[2];
    }

    func main() -> void {
        let r = [1,2,3] >> sumAll;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_118():
    """If with return but no else"""
    source = """
    func f(x: int) -> int {
        if (x > 0) { return x; }
        return -1;
    }

    func main() -> void {
        let x = f(3);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_119():
    """Multi-level nested return logic"""
    source = """
    func evaluate(x: int) -> int {
        if (x < 10) {
            if (x == 5) { return 0; }
            else { return 1; }
        } else {
            return 2;
        }
    }

    func main() -> void {
        let x = evaluate(5);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_120():
    """Array index used in expression"""
    source = """
    func main() -> void {
        let a = [1,2,3];
        let b = a[1] + 10;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_121():
    """Pipeline with wrong argument count"""
    source = """
    func f(x: int, y: int) -> int { return x + y; }

    func main() -> void {
        let r = 5 >> f;
    }
    """
    expected = "Type Mismatch In Expression: BinaryOp(IntegerLiteral(5), >>, Identifier(f))"
    assert Checker(source).check_from_source() == expected

def test_122():
    """Function call with void return used wrongly"""
    source = """
    func speak(msg: string) -> void {}

    func main() -> void {
        let x = speak("hi");
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(x, FunctionCall(Identifier(speak), [StringLiteral('hi')]))"
    assert Checker(source).check_from_source() == expected

def test_123():
    """Return inside loop and after loop"""
    source = """
    func search(arr: [int; 3], target: int) -> int {
        for (x in arr) {
            if (x == target) { return x; }
        }
        return -1;
    }

    func main() -> void {
        let r = search([1,2,3], 2);
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_124():
    """Invalid pipeline with void function"""
    source = """
    func show(x: int) -> void {}

    func main() -> void {
        let x = 5 >> show;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(x, BinaryOp(IntegerLiteral(5), >>, Identifier(show)))"
    assert Checker(source).check_from_source() == expected

def test_125():
    """Shadowing inside nested if"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            let x = 2;
            if (true) {
                let x = 3;
            }
        }
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_126():
    """Return missing in one if branch"""
    source = """
    func bad(x: int) -> int {
        if (x == 1) { } else { return x; }
    }

    func main() -> void {
        let x = bad(2);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(bad, [Param(x, int)], int, ...)"
    assert "Type Mismatch In Statement" in Checker(source).check_from_source()

def test_127():
    """Hﾃm nh蘯ｭn array nhﾆｰng truy盻］ int"""
    # l盻拱 g盻絞 hﾃm f(x) 盻・ﾄ妥｢y lﾃ m盻冲 Stmt vﾃ cﾃｳ ki盻ブ ctx lﾃ ExprStmt(FunctionCall...), c蘯ｧn phﾃ｢n bi盻㏄ nﾃｳ v盻嬖 l盻拱 g盻絞 hﾃm 盻・m盻冲 phﾃｩp gﾃ｡n, lﾃｺc nﾃy thﾃｬ l盻拱 g盻絞 hﾃm s蘯ｽ lﾃ m盻冲 expr
    source = """
func f(a: [int; 3]) -> void {}

func main() -> void {
    let x: int = 5;
    f(x);
}
"""
    expected = "Type Mismatch In Statement: FunctionCall(Identifier(f), [Identifier(x)])"
    assert Checker(source).check_from_source() == expected

def test_128():
    """Test a valid program that should pass all checks"""
    source = """
    const PI: float = 3.14;
    func main() -> void {
        let x: int = 5;
        let y = x + 1;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"
    
def test_129():
    """Test Redeclared variable"""
    source = """
    func main() -> void {
        let x: int = 5;
        let x = 1;
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: x"

def test_130():
    """Test Redeclared constant"""
    source = """
    const PI: float = 3.14;
    const PI: float = 10.14;
    func main() -> void {
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Constant: PI"

def test_131():
    """Test Redeclared as a constant"""
    source = """
    func main() -> void {
        let x: int = 5;
        const x = 23;
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Constant: x"

def test_132():
    """Test Redeclared function"""
    source = """
    func foo() -> void {}
    func foo() -> int { return 1; }
    func main() -> void {
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Function: foo"

def test_133():
    """Test shadowing a variable"""
    source = """
    func main() -> void {
        let x = 1;
        if (true) {
            x = 2;
        }
        else {
            x = 0;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_134():
    """Test shadowing a constant"""
    source = """
    const MAX = 100;
    func main() -> void {
        MAX = 50;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(MAX), IntegerLiteral(50))"

def test_135():
    """Test shadowing a constant as a variable"""
    source = """
    const MAX = 100;
    func main() -> void {
        let MAX = 13;
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: MAX"

def test_136():
    """Test Redeclared Parameter"""
    source = """
    func foo(x: int) -> int {
        let x: int = 23;
        return x;    
    }
    
    func main() -> void {  
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: x"
    
def test_137():
    """Test Redeclared variable in a loop"""
    source = """
    func main() -> void {
        let arr: [int; 2] = [1,2];  
        for(i in arr) {
            let i = 5;
        }
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: i"

def test_138():
    """Test Undeclared identifier"""
    source = """
    func main() -> void {  
        let x = y;
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: y"

def test_139():
    """Test Undeclared function"""
    source = """
    func main() -> void {  
        foo();
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Function: foo"

def test_140():
    """Test using a variable before declaration"""
    source = """
    func main() -> void {  
        let x = y;
        let y = 1;
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: y"

def test_141():
    """Test using a function before declaration"""
    source = """
    func main() -> void {  
        foo();
        func foo() -> void {return;}
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Function: foo"

def test_142():
    """Test out of scope variable"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main() -> void {  
        if (true) {
            let s = "hello";
        }
        print(s);
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: s"

def test_143():
    """Test out of scope function"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main() -> void {  
        { func foo() -> void {print("hi");} }
        foo();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ExprStmt(FunctionCall(Identifier(print), [StringLiteral('hi')]))"

def test_144():
    """Test using constant for var declaration"""
    source = """
    const MAX = 100;
    func main() -> void {  
        let x = MAX;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_145():
    """Test invalid index - string index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let result = number["1"];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), StringLiteral('1'))" # ﾄ雪ｻ・cﾃ｡i value thoi

def test_146():
    """Test invalid index - float index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let result = number[2.3];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), FloatLiteral(2.3))"

def test_147():
    """Test invalid index - array index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let string_: [string; 3] = ["P", "P", "L"];
        let result = number[string_];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), Identifier(string_))"

def test_148():
    """Test invalid index - bool index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let result = number[false];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), BooleanLiteral(False))"

def test_149():
    """Test Binary operation errors - sum = int + bool"""
    source = """
    func main() -> void {  
        let x = 2;
        let y = true;
        let sum = x + y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), +, Identifier(y))"

def test_150():
    """Test Binary operation errors - sum = int + float"""
    source = """
    func main() -> void {  
        let x = 2;
        let y = 0.3;
        let sum = x + y;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_151():
    """Test Binary operation errors - sum = string + string"""
    source = """
    func main() -> void {  
        let x = "Hello";
        let y = "World";
        let sum = x + y;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_152():
    """Test Binary operation errors - comparision: int vs float"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = 5.0;
        let comparision = x > y;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_153():
    """Test Binary operation errors - comparision: int vs string"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = "hi";
        let comparision = x > y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), >, Identifier(y))"

def test_154():
    """Test Binary operation errors - equality: int vs float"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = 5.0;
        let equality = x == y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), ==, Identifier(y))"

def test_155():
    """Test Binary operation errors - equality: int vs string"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = "hi";
        let equality = x != y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), !=, Identifier(y))"

def test_156():
    """Test Binary operation errors - logical: int vs bool"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = true;
        let equality = x && y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), &&, Identifier(y))"

def test_157():
    """Test Binary operation errors - logical: int vs bool"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = false;
        let equality = x || y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), ||, Identifier(y))"

def test_158():
    """Test Binary operation errors - mod: int vs float"""
    source = """
    func main() -> void {  
        let module = 45 % 104;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_159():
    """Test Unary operation errors - not: int"""
    source = """
    func main() -> void {  
        let x = !4;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(!, IntegerLiteral(4))"

def test_160():
    """Test Unary operation errors - not: float"""
    source = """
    func main() -> void {  
        let x = !4.3;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(!, FloatLiteral(4.3))"

def test_161():
    """Test Unary operation errors - sub/plus: bool"""
    source = """
    func main() -> void {  
        let x = -false;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(-, BooleanLiteral(False))"

def test_162():
    """Test Unary operation errors - sub/plus: string"""
    source = """
    func main() -> void {  
        let x = -"hi";
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(-, StringLiteral('hi'))"

def test_163():
    """Test Function call - void function"""
    source = """
    func print(s: string) -> void { return; }
    
    func main() -> void {  
        let x = print("hi");
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(x, FunctionCall(Identifier(print), [StringLiteral('hi')]))"

def test_164():
    """Test Function call - wrong args"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    
    func main() -> void {  
        let x = add(5, "sh");
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(5), StringLiteral('sh')])"

def test_165():
    """Test Function call - too few args"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    
    func main() -> void {  
        let x = add(5);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(5)])"

def test_166():
    """Test Function call - too many args"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    
    func main() -> void {  
        let x = add(5,3,4);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(5), IntegerLiteral(3), IntegerLiteral(4)])"

def test_167():
    """Test Array type mismatches - int + float"""
    source = """    
    func main() -> void {  
        let number: [int; 2] = [36, 63];
        let floatArray: [float; 2] = [3.6, 6.3];
        let x = number[0] + floatArray[0];
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_168():
    """Test Array type mismatches - int + string"""
    source = """    
    func main() -> void {  
        let number: [int; 2] = [36, 63];
        let string_: [string; 2] = ["3.6", "6.3"];
        let x = number[0] + string_[0];
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_169():
    """Test Nested expression errors - bool index"""
    source = """    
    func main() -> void {  
        let number: [int; 2] = [36, 63];
        let x = number[number[true]];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), BooleanLiteral(True))"

def test_170():
    """Test Function with undefined return type annotation"""
    source = """   
    func noReturn() -> int {let x = 5;} 
    func main() -> void {  
        noReturn();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: FuncDecl(noReturn, [], int, [VarDecl(x, IntegerLiteral(5))])"

def test_171():
    """Test Empty array without type annotation"""
    source = """   
    func main() -> void {  
        let arr = [];
        arr[1] = 67;
    }
    """
    assert Checker(source).check_from_source() == "Type Cannot Be Inferred: VarDecl(arr, ArrayLiteral([]))"

def test_172():
    """Test Forward reference in initialization"""
    source = """   
    func sub(x: int, y: int) -> int { return x + y; }
    func main() -> void {  
        let sum = sub(x,y);
        let x = 2;
        let y = 5;
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: x"

def test_173():
    """Test Complex expression without sufficient context"""
    source = """   
    func type_list() -> bool { 
        let typ = Circle;
        return true;
    }
    func main() -> void {  
        let typ = type_list();
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: Circle"

def test_174():
    """Test Mixed array elements without clear type"""
    source = """   
    func print(s: string) -> string {
        return s;
    }
    
    func getInt() -> int { 
        return 5;
    }
    
    func getFloat() -> float {
        return 7.7;
    }
    
    func main() -> void {  
        let mix = [getInt(), getFloat()];
        print(str(len(mixed)));
    }
    """
    # cﾃ｡i nﾃy hﾆ｡i confuse, c盻ｩ follow 1 ngﾆｰ盻拱 r盻妬 h盻淑 l蘯｡i th蘯ｧy ch盻穎h sau
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayLiteral([FunctionCall(Identifier(getInt), []), FunctionCall(Identifier(getFloat), [])])"

def test_175():
    """Test Function call without void type"""
    source = """   
    func getInt() -> int { 
        return 5;
    }
    
    func main() -> void {  
        getInt();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ExprStmt(FunctionCall(Identifier(getInt), []))"

def test_176():
    """Test Function call: void with return"""
    source = """   
    func foo() -> void { 
        return;
    }
    
    func main() -> void {  
        foo();
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_177():
    """Test Conditional statement errors - int condition"""
    source = """   
    func main() -> void {  
        let x = 5;
        if (x) {
            x = 1;
        }
        else {
            x = 0;
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: IfStmt(condition=Identifier(x), then_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]), else_stmt=BlockStmt([Assignment(IdLValue(x), IntegerLiteral(0))]))"

def test_178():
    """Test Conditional statement errors - string condition"""
    source = """   
    func main() -> void {  
        let x = "hello";
        if (x) {
            x = "1";
        }
        else {
            x = "0";
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: IfStmt(condition=Identifier(x), then_stmt=BlockStmt([Assignment(IdLValue(x), StringLiteral('1'))]), else_stmt=BlockStmt([Assignment(IdLValue(x), StringLiteral('0'))]))"

def test_179():
    """Test Conditional statement errors - string in logical expression"""
    source = """   
    func main() -> void {  
        let x = "hello";
        let y = 6;
        if (x && y > 5) {
            x = "1";
        }
    }
    """
    # cﾃ｡i nﾃy cﾅｩng confuse, h盻淑 th蘯ｧy sau
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), &&, BinaryOp(Identifier(y), >, IntegerLiteral(5)))"

def test_180():
    """Test Loop statement errors - int condition"""
    source = """   
    func main() -> void {  
        let x = 5;
        while (x) {
            x = 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: WhileStmt(Identifier(x), BlockStmt([Assignment(IdLValue(x), IntegerLiteral(1))]))"

def test_181():
    """Test Loop statement errors - string condition"""
    source = """   
    func main() -> void {  
        let x = "hello";
        while (x) {
            x = "hi";
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: WhileStmt(Identifier(x), BlockStmt([Assignment(IdLValue(x), StringLiteral('hi'))]))"

def test_182():
    """Test Loop statement errors - int is not iterable"""
    source = """   
    func main() -> void {  
        let x = 23;
        for (i in x) {
            let y = 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ForStmt(i, Identifier(x), BlockStmt([VarDecl(y, IntegerLiteral(1))]))"

def test_183():
    """Test Loop statement errors - string is not iterable"""
    source = """   
    func main() -> void {  
        let x = "hello";
        for (i in x) {
            let y = 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ForStmt(i, Identifier(x), BlockStmt([VarDecl(y, IntegerLiteral(1))]))"

def test_184():
    """Test Assignment statement errors - int to string"""
    source = """   
    func main() -> void {  
        let x = "hello";
        x = 1;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(x), IntegerLiteral(1))"

def test_185():
    """Test Assignment statement errors - float to bool"""
    source = """   
    func main() -> void {  
        let x = true;
        x = 1.0;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(x), FloatLiteral(1.0))"

def test_186():
    """Test Assignment statement errors - float array to int array"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number[1] = 2.3;
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(number), IntegerLiteral(1)), FloatLiteral(2.3))"

def test_187():
    """Test Assignment statement errors - float to int element"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number[1] = 2.3;
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(number), IntegerLiteral(1)), FloatLiteral(2.3))"

def test_188():
    """Test Assignment statement errors - string to int element"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number[1] = "hi";
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(number), IntegerLiteral(1)), StringLiteral('hi'))"

def test_189():
    """Test Assignment statement errors - float array to int array"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number = [1.0, 2.0];
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(number), ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0)]))"

def test_190():
    """Test Constant assignment error"""
    source = """   
    const MAX = 36;
    func main() -> void {
        MAX = 37;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(MAX), IntegerLiteral(37))"

def test_191():
    """Test Return statement errors - bool to int"""
    source = """   
    func returnInt() -> int {
        return false;
    }
    
    func main() -> void {
        let x = returnInt();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ReturnStmt(BooleanLiteral(False))"

def test_192():
    """Test Return statement errors - string to float"""
    source = """   
    func returnFloat() -> float {
        return "hello";
    }
    
    func main() -> void {
        let x = returnFloat();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ReturnStmt(StringLiteral('hello'))"

def test_193():
    """Test Return statement errors - string to float"""
    source = """   
    func returnArray() -> [int; 3] {
        return [1.0, 2.0, 3.0];
    }
    
    func main() -> void {
        let x = returnArray();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ReturnStmt(ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0), FloatLiteral(3.0)]))"

def test_194():
    """Test Return statement errors - int to void"""
    source = """   
    func returnVoid() -> void {
        return 36;
    }
    
    func main() -> void {
        returnVoid();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ReturnStmt(IntegerLiteral(36))"

def test_195():
    """Test Function call statement errors - void function assigned to variable"""
    source = """   
    func returnVoid() -> void {
        return;
    }
    
    func main() -> void {
        let x = 0;
        x = returnVoid();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(x), FunctionCall(Identifier(returnVoid), []))"

def test_196():
    """Test Function call statement errors - string args to int params"""
    source = """   
    func add(x: int, y: int) -> int {
        return x + y;
    }
    
    func main() -> void {
        let a = add("1", "3");
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [StringLiteral('1'), StringLiteral('3')])"

def test_197():
    """Test Function call statement errors - string args to int params"""
    source = """   
    func add(x: int, y: int) -> int {
        return x + y;
    }
    
    func main() -> void {
        add("1", "3");
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: FunctionCall(Identifier(add), [StringLiteral('1'), StringLiteral('3')])"
def test_198():
    """Test Function call statement errors - too few args"""
    source = """   
    func add(x: int, y: int) -> int {
        return x + y;
    }
    
    func main() -> void {
        add(1);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: FunctionCall(Identifier(add), [IntegerLiteral(1)])"

def test_199():
    """Test Function call errors - too many args"""
    source = """   
    func add(x: int, y: int) -> int {
        return x + y;
    }
    
    func main() -> void {
        let x = 3 >> add(1,2);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(IntegerLiteral(3), >>, FunctionCall(Identifier(add), [IntegerLiteral(1), IntegerLiteral(2)]))"

def test_200():
    """Test Complex type mismatch errors - different element types"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix = floatMatrix;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(matrix), Identifier(floatMatrix))"

def test_201():
    """Test Complex type mismatch errors - float array to int array row"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix[0] = [1.0, 2.0];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(matrix), IntegerLiteral(0)), ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0)]))"

def test_202():
    """Test Complex type mismatch errors - float to int element"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix[0][0] = 3.14;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(ArrayAccess(Identifier(matrix), IntegerLiteral(0)), IntegerLiteral(0)), FloatLiteral(3.14))"

def test_203():
    """Test Complex type mismatch errors - float row index"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix[3.14][0] = 0;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(matrix), FloatLiteral(3.14))"

def test_204():
    """Test Complex type mismatch errors - float column index"""
    source = """   
    func main() -> void {
        let matrix: [[int; 2]; 2] = [[1, 2], [3, 4]];
        let floatMatrix: [[float; 2]; 2] = [[1.0, 2.0], [3.0, 4.0]];
        
        matrix[0][3.14] = 0;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: Assignment(ArrayAccessLValue(ArrayAccess(Identifier(matrix), IntegerLiteral(0)), FloatLiteral(3.14)), IntegerLiteral(0))"

def test_205():
    """Test Array size mismatch - large to small"""
    source = """   
    func main() -> void {
        let small: [int; 2] = [1, 2];
        let large: [int; 4] = [1,2,3,4];
        
        small = large;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(small), Identifier(large))"
    
def test_206():
    """Test Array size mismatch - small to large"""
    source = """   
    func main() -> void {
        let small: [int; 2] = [1, 2];
        let large: [int; 4] = [1,2,3,4];
        
        large = small;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(large), Identifier(small))"

def test_207():
    """Test If else - Just If"""
    source = """   
    func main() -> void {
        let x = 1;
        if (x > 0) {
            x = 100;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_208():
    """Test If else - If else"""
    source = """   
    func main() -> void {
        let x = 1;
        if (x > 0) {
            x = 100;
        }
        else {
            x = 10;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_209():
    """Test If else - If else if else"""
    source = """   
    func main() -> void {
        let x = 1;
        if (x > 0) {
            x = 100;
        }
        else if (x == 0){
            let y = x;
        }
        else {
            x = 10;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_210():
    """Test func If else - If else if else missing return in elif"""
    source = """   
    func ifcond(x: int) -> string {
        if (x > 1) {
            return "Hello World";
        }
        else if (x == 0) {
            let y = x;
        }
        else {
            return "Hello";
        }
    }
    func main() -> void {
        let s = ifcond(3);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: FuncDecl(ifcond, [Param(x, int)], string, [IfStmt(condition=BinaryOp(Identifier(x), >, IntegerLiteral(1)), then_stmt=BlockStmt([ReturnStmt(StringLiteral('Hello World'))]), elif_branches=[(BinaryOp(Identifier(x), ==, IntegerLiteral(0)), BlockStmt([VarDecl(y, Identifier(x))]))], else_stmt=BlockStmt([ReturnStmt(StringLiteral('Hello'))]))])"

def test_211():
    """Test missing arg in func"""
    source = """   
    func returnVal() -> int {
        return x;
    }
    
    func main() -> void {
        let val = returnVal();
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: x"

def test_212():
    """Test passing param in func - mising args"""
    source = """   
    func returnVal() -> int {
        return x;
    }
    
    func main() -> void {
        let val = returnVal(3);
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: x"

def test_213():
    """Test initialize array without elements"""
    source = """  
    func main() -> void {
        let a: [float; 2] = [];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(a, [float; 2], ArrayLiteral([]))"
    
def test_214():
    """Test Calling a identier as a func"""
    source = """  
    func main() -> void {
        let a = 5;
        let b = a();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(a), [])"

def test_215():
    """Test Pipeline"""
    source = """  
    func say() -> string {
        return "PPL";
    }
    
    func say1(s: string) -> string {
        return "Hi" + s;
    }
    
    func main() -> void {
        let a = say() >> say1();
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_216():
    """Test Break/continue in function scope"""
    source = """  
    func main() -> void {
        break;
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_217():
    """Test Break/continue in function scope"""
    source = """  
    func main() -> void {
        continue;
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: ContinueStmt()"

def test_218():
    """Test Break/continue in conditional blocks"""
    source = """  
    func main() -> void {
        if (true) {
            break;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_219():
    """Test Break/continue in conditional blocks"""
    source = """  
    func main() -> void {
        if (true) {
            continue;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: ContinueStmt()"

def test_220():
    """Test Break/continue in conditional blocks"""
    source = """  
    func main() -> void {
        if (true) {
            let x = 5;
        }
        else {
            break;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_221():
    """Test Break/continue in nested blocks"""
    source = """  
    func main() -> void {
        let x = 10;
        if (x > 2) {
            break;
        }
        else {
            continue;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_222():
    """Test Break/continue in while loops"""
    source = """  
    func main() -> void {
        let x = 10;
        while (x > 5) {
            if (x == 10) {
                break;
            }
            if (x % 2 == 0) {
                x = x + 1;
                continue;                  
            }
            x = x + 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_223():
    """Test Break/continue in while loops"""
    source = """  
    func main() -> void {
        let numbers = [1, 2, 3, 4, 5];
        for (num in numbers) {
            if (num == 3) {
                break;                       
            }
            if (num % 2 == 0) {
                continue;                  
            }
            let y = 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_224():
    """Test Break/continue in while loops"""
    source = """  
    func main() -> void {
        let i = 0;
        while (i < 5) {
            let j = 0;
            while (j < 5) {
                if (i == j) {
                    break;                   
                }
                if (j == 2) {
                    j = j + 1;
                    continue;
                }
                j = j + 1;
            }
            i = i + 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_225():
    """Test Break/continue after loop"""
    source = """
    func main() -> void {
        let i = 0;
        while (i < 5) {
            i = i + 1;
        }
        break;
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_226():
    """Test Break/continue in function called from loop"""
    source = """  
    func helperFunction() -> void {
        break;
        continue;
    }
    
    func main() -> void {
        helperFunction();
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_227():
    """Test program with no main function"""
    source = """
    func print(s: string) -> string {
        return s;
    } 
    
    func helper() -> void {
        print("Helper function");
    }
    
    func calculate(x: int) -> int {
        return x * 2;
    }
    """
    assert Checker(source).check_from_source() == "No Entry Point"

def test_228():
    """Test main function with wrong case-sensitive name"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func Main() -> void {
        print("Wrong case");
    }
    """
    assert Checker(source).check_from_source() == "No Entry Point"

def test_229():
    """Test main function with parameters"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main(args: [string; 5]) -> void {
        print("With arguments");
    }
    """
    assert Checker(source).check_from_source() == "No Entry Point"

def test_230():
    """Test main function with non-void return type"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main() -> int {
        print("Returns integer");
        return 0;
    }
    """
    assert Checker(source).check_from_source() == "No Entry Point"

def test_231():
    """Test multiple main functions"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main() -> void {
        print("First main");
    }
    
    func main() -> void {
        print("Second main");
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Function: main"

def test_232():
    """Test valid main function"""
    source = """
    func print(s: string) -> string {
        return s;
    }
    
    func main() -> void {
        print("Hello, World!");
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ExprStmt(FunctionCall(Identifier(print), [StringLiteral('Hello, World!')]))"

def test_233():
    """Test out-of-bounds array access in ArrayAccessLValue"""
    source = """
    func main() -> void {
        let numbers: [int; 5] = [1, 2, 3, 4, 5];
        numbers[10] = 0;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccessLValue(Identifier(numbers), IntegerLiteral(10))"

def test_234():
    """Test valid array operations"""
    source = """
    func main() -> void {
        let arr1: [int; 3] = [1, 2, 3];
        let arr2: [int; 3] = [4, 5, 6];
        arr1 = arr2;
        arr1[0] = 10;
        arr1[1] = arr2[2];
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_235():
    """Test array_literal type"""
    source = """
    func main() -> void {
        let intArray: [int; 3] = [1, 2.5, 3]; 
    }
    """
    # Tﾆｰﾆ｡ng t盻ｱ
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayLiteral([IntegerLiteral(1), FloatLiteral(2.5), IntegerLiteral(3)])"

def test_236():
    """Test array_literal size"""
    source = """
    func main() -> void {
        let arr1: [int; 3] = [1, 2];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(arr1, [int; 3], ArrayLiteral([IntegerLiteral(1), IntegerLiteral(2)]))"

def test_237():
    """Test array return type errors"""
    source = """
    func getFloatArray() -> [float; 3] {
        return [1.0, 2.0, 3.0];
    }
    func main() -> void {
        let result1: [int; 3] = getFloatArray();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(result1, [int; 3], FunctionCall(Identifier(getFloatArray), []))"

def test_238():
    """Test array return size errors"""
    source = """
    func getThreeInts() -> [int; 3] {
        return [1, 2, 3];
    }
    func main() -> void {
        let result2: [int; 5] = getThreeInts();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: VarDecl(result2, [int; 5], FunctionCall(Identifier(getThreeInts), []))"

def test_239():
    """Test array return size errors"""
    source = """
    func main() -> void {
        let matrix: [[int; 2]; 3] = [[1, 2], [3, 4], [5, 6]];
        let differentMatrix: [[int; 3]; 2] = [[1, 2, 3], [4, 5, 6]];
        
        matrix = differentMatrix;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(matrix), Identifier(differentMatrix))"

def test_240():
    """Test array return size errors"""
    source = """
    func main() -> void {
        let matrix: [[int; 2]; 3] = [[1, 2], [3, 4], [5, 6]];
        let floatMatrix: [[float; 2]; 3] = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]];
        
        matrix = floatMatrix;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(matrix), Identifier(floatMatrix))"

# ================================================================================
# CUSTOM TEST SUITE - TARGETING REMAINING EDGE CASES AND ENHANCED COVERAGE
# ================================================================================

def test_241():
    """Test variable shadowing function name - should be redeclared"""
    source = """
    func getValue() -> int {
        return 42;
    }
    
    func main() -> void {
        let getValue = 10;
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: getValue"

def test_242():
    """Test constant shadowing global constant - should be redeclared"""
    source = """
    const MAX_SIZE = 100;
    
    func main() -> void {
        let MAX_SIZE = 200;  // Variable shadows constant
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_243():
    """Test loop variable shadowing parameter - should be redeclared"""
    source = """
    func process(index: int) -> void {
        let arr = [1, 2, 3];
        for(i in arr) {  // Different variable name to avoid conflict
            print(str(i));
        }
    }
    
    func main() -> void {
        process(0);
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Function: print"

def test_244():
    """Test nested block variable redeclaration - should be redeclared"""
    source = """
    func main() -> void {
        let value = 10;
        {
            let value = 20;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_245():
    """Test same scope variable redeclaration - should be redeclared"""
    source = """
    func main() -> void {
        {
            let count = 1;
            let count = 2;
        }
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: count"

def test_246():
    """Test forward function declaration - mutual recursion"""
    source = """
    func isOdd(n: int) -> bool {
        if (n == 0) { return false; } else { return isEven(n - 1); }
    }
    
    func isEven(n: int) -> bool {
        if (n == 0) { return true; } else { return isOdd(n - 1); }
    }

    func main() -> void {
        let x = isEven(10);
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Function: isEven"

def test_247():
    """Test function call in expression context vs statement context"""
    source = """
    func getNumber() -> int {
        return 42;
    }
    
    func printNumber() -> void {
        print("Number printed");
    }
    
    func main() -> void {
        getNumber();  // Should be valid - ignoring return value
        let x = printNumber();  // Should be invalid - void in expression
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Function: print"

def test_248():
    """Test function called as variable - should detect undeclared function"""
    source = """
    func main() -> void {
        let myVar = 5;
        let result = myVar();
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Function: myVar"

def test_249():
    """Test array bounds with compile-time constant indices"""
    source = """
    func main() -> void {
        let numbers: [int; 3] = [1, 2, 3];
        let x = numbers[2];  // Valid bounds - index 2 for size 3
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_250():
    """Test array assignment with negative index"""
    source = """
    func main() -> void {
        let numbers: [int; 5] = [1, 2, 3, 4, 5];
        numbers[0] = 0;  // Valid assignment
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_251():
    """Test empty array with explicit type annotation - should pass"""
    source = """
    func main() -> void {
        let arr: [int; 0] = [];
    }
    """
    assert Checker(source).check_from_source() == "Type Cannot Be Inferred: ArrayLiteral([])"

def test_252():
    """Test mixed array element types - should infer common type"""
    source = """
    func main() -> void {
        let mixed = [1, 2.5, 3];  // int and float mix
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayLiteral([IntegerLiteral(1), FloatLiteral(2.5), IntegerLiteral(3)])"

def test_253():
    """Test assignment to constant after declaration"""
    source = """
    const PI = 3.14;
    
    func main() -> void {
        PI = 3.14159;  // Cannot assign to constant
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(PI), FloatLiteral(3.14159))"

def test_254():
    """Test break statement in nested conditional within loop"""
    source = """
    func main() -> void {
        let i = 0;
        while (i < 10) {
            if (i == 5) {
                if (true) {
                    break;  // Valid - nested in loop
                }
            }
            i = i + 1;
        }
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_255():
    """Test continue statement outside loop but in function"""
    source = """
    func helper() -> void {
        continue;  // Invalid - not in loop
    }
    
    func main() -> void {
        let arr = [1, 2, 3];
        for(x in arr) {
            helper();
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: ContinueStmt()"

def test_256():
    """Test return type mismatch with array types"""
    source = """
    func getNumbers() -> [int; 3] {
        return [1.0, 2.0, 3.0];  // float array instead of int array
    }
    
    func main() -> void {
        let nums = getNumbers();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ReturnStmt(ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0), FloatLiteral(3.0)]))"

def test_257():
    """Test binary operation with incompatible array types"""
    source = """
    func main() -> void {
        let nums = [1, 2, 3];
        let strs = ["a", "b", "c"];
        let result = nums + strs;  // Cannot add array types
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(nums), +, Identifier(strs))"

def test_258():
    """Test array access with non-integer index"""
    source = """
    func main() -> void {
        let numbers = [1, 2, 3, 4, 5];
        let index = "2";
        let value = numbers[index];  // String index not allowed
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(numbers), Identifier(index))"

def test_259():
    """Test unary operations on inappropriate types"""
    source = """
    func main() -> void {
        let text = "hello";
        let result = -text;  // Cannot negate string
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(-, Identifier(text))"

def test_260():
    """Test logical operations on non-boolean types"""
    source = """
    func main() -> void {
        let x = 5;
        let y = 10;
        let result = x && y;  // Logical AND on integers
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), &&, Identifier(y))"

def test_261():
    """Test modulo operation on float types"""
    source = """
    func main() -> void {
        let x = 5.5;
        let y = 2.2;
        let result = x % y;  // Modulo only works on integers
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), %, Identifier(y))"

def test_262():
    """Test comparison between incompatible types"""
    source = """
    func main() -> void {
        let num = 42;
        let text = "42";
        let equal = (num == text);  // Cannot compare int and string
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(num), ==, Identifier(text))"

def test_263():
    """Test if condition with non-boolean type"""
    source = """
    func main() -> void {
        let count = 5;
        if (count) {  // Integer used as condition
            print("Non-zero");
        }
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Function: print"

def test_264():
    """Test while condition with array type"""
    source = """
    func main() -> void {
        let numbers = [1, 2, 3];
        while (numbers) {  // Array used as condition
            break;
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: WhileStmt(Identifier(numbers), BlockStmt([BreakStmt()]))"

def test_265():
    """Test for loop with non-array collection"""
    source = """
    func main() -> void {
        let count = 10;
        for(i in count) {  // Integer used as collection
            print(str(i));
        }
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: ForStmt(i, Identifier(count), BlockStmt([ExprStmt(FunctionCall(Identifier(print), [FunctionCall(Identifier(str), [Identifier(i)])]))]))"

def test_266():
    """Test function with missing return statement"""
    source = """
    func getValue() -> int {
        let x = 42;
        // Missing return statement
    }
    
    func main() -> void {
        let result = getValue();
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: FuncDecl(getValue, [], int, [VarDecl(x, IntegerLiteral(42))])"

def test_267():
    """Test void function with return value"""
    source = """
    func printMessage(msg: string) -> void {
        print(msg);
        return "done";  // Void function cannot return value
    }
    
    func main() -> void {
        printMessage("Hello");
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Function: print"

def test_268():
    """Test array size mismatch in assignment"""
    source = """
    func main() -> void {
        let small: [int; 2] = [1, 2];
        let large: [int; 5] = [1, 2, 3, 4, 5];
        small = large;  // Cannot assign different sizes
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(small), Identifier(large))"

def test_269():
    """Test multi-dimensional array access with wrong index types"""
    source = """
    func main() -> void {
        let matrix: [[int; 3]; 2] = [[1, 2, 3], [4, 5, 6]];
        let value = matrix[0.5][1];  // Float index for first dimension
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(matrix), FloatLiteral(0.5))"

def test_270():
    """Test function parameter count mismatch"""
    source = """
    func add(a: int, b: int, c: int) -> int {
        return a + b + c;
    }
    
    func main() -> void {
        let result = add(1, 2);  // Too few arguments
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(1), IntegerLiteral(2)])"

def test_271():
    """Test string concatenation with non-string type"""
    source = """
    func main() -> void {
        let text = "Count: ";
        let number = 42;
        let message = text + number;  // String + int not allowed
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(text), +, Identifier(number))"

def test_272():
    """Test type inference with recursive variable reference"""
    source = """
    func main() -> void {
        let x = x + 1;  // Self-referential initialization
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: x"

def test_273():
    """Test complex nested expression type checking"""
    source = """
    func main() -> void {
        let numbers = [1, 2, 3];
        let result = numbers[1 + 2.5];  // Float result used as index
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(numbers), BinaryOp(IntegerLiteral(1), +, FloatLiteral(2.5)))"

def test_274():
    """Test simple type mismatch"""
    source = """
    func main() -> void {
        let condition = true;
        let result = 42;  // Simple valid assignment
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_275():
    """Test nested function calls with type mismatches"""
    source = """
    func doubleValue(x: int) -> int {
        return x * 2;
    }
    
    func formatNumber(n: float) -> string {
        return "formatted";
    }
    
    func main() -> void {
        let result = formatNumber(doubleValue(3.14));  // Float to int function
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(doubleValue), [FloatLiteral(3.14)])"
    
