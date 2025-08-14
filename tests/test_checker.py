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

def test_014():
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

def test_015():
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

def test_016():
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

def test_017():
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

def test_018():
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

def test_019():
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

def test_020():
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

def test_021():
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

def test_022():
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

def test_023():
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

def test_024():
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

def test_025():
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

def test_026():
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

def test_027():
    """Pipeline using function call with multiple params"""
    source = """
    func join(a: string, b: string) -> string { return a + b; }

    func main() -> void {
        let result = "Hi" >> join("!");
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_028():
    """Array access with type match and bounds check"""
    source = """
    func main() -> void {
        let a = [10, 20, 30];
        let x: int = a[1];
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_029():
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

def test_030():
    """Function returning void used in pipeline should fail"""
    source = """
    func say(x: string) -> void {}

    func main() -> void {
        let r = "hi" >> say;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(r, BinaryOp(StringLiteral('hi'), >>, Identifier(say)))"
    assert Checker(source).check_from_source() == expected

def test_031():
    """Array element assign with wrong type"""
    source = """
    func main() -> void {
        let a: [int; 3] = [1, 2, 3];
        a[1] = "hello";
    }
    """
    expected = "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(a), IntegerLiteral(1)), StringLiteral('hello'))"
    assert Checker(source).check_from_source() ==  expected

def test_032():
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

def test_033():
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

def test_034():
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

def test_035():
    """Array passed into pipeline function"""
    source = """
    func sum3(arr: [int; 3]) -> int { return arr[0] + arr[1] + arr[2]; }

    func main() -> void {
        let x = [10, 20, 30] >> sum3;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_036():
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

def test_037():
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

def test_038():
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

def test_039():
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

def test_040():
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

def test_041():
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

def test_042():
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

def test_043():
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

def test_044():
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

def test_045():
    """Function with no return (should fail)"""
    source = """
    func f(x: int) -> int {}

    func main() -> void {
        let x = f(1);
    }
    """
    expected = "Type Mismatch In Statement: FuncDecl(f, [Param(x, int)], int, [])"
    assert Checker(source).check_from_source() ==  expected

def test_046():
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

def test_047():
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

def test_048():
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

def test_049():
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

def test_050():
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

def test_051():
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

def test_052():
    """Pipeline with mixed literal and call expressions"""
    source = """
    func wrap(x: string) -> string { return "[" + x + "]"; }
    func main() -> void {
        let s = ("hello" + "!") >> wrap;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_053():
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

def test_054():
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

def test_055():
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

def test_056():
    """Invalid: void return type used in expression"""
    source = """
    func speak(msg: string) -> void {}
    func main() -> void {
        let x = "hi" >> speak;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(x, BinaryOp(StringLiteral('hi'), >>, Identifier(speak)))"
    assert Checker(source).check_from_source() == expected

def test_057():
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

def test_058():
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

def test_059():
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

def test_060():
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

def test_061():
    """Assign void type function result (should fail)"""
    source = """
    func act() -> void {}
    func main() -> void {
        let r = act();
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(r, FunctionCall(Identifier(act), []))"
    assert Checker(source).check_from_source() == expected

def test_062():
    """Check inferred array type"""
    source = """
    func main() -> void {
        let a = [1, 2, 3];
        let b: int = a[1];
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_063():
    """Function declared but never used"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    func main() -> void {
        let a = 5;
    }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_064():
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

def test_065():
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

def test_066():
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

def test_067():
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

def test_068():
    """Invalid: assign array to int"""
    source = """
    func main() -> void {
        let a = [1,2,3];
        let b: int = a;
    }
    """
    expected = "Type Mismatch In Statement: VarDecl(b, int, Identifier(a))"
    assert Checker(source).check_from_source() == expected

def test_069():
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

def test_070():
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

def test_071():
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

def test_072():
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

def test_073():
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

def test_074():
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

def test_075():
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

def test_076():
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

def test_077():
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

def test_078():
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

def test_079():
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

def test_080():
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

def test_081():
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

def test_082():
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

def test_083():
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

def test_084():
    """Test a valid program that should pass all checks"""
    source = """
    const PI: float = 3.14;
    func main() -> void {
        let x: int = 5;
        let y = x + 1;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"
    
def test_085():
    """Test Redeclared variable"""
    source = """
    func main() -> void {
        let x: int = 5;
        let x = 1;
    }
    """
    assert Checker(source).check_from_source() == "Redeclared Variable: x"

def test_086():
    """Test Undeclared identifier"""
    source = """
    func main() -> void {  
        let x = y;
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: y"

def test_087():
    """Test using a variable before declaration"""
    source = """
    func main() -> void {  
        let x = y;
        let y = 1;
    }
    """
    assert Checker(source).check_from_source() == "Undeclared Identifier: y"

def test_088():
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

def test_089():
    """Test using constant for var declaration"""
    source = """
    const MAX = 100;
    func main() -> void {  
        let x = MAX;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_090():
    """Test invalid index - string index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let result = number["1"];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), StringLiteral('1'))" # ﾄ雪ｻ・cﾃ｡i value thoi

def test_091():
    """Test invalid index - float index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let result = number[2.3];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), FloatLiteral(2.3))"

def test_092():
    """Test invalid index - array index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let string_: [string; 3] = ["P", "P", "L"];
        let result = number[string_];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), Identifier(string_))"

def test_093():
    """Test invalid index - bool index"""
    source = """
    func main() -> void {  
        let number: [int; 4] = [0, 3, 6, 9];
        let result = number[false];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), BooleanLiteral(False))"

def test_094():
    """Test Binary operation errors - sum = int + bool"""
    source = """
    func main() -> void {  
        let x = 2;
        let y = true;
        let sum = x + y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), +, Identifier(y))"

def test_095():
    """Test Binary operation errors - logical: int vs bool"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = true;
        let equality = x && y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), &&, Identifier(y))"

def test_096():
    """Test Binary operation errors - logical: int vs bool"""
    source = """
    func main() -> void {  
        let x = 4;
        let y = false;
        let equality = x || y;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: BinaryOp(Identifier(x), ||, Identifier(y))"

def test_097():
    """Test Binary operation errors - mod: int vs float"""
    source = """
    func main() -> void {  
        let module = 45 % 104;
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_098():
    """Test Unary operation errors - not: int"""
    source = """
    func main() -> void {  
        let x = !4;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: UnaryOp(!, IntegerLiteral(4))"

def test_099():
    """Test Function call - too many args"""
    source = """
    func add(x: int, y: int) -> int { return x + y; }
    
    func main() -> void {  
        let x = add(5,3,4);
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: FunctionCall(Identifier(add), [IntegerLiteral(5), IntegerLiteral(3), IntegerLiteral(4)])"

def test_100():
    """Test Array type mismatches - int + float"""
    source = """    
    func main() -> void {  
        let number: [int; 2] = [36, 63];
        let floatArray: [float; 2] = [3.6, 6.3];
        let x = number[0] + floatArray[0];
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_101():
    """Test Nested expression errors - bool index"""
    source = """    
    func main() -> void {  
        let number: [int; 2] = [36, 63];
        let x = number[number[true]];
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Expression: ArrayAccess(Identifier(number), BooleanLiteral(True))"

def test_102():
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

def test_103():
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

def test_104():
    """Test Assignment statement errors - float array to int array"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number[1] = 2.3;
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(number), IntegerLiteral(1)), FloatLiteral(2.3))"

def test_105():
    """Test Assignment statement errors - float to int element"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number[1] = 2.3;
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(number), IntegerLiteral(1)), FloatLiteral(2.3))"

def test_106():
    """Test Assignment statement errors - string to int element"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number[1] = "hi";
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(ArrayAccessLValue(Identifier(number), IntegerLiteral(1)), StringLiteral('hi'))"

def test_107():
    """Test Assignment statement errors - float array to int array"""
    source = """   
    func main() -> void {  
        let number: [int; 2] = [1,2];
        number = [1.0, 2.0];
    } 
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(number), ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0)]))"

def test_108():
    """Test Constant assignment error"""
    source = """   
    const MAX = 36;
    func main() -> void {
        MAX = 37;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(MAX), IntegerLiteral(37))"

def test_109():
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

def test_110():
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

def test_111():
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

def test_112():
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

def test_113():
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

def test_114():
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

def test_115():
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
def test_116():
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

def test_117():
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

def test_118():
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

def test_119():
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

def test_120():
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

def test_121():
    """Test Break/continue in function scope"""
    source = """  
    func main() -> void {
        continue;
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: ContinueStmt()"

def test_122():
    """Test Break/continue in conditional blocks"""
    source = """  
    func main() -> void {
        if (true) {
            break;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: BreakStmt()"

def test_123():
    """Test Break/continue in conditional blocks"""
    source = """  
    func main() -> void {
        if (true) {
            continue;
        }
    }
    """
    assert Checker(source).check_from_source() == "Must In Loop: ContinueStmt()"

def test_124():
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

def test_125():
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

def test_126():
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

def test_127():
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

def test_128():
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

def test_129():
    """Test array return size errors"""
    source = """
    func main() -> void {
        let matrix: [[int; 2]; 3] = [[1, 2], [3, 4], [5, 6]];
        let differentMatrix: [[int; 3]; 2] = [[1, 2, 3], [4, 5, 6]];
        
        matrix = differentMatrix;
    }
    """
    assert Checker(source).check_from_source() == "Type Mismatch In Statement: Assignment(IdLValue(matrix), Identifier(differentMatrix))"

def test_130():
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

def test_131():
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

def test_132():
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

def test_133():
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

def test_134():
    """Test array bounds with compile-time constant indices"""
    source = """
    func main() -> void {
        let numbers: [int; 3] = [1, 2, 3];
        let x = numbers[2];  // Valid bounds - index 2 for size 3
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

def test_135():
    """Test array assignment with negative index"""
    source = """
    func main() -> void {
        let numbers: [int; 5] = [1, 2, 3, 4, 5];
        numbers[0] = 0;  // Valid assignment
    }
    """
    assert Checker(source).check_from_source() == "Static checking passed"

 