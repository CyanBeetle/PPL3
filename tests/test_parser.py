from utils import Parser


def test_001():
    """Test basic function declaration"""
    source = """func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_002():
    """Test function with parameters"""
    source = """func add(a: int, b: int) -> int { return a + b; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_003():
    """Test variable declaration with type annotation"""
    source = """func main() -> void { let x: int = 42; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_004():
    """Test variable declaration with type inference"""
    source = """func main() -> void { let name = "Alice"; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_005():
    """Test constant declaration"""
    source = """const PI: float = 3.14159; func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_006():
    """Test if-else statement"""
    source = """func main() -> void { 
        if (x > 0) { 
            print("positive"); 
        } else { 
            print("negative"); 
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_007():
    """Test while loop"""
    source = """func main() -> void { 
        let i = 0;
        while (i < 10) { 
            i = i + 1; 
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_008():
    """Test for loop with array"""
    source = """func main() -> void { 
        let numbers = [1, 2, 3, 4, 5];
        for (num in numbers) { 
            print(str(num)); 
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_009():
    """Test array declaration and access"""
    source = """func main() -> void { 
        let arr: [int; 3] = [1, 2, 3];
        let first = arr[0];
        arr[1] = 42;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_010():
    """Test complex expression with pipeline operator"""
    source = """func main() -> void { 
        let result = data >> process >> validate >> transform;
        let calculation = 5 >> add(3) >> multiply(2);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_011():
    """Test parser error: missing closing brace in function declaration"""
    source = """func main() -> void { let x = 1; """  # Thiếu dấu }
    expected = "Error on line 1 col 33: <EOF>"
    assert Parser(source).parse() == expected


def test_012():
    """Test empty function"""
    source = """func test() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_013():
    """Test function with single parameter"""
    source = """func greet(name: string) -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_014():
    """Test function returning int"""
    source = """func getValue() -> int { return 42; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_015():
    """Test simple variable declaration"""
    source = """func main() -> void { let x = 10; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_016():
    """Test variable with type annotation"""
    source = """func main() -> void { let x: int = 10; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_017():
    """Test string variable"""
    source = """func main() -> void { let message = "hello"; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_018():
    """Test boolean variable"""
    source = """func main() -> void { let flag = true; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_019():
    """Test float variable"""
    source = """func main() -> void { let pi = 3.14; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_020():
    """Test simple assignment"""
    source = """func main() -> void { let x = 5; x = 10; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_021():
    """Test return statement with value"""
    source = """func getNumber() -> int { return 42; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_022():
    """Test return statement without value"""
    source = """func doNothing() -> void { return; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_023():
    """Test simple if statement"""
    source = """func main() -> void { if (true) { let x = 1; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_024():
    """Test if-else statement"""
    source = """func main() -> void { if (false) { let x = 1; } else { let y = 2; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_025():
    """Test while loop"""
    source = """func main() -> void { while (true) { let x = 1; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_026():
    """Test for loop"""
    source = """func main() -> void { for (x in arr) { let y = 1; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_027():
    """Test break statement"""
    source = """func main() -> void { while (true) { break; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_028():
    """Test continue statement"""
    source = """func main() -> void { while (true) { continue; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_029():
    """Test array literal"""
    source = """func main() -> void { let arr = [1, 2, 3]; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_030():
    """Test empty array literal"""
    source = """func main() -> void { let arr = []; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_031():
    """Test function call"""
    source = """func main() -> void { test(); }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_032():
    """Test function call with arguments"""
    source = """func main() -> void { add(1, 2); }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_033():
    """Test arithmetic expression"""
    source = """func main() -> void { let result = 1 + 2; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_034():
    """Test comparison expression"""
    source = """func main() -> void { let result = x > 5; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_035():
    """Test logical expression"""
    source = """func main() -> void { let result = true && false; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_036():
    """Test parenthesized expression"""
    source = """func main() -> void { let result = (1 + 2) * 3; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_037():
    """Test array access"""
    source = """func main() -> void { let item = arr[0]; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_038():
    """Test multiple statements"""
    source = """func main() -> void { let x = 1; let y = 2; let z = x + y; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_039():
    """Test nested blocks"""
    source = """func main() -> void { { let x = 1; } }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_040():
    """Test constant declaration"""
    source = """const MAX = 100; func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_041():
    """Test multiple functions"""
    source = """func helper() -> int { return 1; } func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_042():
    """Test expression statement"""
    source = """func main() -> void { 1 + 2; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_043():
    """Test complex function with multiple parameters and nested statements"""
    source = """func calculate(a: int, b: float, name: string) -> float {
        let result: float = 0.0;
        if (a > 0) {
            result = a * b;
            let temp = result + 1.0;
            if (temp > 10.0) {
                result = temp / 2.0;
            }
        }
        return result;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_044():
    """Test multiple function declarations with different return types"""
    source = """func getInt() -> int { return 42; }
    func getFloat() -> float { return 3.14; }
    func getString() -> string { return "hello"; }
    func getBool() -> bool { return true; }
    func main() -> void { 
        let x = getInt(); 
        let y = getFloat(); 
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_045():
    """Test complex nested control structures"""
    source = """func main() -> void {
        let i = 0;
        while (i < 10) {
            if (i % 2 == 0) {
                let j = 0;
                while (j < i) {
                    if (j > 5) {
                        break;
                    }
                    let sum = i + j;
                    j = j + 1;
                }
            } else {
                while (i > 0) {
                    i = i - 1;
                    if (i == 3) {
                        continue;
                    }
                }
            }
            i = i + 1;
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_046():
    """Test complex expression with multiple operators and precedence"""
    source = """func main() -> void {
        let result = (a + b) * c - d / e % f;
        let boolean = (x > y) && (z < w) || !flag;
        let mixed = (count * 2.5) >= (limit - offset);
        let conditional = condition && value1 || value2;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_047():
    """Test array operations and function calls"""
    source = """func process(arr: [int; 10], size: int) -> int {
        let sum = 0;
        let i = 0;
        while (i < size) {
            sum = sum + arr[i];
            if (arr[i] > arr[0]) {
                sum = sum * 2;
            }
            i = i + 1;
        }
        return sum;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_048():
    """Test complex variable declarations with different types"""
    source = """const MAX_SIZE: int = 1000;
    const PI: float = 3.14159;
    const APP_NAME: string = "MyApp";
    const DEBUG: bool = true;
    
    func main() -> void {
        let numbers: [int; 5] = [1, 2, 3, 4, 5];
        let name = "default";
        let count = MAX_SIZE;
        let pi_val = PI;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_049():
    """Test error handling and complex control flow"""
    source = """func divide(a: float, b: float) -> float {
        if (b == 0.0) {
            return 0.0;
        }
        
        let result = a / b;
        
        if (result > 1000.0) {
            while (result > 100.0) {
                result = result / 10.0;
                if (result < 0.0) {
                    break;
                }
            }
        }
        
        return result;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_050():
    """Test complex string operations and concatenation"""
    source = """func formatMessage(name: string, age: int, score: float) -> string {
        let message = "User: " + name;
        message = message + ", Age: ";
        message = message + ", Score: ";
        
        if (score >= 90.0) {
            message = message + " (Excellent!)";
        } else {
            if (score >= 70.0) {
                message = message + " (Good)";
            } else {
                message = message + " (Needs improvement)";
            }
        }
        
        return message;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_051():
    """Test recursive function with complex logic"""
    source = """func fibonacci(n: int) -> int {
        if (n <= 1) {
            return n;
        }
        
        let a = fibonacci(n - 1);
        let b = fibonacci(n - 2);
        let result = a + b;
        
        return result;
    }
    
    func factorial(n: int) -> int {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_052():
    """Test comprehensive program with multiple features"""
    source = """const MAX_ITEMS: int = 100;
    const DEFAULT_NAME: string = "Unknown";
    
    func findMax(arr: [int; 10], size: int) -> int {
        let max = arr[0];
        let i = 1;
        while (i < size) {
            if (arr[i] > max) {
                max = arr[i];
            }
            i = i + 1;
        }
        return max;
    }
    
    func processData(data: [float; 5], threshold: float) -> [float; 5] {
        let result: [float; 5] = [0.0, 0.0, 0.0, 0.0, 0.0];
        let i = 0;
        while (i < 5) {
            if (data[i] >= threshold) {
                result[i] = data[i] * 1.5;
            } else {
                result[i] = data[i] / 2.0;
            }
            i = i + 1;
        }
        return result;
    }
    
    func main() -> void {
        let numbers: [int; 7] = [1, 5, 3, 9, 2, 8, 4];
        let maxValue = findMax(numbers, 7);
        let scores: [float; 4] = [85.5, 92.0, 78.5, 96.0];
        let processed = processData(scores, 80.0);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_053():
    """Test array type with zero size"""
    source = """func test() -> void { let empty: [int; 0] = []; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_054():
    """Test nested array access with complex expressions"""
    source = """func test() -> void { 
        let value = matrix[i + 1][j * 2 + k];
        matrix[arr[x]][y] = value;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_055():
    """Test unary operators with parentheses and precedence"""
    source = """func test() -> void { 
        let result = -(-x + y);
        let flag = !(!condition && other);
        let value = +(+5);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_056():
    """Test pipeline operator with complex expressions"""
    source = """func test() -> void { 
        let result = data >> process(arg1, arg2) >> validate >> transform(x, y, z);
        let chain = value >> func1 >> func2 >> func3;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_057():
    """Test function with no parameters but with parentheses"""
    source = """func getValue() -> int { return 42; }
    func main() -> void { let x = getValue(); }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_058():
    """Test deeply nested control structures with breaks and continues"""
    source = """func test() -> void {
        while (true) {
            for (item in collection) {
                if (condition1) {
                    while (condition2) {
                        if (condition3) {
                            break;
                        }
                        continue;
                    }
                } else {
                    if (condition4) {
                        break;
                    }
                }
            }
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_059():
    """Test array type in function parameters and return type"""
    source = """func processArray(input: [float; 10], size: int) -> [float; 10] {
        let result: [float; 10] = input;
        return result;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_060():
    """Test empty blocks in all statement types"""
    source = """func test() -> void {
        if (condition) {} else {}
        while (condition) {}
        for (item in array) {}
        {}
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_061():
    """Test complex expression precedence with all operators"""
    source = """func test() -> void {
        let result = a + b * c - d / e % f == g && h || i != j;
        let complex = (x > y) && (z <= w) || (!flag && value >= threshold);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_062():
    """Test error: missing semicolon after statement"""
    source = """func test() -> void { let x = 5 let y = 10; }"""
    expected = "Error on line 1 col 32: let"
    assert Parser(source).parse() == expected


def test_063():
    """Test constant declaration without type annotation"""
    source = """const MAX = 100; func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_064():
    """Test function parameter with array type"""
    source = """func process(data: [int; 10]) -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_065():
    """Test nested array type declarations"""
    source = """func test() -> void { 
        let matrix: [[int; 3]; 3] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_066():
    """Test assignment to array elements with complex indices"""
    source = """func test() -> void {
        let arr: [int; 5] = [1, 2, 3, 4, 5];
        arr[i * 2 + j] = value;
        arr[func_call(x, y)] = result;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_067():
    """Test pipeline operator with unary expressions"""
    source = """func test() -> void {
        let result = -x >> abs >> double;
        let flag = !condition >> validate;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_068():
    """Test chained pipeline with parentheses"""
    source = """func test() -> void {
        let result = (data >> process) >> validate >> (transform >> finalize);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_069():
    """Test for loop with complex collection expression"""
    source = """func test() -> void {
        for (item in arr1 >> filter >> map) { 
            process(item);
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_070():
    """Test return statement in different control structures"""
    source = """func test() -> int {
        if (condition) {
            return 1;
        } else {
            while (true) {
                return 2;
            }
        }
        return 0;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_071():
    """Test mixed array types in function signatures"""
    source = """func convert(ints: [int; 5], floats: [float; 3]) -> [string; 8] {
        let result: [string; 8] = ["", "", "", "", "", "", "", ""];
        return result;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_072():
    """Test complex expression with all precedence levels"""
    source = """func test() -> void {
        let result = data >> func1 || condition && value > threshold + offset * multiplier / divisor % modulus;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_073():
    """Test break and continue in nested loops"""
    source = """func test() -> void {
        for (item in collection) {
            while (condition) {
                if (should_break) {
                    break;
                }
                if (should_continue) {
                    continue;
                }
            }
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_074():
    """Test function call with pipeline as argument"""
    source = """func test() -> void {
        let result = process(data >> transform >> validate, other_param);
        let value = myFunc(x >> y, a >> b >> c, simple);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_075():
    """Test empty program with only constants"""
    source = """const A = 1; const B = 2; const C = 3;"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_076():
    """Test function with maximum parameter count"""
    source = """func complex(a: int, b: float, c: bool, d: string, e: [int; 5], f: [float; 3]) -> void {
        let result = a + b;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_077():
    """Test error: function declaration without return type"""
    source = """func test() { return 42; }"""
    expected = "Error on line 1 col 12: {"
    assert Parser(source).parse() == expected


def test_078():
    """Test constant declaration with explicit type"""
    source = """const MAX_SIZE: int = 100; func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_079():
    """Test constant declaration with type inference"""
    source = """const PI = 3.14159; func main() -> void {}"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_080():
    """Test multiple constant declarations"""
    source = """
    const A: int = 1;
    const B: float = 2.0;
    const C = true;
    func main() -> void {}
    """
    expected = "success"
    assert Parser(source).parse() == expected


def test_081():
    """Test function with no parameters and void return"""
    source = """func test() -> void { return; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_082():
    """Test function with single parameter"""
    source = """func double(x: int) -> int { return x * 2; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_083():
    """Test function with multiple parameters"""
    source = """func add(a: int, b: int, c: int) -> int { return a + b + c; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_084():
    """Test array type declarations"""
    source = """func process(arr: [int; 10]) -> void { let x = arr[0]; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_085():
    """Test nested array access"""
    source = """func main() -> void { let matrix: [[int; 3]; 3] = []; let x = matrix[0][1]; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_086():
    """Test variable declaration with type inference from array"""
    source = """func main() -> void { let numbers = [1, 2, 3, 4, 5]; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_087():
    """Test assignment to array elements"""
    source = """func main() -> void { let arr: [int; 5] = []; arr[0] = 42; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_088():
    """Test nested if-else statements"""
    source = """func main() -> void {
        if (x > 0) {
            if (y > 0) {
                let z = x + y;
            } else {
                let z = x - y;
            }
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_089():
    """Test while loop with complex condition"""
    source = """func main() -> void {
        while ((x > 0) && (y < 10) || flag) {
            x = x - 1;
            y = y + 1;
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_090():
    """Test for loop with array iteration"""
    source = """func main() -> void {
        let items = [1, 2, 3];
        for (item in items) {
            let doubled = item * 2;
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_091():
    """Test break and continue statements"""
    source = """func main() -> void {
        while (true) {
            if (condition1) {
                break;
            }
            if (condition2) {
                continue;
            }
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_092():
    """Test pipeline operator in expressions"""
    source = """func main() -> void { let result = data >> process >> transform; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_093():
    """Test complex arithmetic expressions with precedence"""
    source = """func main() -> void { let result = a + b * c - d / e % f; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_094():
    """Test logical expressions with precedence"""
    source = """func main() -> void { let result = a && b || c && d; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_095():
    """Test comparison expressions"""
    source = """func main() -> void { let result = (a >= b) && (c <= d) && (e != f); }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_096():
    """Test unary expressions"""
    source = """func main() -> void { let result = -x + !flag - +y; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_097():
    """Test function calls with various arguments"""
    source = """func main() -> void { 
        let result = func1(a, b + c, func2(d, e), arr[0]); 
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_098():
    """Test empty array literal"""
    source = """func main() -> void { let empty: [int; 0] = []; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_099():
    """Test array literal with mixed expressions"""
    source = """func main() -> void { let mixed = [x + 1, myFunc(y), z * 2]; }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_100():
    """Test comprehensive program with all constructs"""
    source = """
    const PI: float = 3.14159;
    const MAX_ITEMS = 100;
    
    func calculate(radius: float, items: [int; 5]) -> float {
        let area = PI * radius * radius;
        let sum = 0;
        
        for (item in items) {
            sum = sum + item;
        }
        
        if (sum > MAX_ITEMS) {
            return area * 2.0;
        } else {
            while (sum > 0) {
                sum = sum - 1;
                if (sum == 50) {
                    break;
                }
            }
            return area;
        }
    }
    """
    expected = "success"
    assert Parser(source).parse() == expected


def test_101():
    """Test function type as parameter - should work with updated grammar"""
    source = """func process(data: [int], callback: (int) -> bool) -> void {
        for (item in data) {
            callback(item);
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_102():
    """Test function type as return type - should work with updated grammar"""
    source = """func getProcessor() -> (int) -> bool {
        return func(x: int) -> bool { return x > 0; };
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_103():
    """Test simple function type - should work with updated grammar"""
    source = """func main() -> void {
        let processor: (int) -> bool = processNumber;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_104():
    """Test anonymous function expression - should work with updated grammar"""
    source = """func main() -> void {
        let doubler = func(x: int) -> int { return x * 2; };
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_105():
    """Test pipeline-aware function definition - should work with current grammar"""
    source = """func process(input: string) -> string {
        let result = input >> trim >> uppercase;
        return result;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_106():
    """Test higher-order function with function type parameter - should work with updated grammar"""
    source = """func map(items: [int], transform: (int) -> int) -> [int] {
        let result: [int] = [];
        for (item in items) {
            result = result + [transform(item)];
        }
        return result;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_107():
    """Test complex function type with multiple parameters - should work with updated grammar"""
    source = """func combine(fn: (int, int) -> int, a: int, b: int) -> int {
        return fn(a, b);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_108():
    """Test function returning function type - should work with updated grammar"""
    source = """func createAdder(x: int) -> (int) -> int {
        return func(y: int) -> int { return x + y; };
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_109():
    """Test pipeline with function calls - should work with current grammar"""
    source = """func main() -> void {
        let result = getData() >> processData >> validateData >> saveData;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_110():
    """Test nested function type - should work with updated grammar"""
    source = """func process(fn: ((int) -> int) -> int) -> int {
        return fn(func(x: int) -> int { return x * 2; });
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_111():
    """Test function type with void return - should work with updated grammar"""
    source = """func forEach(items: [int], action: (int) -> void) -> void {
        for (item in items) {
            action(item);
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_112():
    """Test anonymous function with complex body - should work with updated grammar"""
    source = """func main() -> void {
        let processor = func(input: string) -> string {
            if (input == "") {
                return "empty";
            }
            let processed = input >> trim >> lowercase;
            return processed;
        };
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_113():
    """Test pipeline-aware function with multiple transformations - should work with current grammar"""
    source = """func transform(data: string) -> string {
        let step1 = data >> removeSpaces;
        let step2 = step1 >> capitalize;
        let final = step2 >> addPrefix;
        return final;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_114():
    """Test function type in variable declaration - should work with updated grammar"""
    source = """func main() -> void {
        let transform: (string) -> string = processString;
        let result = transform("hello");
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_115():
    """Test function type with array parameter - should work with updated grammar"""
    source = """func processArray(items: [int], processor: ([int]) -> [int]) -> [int] {
        return processor(items);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_116():
    """Test non-parenthesized function type as parameter - spec compliant"""
    source = """func process(callback: int -> bool) -> void {
        if (callback(42)) {
            return;
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_117():
    """Test non-parenthesized function type as return type - spec compliant"""
    source = """func getProcessor() -> int -> bool {
        return func(x: int) -> bool { return x > 0; };
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_118():
    """Test non-parenthesized function type in variable declaration - spec compliant"""
    source = """func main() -> void {
        let processor: int -> bool = processNumber;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_119():
    """Test multiple non-parenthesized function types - spec compliant"""
    source = """func pipeline(f1: int -> string, f2: string -> bool) -> int -> bool {
        return func(x: int) -> bool { return f2(f1(x)); };
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_120():
    """Test mixed parenthesized and non-parenthesized function types - spec compliant"""
    source = """func test(f1: int -> bool, f2: (string) -> int) -> void {
        let result1 = f1(42);
        let result2 = f2("test");
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_121():
    """Test complex function type from spec - createPipeline example"""
    source = """func createPipeline(processor: string -> string) -> (string -> string) {
        return func(input: string) -> string {
            return input >> processor >> finalize;
        };
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_122():
    """Test right-associative function types - spec compliant"""
    source = """func test() -> int -> string -> bool {
        return func(x: int) -> string -> bool {
            return func(s: string) -> bool {
                return s == "test";
            };
        };
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_123():
    """Test function type with void return - non-parenthesized"""
    source = """func forEach(items: [int], action: int -> void) -> void {
        for (item in items) {
            action(item);
        }
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_124():
    """Test function type with array types - non-parenthesized"""
    source = """func mapArray(items: [int], transform: int -> string) -> [string] {
        let result: [string] = [];
        for (item in items) {
            result = result + [transform(item)];
        }
        return result;
    }"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_125():
    """Test nested function types - mixed parenthesized and non-parenthesized"""
    source = """func process(fn: (int -> bool) -> string) -> void {
        let checker: int -> bool = func(x: int) -> bool { return x > 0; };
        let result = fn(checker);
    }"""
    expected = "success"
    assert Parser(source).parse() == expected
