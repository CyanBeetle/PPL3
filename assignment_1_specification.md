# HLang Specification for Assignment 1

This document contains excerpts from the HLang specification relevant to completing Assignment 1, which focuses on the lexer and parser implementation.

## Program Structure

A HLang program consists of:
1. Optional constant declarations
2. Function declarations

### Example program structure:
```hlang
const PI: float = 3.14159;

func factorial(n: int) -> int {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

## Lexical Structure

### Character Set
HLang programs are written using the ASCII character set (7-bit encoding, characters 0-127).

### Comments

- **Line Comments (`//`)**: Start with `//` and continue to the end of the line.
- **Block Comments (`/* */`)**: Enclosed between `/*` and `*/`. They can span multiple lines and can be nested.

### Tokens

#### Identifiers
- Must start with a letter (a-z, A-Z) or underscore (_).
- Can be followed by any combination of letters, digits (0-9), or underscores.
- HLang is case-sensitive.
- **Valid examples**: `hello`, `_value`, `myVar123`

#### Keywords
The following are reserved keywords:

| | | | | | |
|---|---|---|---|---|---|
| `bool` | `break` | `const` | `continue` | `else` | `false` |
| `float` | `for` | `func` | `if` | `in` | `int` |
| `let` | `return` | `string` | `true` | `void` | `while` |

#### Operators

- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `==`, `!=`, `<`, `<=`, `>`, `>=`
- **Logical**: `&&`, `||`, `!`
- **Assignment**: `=`
- **Type annotation**: `:`
- **Function return type**: `->`
- **Pipeline**: `>>`

#### Separators
`(`, `)`, `[`, `]`, `{`, `}`, `,`, `;`, `.`

#### Literals

- **Integer literals**: 32-bit signed integers. A sequence of one or more digits (0-9), optionally preceded by a minus sign (`-`).
  - **Examples**: `42`, `-17`, `0`, `007`
- **Float literals**: A sequence of digits with a decimal point (`.`) and an optional exponent part (`e` or `E`).
- **String literals**: Enclosed in double quotes (`"`). Support escape sequences: `\n`, `\t`, `\r`, `\"`, `\\`.
