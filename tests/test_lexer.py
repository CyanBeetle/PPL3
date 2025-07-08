from utils import Tokenizer


def test_001():
    """Test basic identifier tokenization"""
    source = "abc"
    expected = "abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_002():
    """Test keywords recognition"""
    source = "func main if else while for let const"
    expected = "func,main,if,else,while,for,let,const,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_003():
    """Test integer literals"""
    source = "42 0 -17 007"
    expected = "42,0,-,17,007,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_004():
    """Test float literals"""
    source = "3.14 -2.5 0.0 42. 5."
    expected = "3.14,-,2.5,0.0,42.,5.,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_005():
    """Test boolean literals"""
    source = "true false"
    expected = "true,false,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_006():
    """Test unclosed string literal error"""
    source = '"Hello World'
    expected = "Unclosed String: Hello World"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_007():
    """Test illegal escape sequence error"""
    source = '"Hello \\x World"'
    expected = "Illegal Escape In String: Hello \\x"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_008():
    """Test error character (non-ASCII or invalid character)"""
    source = "let x = 5; @ invalid"
    expected = "let,x,=,5,;,Error Token @"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_009():
    """Test valid string literals with escape sequences"""
    source = '"Hello World" "Line 1\\nLine 2" "Quote: \\"text\\""'
    expected = "Hello World,Line 1\\nLine 2,Quote: \\\"text\\\",EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_009a():
    """Test string literals return content without quotes"""
    source = '"Hello World"'
    expected = "Hello World,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_009b():
    """Test empty string literal"""
    source = '""'
    expected = ",EOF"  # Empty string content
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_010():
    """Test operators and separators"""
    source = "+ - * / % == != < <= > >= && || ! = -> >> ( ) [ ] { } , ; :"
    expected = "+,-,*,/,%,==,!=,<,<=,>,>=,&&,||,!,=,->,>>,(,),[,],{,},,,;,:,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_011():
    """Test single identifier"""
    source = "variable"
    expected = "variable,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_012():
    """Test identifier with underscore"""
    source = "_private"
    expected = "_private,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_013():
    """Test identifier with numbers"""
    source = "var123"
    expected = "var123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_014():
    """Test single integer"""
    source = "123"
    expected = "123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_015():
    """Test zero integer"""
    source = "0"
    expected = "0,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_016():
    """Test single float"""
    source = "123.456"
    expected = "123.456,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_017():
    """Test float with exponent"""
    source = "1.23e5"
    expected = "1.23e5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_018():
    """Test true keyword"""
    source = "true"
    expected = "true,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_019():
    """Test false keyword"""
    source = "false"
    expected = "false,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_020():
    """Test simple string"""
    source = '"hello"'
    expected = "hello,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_021():
    """Test addition operator"""
    source = "+"
    expected = "+,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_022():
    """Test subtraction operator"""
    source = "-"
    expected = "-,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_023():
    """Test multiplication operator"""
    source = "*"
    expected = "*,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_024():
    """Test division operator"""
    source = "/"
    expected = "/,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_025():
    """Test modulo operator"""
    source = "%"
    expected = "%,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_026():
    """Test assignment operator"""
    source = "="
    expected = "=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_027():
    """Test equality operator"""
    source = "=="
    expected = "==,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_028():
    """Test not equal operator"""
    source = "!="
    expected = "!=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_029():
    """Test less than operator"""
    source = "<"
    expected = "<,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_030():
    """Test greater than operator"""
    source = ">"
    expected = ">,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_031():
    """Test left parenthesis"""
    source = "("
    expected = "(,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_032():
    """Test right parenthesis"""
    source = ")"
    expected = "),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_033():
    """Test left bracket"""
    source = "["
    expected = "[,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_034():
    """Test right bracket"""
    source = "]"
    expected = "],EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_035():
    """Test left brace"""
    source = "{"
    expected = "{,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_036():
    """Test right brace"""
    source = "}"
    expected = "},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_037():
    """Test semicolon"""
    source = ";"
    expected = ";,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_038():
    """Test comma"""
    source = ","
    expected = ",,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_039():
    """Test colon"""
    source = ":"
    expected = ":,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_040():
    """Test simple variable assignment"""
    source = "x = 5"
    expected = "x,=,5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_041():
    """Test function keyword"""
    source = "func"
    expected = "func,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_042():
    """Test return keyword"""
    source = "return"
    expected = "return,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_043():
    """Test complex arithmetic expression with mixed operators"""
    source = "x = (a + b) * 2 - 3 / 4 % 5"
    expected = "x,=,(,a,+,b,),*,2,-,3,/,4,%,5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_044():
    """Test complex boolean expression with logical operators"""
    source = "result = (x > 0) && (y < 10) || !flag"
    expected = "result,=,(,x,>,0,),&&,(,y,<,10,),||,!,flag,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_045():
    """Test mixed string literals with escape sequences"""
    source = '"First line\\nSecond line" "Tab\\tSeparated" "Quote:\\""'
    expected = "First line\\nSecond line,Tab\\tSeparated,Quote:\\\",EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_046():
    """Test function call with multiple arguments and array access"""
    source = "func(arr[0], x + y, name)"
    expected = "func,(,arr,[,0,],,,x,+,y,,,name,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_047():
    """Test complex type annotation with array and function types"""
    source = "func process(data: [int], callback: (int) -> bool) -> void"
    expected = "func,process,(,data,:,[,int,],,,callback,:,(,int,),->,bool,),->,void,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_048():
    """Test mixed number formats in complex expression"""
    source = "result = 42 + 3.14 - 255 + 200000 / 0.0015"
    expected = "result,=,42,+,3.14,-,255,+,200000,/,0.0015,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_049():
    """Test complex conditional with comparison operators"""
    source = "value = condition && true_val || false_val"
    expected = "value,=,condition,&&,true_val,||,false_val,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_050():
    """Test nested array access and member access"""
    source = "matrix[i][j] . field = obj . method()"
    expected = "matrix,[,i,],[,j,],.,field,=,obj,.,method,(,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_051():
    """Test complex for loop structure"""
    source = "for (let i = 0; i < length; i = i + 1)"
    expected = "for,(,let,i,=,0,;,i,<,length,;,i,=,i,+,1,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_052():
    """Test complex switch-case like structure"""
    source = "switch (value) { case 1: break; default: continue; }"
    expected = "switch,(,value,),{,case,1,:,break,;,default,:,continue,;,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_053():
    """Test float literal with no fractional digits after decimal point"""
    source = "42."
    expected = "42.,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_054():
    """Test invalid float literal starting with decimal point"""
    source = ".5"
    expected = ".,5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_055():
    """Test float literal with negative exponent"""
    source = "1.23e-10"
    expected = "1.23e-10,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_056():
    """Test float literal with positive exponent"""
    source = "2.5E+3"
    expected = "2.5E+3,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_057():
    """Test string with all valid escape sequences"""
    source = '"newline\\ntab\\treturn\\rquote\\"backslash\\\\"'
    expected = "newline\\ntab\\treturn\\rquote\\\"backslash\\\\,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_058():
    """Test unclosed string at end of input"""
    source = '"This string never closes'
    expected = "Unclosed String: This string never closes"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_059():
    """Test illegal escape sequence with invalid character"""
    source = '"Valid text\\q invalid"'
    expected = "Illegal Escape In String: Valid text\\q"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_060():
    """Test multiple error tokens in sequence"""
    source = "let x = 5; @ # $ invalid"
    expected = "let,x,=,5,;,Error Token @"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_061():
    """Test identifier starting with underscore and containing numbers"""
    source = "_private_var_123"
    expected = "_private_var_123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_062():
    """Test pipeline operator vs greater than operator disambiguation"""
    source = "x > y >> z"
    expected = "x,>,y,>>,z,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_063():
    """Test float literal with zero before decimal point"""
    source = "0.5"
    expected = "0.5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_064():
    """Test float literal with exponent and no fractional part"""
    source = "5.e10"
    expected = "5.e10,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_065():
    """Test string with only escape sequences"""
    source = '"\\n\\t\\r\\"\\\\"'
    expected = "\\n\\t\\r\\\"\\\\,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_066():
    """Test identifier with maximum underscore usage"""
    source = "__private__var__123__"
    expected = "__private__var__123__,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_067():
    """Test adjacent operators without spaces"""
    source = "x>=y<=z!=w==v"
    expected = "x,>=,y,<=,z,!=,w,==,v,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_068():
    """Test line comment at end of line without newline"""
    source = "let x = 5; // comment"
    expected = "let,x,=,5,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_069():
    """Test block comment spanning multiple lines"""
    source = "let /* multi\nline\ncomment */ x = 5;"
    expected = "let,x,=,5,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_070():
    """Test nested block comments"""
    source = "/* outer /* inner */ still outer */ let x = 1;"
    expected = "let,x,=,1,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_071():
    """Test unclosed string with escape sequences"""
    source = '"Hello\\nWorld'
    expected = "Unclosed String: Hello\\nWorld"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_072():
    """Test illegal escape at end of string"""
    source = '"Valid text\\z"'
    expected = "Illegal Escape In String: Valid text\\z"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_073():
    """Test arrow operator vs minus and greater than"""
    source = "x - > y -> z"
    expected = "x,-,>,y,->,z,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_074():
    """Test integer literal with leading zeros"""
    source = "007 0123 000"
    expected = "007,0123,000,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_075():
    """Test all separators in sequence"""
    source = "()[]{},.;:"
    expected = "(,),[,],{,},,,.,;,:,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_076():
    """Test string literal with all printable ASCII (without illegal escapes)"""
    source = '" !#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"'
    expected = " !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_077():
    """Test illegal escape with backslash followed by invalid character"""
    source = '"Valid text with\\]illegal escape"'
    expected = "Illegal Escape In String: Valid text with\\]"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_078():
    """Test scientific notation with uppercase E"""
    source = "1.23E+10 4.56E-5"
    expected = "1.23E+10,4.56E-5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_079():
    """Test case sensitivity of keywords vs identifiers"""
    source = "TRUE FALSE FUNC LET If Else"
    expected = "TRUE,FALSE,FUNC,LET,If,Else,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_080():
    """Test float literal with zero fractional part"""
    source = "1.0 2.000 0.0000"
    expected = "1.0,2.000,0.0000,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_081():
    """Test invalid float literals with only exponent (no integer part)"""
    source = ".5e10 .123E-5"
    expected = ".,5,e10,.,123,E,-,5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_082():
    """Test negative float literals (including invalid ones)"""
    source = "-3.14 -0.5 -.123"
    expected = "-,3.14,-,0.5,-,.,123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_083():
    """Test edge case: dot without digits"""
    source = "x.y"
    expected = "x,.,y,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_084():
    """Test all keyword combinations"""
    source = "bool break const continue else false float for func if in int let return string true void while"
    expected = "bool,break,const,continue,else,false,float,for,func,if,in,int,let,return,string,true,void,while,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_085():
    """Test identifier edge cases - single character"""
    source = "a A _ x9 Z"
    expected = "a,A,_,x9,Z,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_086():
    """Test operator precedence in tokenization"""
    source = ">>= >= = = >>> << <= ="
    expected = ">>,=,>=,=,=,>>,>,<,<,<=,=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_087():
    """Test string with maximum valid escape sequences"""
    source = '"\\n\\t\\r\\"\\\\"'  
    expected = "\\n\\t\\r\\\"\\\\,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_088():
    """Test various illegal escape sequences"""
    source = '"test\\a"'
    expected = "Illegal Escape In String: test\\a"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_089():
    """Test various illegal escape sequences - backspace"""
    source = '"test\\b"'
    expected = "Illegal Escape In String: test\\b"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_090():
    """Test various illegal escape sequences - form feed"""
    source = '"test\\f"'
    expected = "Illegal Escape In String: test\\f"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_091():
    """Test various illegal escape sequences - vertical tab"""
    source = '"test\\v"'
    expected = "Illegal Escape In String: test\\v"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_092():
    """Test unclosed string without newline"""
    source = '"line1 and more text'
    expected = "Unclosed String: line1 and more text"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_093():
    """Test string with mixed valid content"""
    source = '"Mixed123!@#$%^&*()_+-={}[]|:;<>?,./"'
    expected = "Mixed123!@#$%^&*()_+-={}[]|:;<>?,./,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_094():
    """Test integer literal bounds - large numbers"""
    source = "2147483647 0000000001 999999999"
    expected = "2147483647,0000000001,999999999,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_095():
    """Test complex float variations (including invalid ones)"""
    source = "1.0e10 1.0E10 1.0e+10 1.0E-10 .5e5 5.e5"
    expected = "1.0e10,1.0E10,1.0e+10,1.0E-10,.,5,e5,5.e5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_096():
    """Test edge case operators - not equal vs not"""
    source = "!= ! == ="
    expected = "!=,!,==,=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_097():
    """Test comment edge cases - empty comments"""
    source = "x // \ny //"
    expected = "x,y,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_098():
    """Test comment edge cases - nested block comments"""
    source = "/* outer /* inner1 /* inner2 */ inner1 */ outer */ result"
    expected = "result,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_099():
    """Test error token - special characters"""
    source = "valid ~ invalid"
    expected = "valid,Error Token ~"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_100():
    """Test comprehensive mixed tokenization"""
    source = 'let x: int = 42; let y: float = 3.14; let name: string = "Hello"; let flag: bool = true;'
    expected = "let,x,:,int,=,42,;,let,y,:,float,=,3.14,;,let,name,:,string,=,Hello,;,let,flag,:,bool,=,true,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_101():
    """Test lexer support for function type arrows"""
    source = "(int) -> bool"
    expected = "(,int,),->,bool,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_102():
    """Test lexer support for complex function type with multiple parameters"""
    source = "(int, string) -> float"
    expected = "(,int,,,string,),->,float,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_103():
    """Test lexer support for nested function types"""
    source = "((int) -> bool) -> string"
    expected = "(,(,int,),->,bool,),->,string,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_104():
    """Test lexer support for function type with void return"""
    source = "(string) -> void"
    expected = "(,string,),->,void,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_105():
    """Test lexer support for function type with array parameters"""
    source = "([int; 5]) -> [string; 10]"
    expected = "(,[,int,;,5,],),->,[,string,;,10,],EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_106():
    """Test lexer support for anonymous function expression"""
    source = "func(x: int) -> int { return x * 2; }"
    expected = "func,(,x,:,int,),->,int,{,return,x,*,2,;,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_107():
    """Test lexer support for pipeline operator in complex expressions"""
    source = "data >> process >> validate >> transform"
    expected = "data,>>,process,>>,validate,>>,transform,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_108():
    """Test lexer support for function type in variable declaration"""
    source = "let callback: (int) -> bool = myFunc;"
    expected = "let,callback,:,(,int,),->,bool,=,myFunc,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_109():
    """Test lexer support for function type in function parameters"""
    source = "func process(data: [int], transform: (int) -> string) -> void"
    expected = "func,process,(,data,:,[,int,],,,transform,:,(,int,),->,string,),->,void,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_110():
    """Test lexer support for function returning function type"""
    source = "func getProcessor() -> (int) -> bool"
    expected = "func,getProcessor,(,),->,(,int,),->,bool,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_111():
    """Test lexer support for anonymous function with complex body"""
    source = 'func(input: string) -> string { if (input == "") { return "empty"; } return input; }'
    expected = "func,(,input,:,string,),->,string,{,if,(,input,==,,),{,return,empty,;,},return,input,;,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_112():
    """Test lexer support for higher-order function syntax"""
    source = "func map(items: [int], transform: (int) -> int) -> [int]"
    expected = "func,map,(,items,:,[,int,],,,transform,:,(,int,),->,int,),->,[,int,],EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_113():
    """Test lexer support for pipeline with function calls"""
    source = "input >> validate >> clean >> format"
    expected = "input,>>,validate,>>,clean,>>,format,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_114():
    """Test lexer support for complex function type with multiple arrows"""
    source = "func createPipeline(processor: string -> string) -> (string -> string)"
    expected = "func,createPipeline,(,processor,:,string,->,string,),->,(,string,->,string,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_115():
    """Test lexer support for function type without parentheses"""
    source = "string -> string"
    expected = "string,->,string,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_116():
    """Test lexer disambiguation between arrow and pipeline operators"""
    source = "x -> y >> z"
    expected = "x,->,y,>>,z,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_117():
    """Test lexer support for anonymous function assignment"""
    source = "let doubler = func(x: int) -> int { return x * 2; };"
    expected = "let,doubler,=,func,(,x,:,int,),->,int,{,return,x,*,2,;,},;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_118():
    """Test lexer support for function type with no parameters"""
    source = "() -> int"
    expected = "(,),->,int,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_119():
    """Test lexer support for complex pipeline expression"""
    source = "data >> func1(arg1, arg2) >> func2 >> func3(arg3)"
    expected = "data,>>,func1,(,arg1,,,arg2,),>>,func2,>>,func3,(,arg3,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected


def test_120():
    """Test lexer support for function type in return statement"""
    source = "return func(x: int) -> bool { return x > 0; };"
    expected = "return,func,(,x,:,int,),->,bool,{,return,x,>,0,;,},;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected