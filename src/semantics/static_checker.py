"""
Static Semantic Checker for HLang Programming Language
"""

from functools import reduce
from typing import Dict, List, Set, Optional, Any, Tuple, Union, NamedTuple
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode, Program, ConstDecl, FuncDecl, Param, VarDecl, Assignment, 
    IfStmt, WhileStmt, ForStmt, ReturnStmt, BreakStmt, ContinueStmt, 
    ExprStmt, BlockStmt, IntType, FloatType, BoolType, StringType, 
    VoidType, ArrayType, IdLValue, ArrayAccessLValue, BinaryOp, UnaryOp, 
    FunctionCall, ArrayAccess, Identifier, IntegerLiteral, FloatLiteral, 
    BooleanLiteral, StringLiteral, ArrayLiteral
)
from .static_error import (
    StaticError, Redeclared, Undeclared, TypeMismatchInExpression,
    TypeMismatchInStatement, TypeCannotBeInferred, NoEntryPoint,
    MustInLoop
)

# Import marker classes with different names to avoid conflict  
from .static_error import Identifier as IdentifierMarker, Function as FunctionMarker


# ============================================================================
# TASK 3.1: Symbol Table Design & Implementation
# ============================================================================

class SymbolKind:
    """Constants for different kinds of symbols."""
    VARIABLE = "Variable"
    CONSTANT = "Constant"
    FUNCTION = "Function"
    PARAMETER = "Parameter"


class SymbolInfo(NamedTuple):
    """Information stored about each symbol in the symbol table."""
    name: str
    kind: SymbolKind
    type_info: Any  # Type node from AST
    line: Optional[int] = None
    column: Optional[int] = None


class Scope:
    """Represents a single scope in the symbol table."""
    
    def __init__(self, scope_name: str = ""):
        self.scope_name = scope_name
        self.symbols: Dict[str, SymbolInfo] = {}
    
    def declare(self, symbol: SymbolInfo) -> bool:
        """
        Declare a symbol in this scope.
        Returns True if successful, False if already declared.
        """
        if symbol.name in self.symbols:
            return False
        self.symbols[symbol.name] = symbol
        return True
    
    def lookup(self, name: str) -> Optional[SymbolInfo]:
        """Look up a symbol in this scope only."""
        return self.symbols.get(name)
    
    def contains(self, name: str) -> bool:
        """Check if symbol exists in this scope."""
        return name in self.symbols


class SymbolTable:
    """
    Symbol table with scope stack for managing nested scopes.
    Supports shadowing and proper scope resolution.
    """
    
    def __init__(self):
        self.scope_stack: List[Scope] = []
        self.global_scope = Scope("global")
        self.scope_stack.append(self.global_scope)
    
    def enter_scope(self, scope_name: str = ""):
        """Enter a new scope."""
        new_scope = Scope(scope_name)
        self.scope_stack.append(new_scope)
    
    def exit_scope(self):
        """Exit the current scope."""
        if len(self.scope_stack) > 1:  # Keep global scope
            self.scope_stack.pop()
    
    def current_scope(self) -> Scope:
        """Get the current (top) scope."""
        return self.scope_stack[-1]
    
    def declare(self, symbol: SymbolInfo) -> bool:
        """
        Declare a symbol in the current scope.
        Returns True if successful, False if redeclared.
        """
        return self.current_scope().declare(symbol)
    
    def lookup(self, name: str) -> Optional[SymbolInfo]:
        """
        Look up a symbol starting from current scope up to global.
        Implements proper shadowing resolution.
        """
        for scope in reversed(self.scope_stack):
            if symbol := scope.lookup(name):
                return symbol
        return None
    
    def lookup_current_scope(self, name: str) -> Optional[SymbolInfo]:
        """Look up a symbol only in the current scope."""
        return self.current_scope().lookup(name)
    
    def is_global_scope(self) -> bool:
        """Check if we're currently in global scope."""
        return len(self.scope_stack) == 1


class StaticChecker(ASTVisitor):
    """
    Static semantic analyzer for HLang.
    Performs type checking, scope analysis, and error detection.
    """
    
    def __init__(self):
        # Task 3.1: Symbol table for scope management
        self.symbol_table = SymbolTable()
        
        # Task 3.3: Error reporting framework
        self.errors: List[StaticError] = []
        self.continue_on_error = True  # Continue analysis after finding errors
        
        # Task 3.9: Loop context tracking for break/continue
        self.loop_depth = 0
        
        # Task 3.6: Track main function for entry point validation
        self.main_function_found = False
        
        # Task 3.10: Current function return type for return statement validation
        self.current_function_return_type: Optional[Any] = None
    
    # ========================================================================
    # TASK 3.3: Error Reporting Framework
    # ========================================================================
    
    def add_error(self, error: StaticError):
        """Add an error to the error list with context information."""
        self.errors.append(error)
    
    def add_error_at_node(self, error: StaticError, node: ASTNode):
        """Add an error with location information from AST node."""
        if hasattr(node, 'line'):
            error.line = node.line
        if hasattr(node, 'column'):
            error.column = node.column
        self.add_error(error)
    
    def has_errors(self) -> bool:
        """Check if any errors were found."""
        return len(self.errors) > 0
    
    def get_errors(self) -> List[StaticError]:
        """Get all collected errors."""
        return self.errors.copy()
    
    def get_error_count(self) -> int:
        """Get the number of errors found."""
        return len(self.errors)
    
    def clear_errors(self):
        """Clear all collected errors."""
        self.errors.clear()
    
    def should_continue_analysis(self) -> bool:
        """Determine if analysis should continue after errors."""
        return self.continue_on_error
    
    def set_continue_on_error(self, continue_flag: bool):
        """Set whether to continue analysis after finding errors."""
        self.continue_on_error = continue_flag
    
    def format_error_report(self) -> str:
        """Format all errors into a comprehensive report."""
        if not self.errors:
            return "No errors found."
        
        report = f"Found {len(self.errors)} error(s):\n"
        for i, error in enumerate(self.errors, 1):
            location = ""
            if hasattr(error, 'line') and error.line is not None:
                location = f" (line {error.line}"
                if hasattr(error, 'column') and error.column is not None:
                    location += f", column {error.column}"
                location += ")"
            
            report += f"{i}. {error}{location}\n"
        
        return report
    
    def check_program(self, ast: Program):
        """
        Main entry point for static semantic checking.
        Performs comprehensive semantic analysis on the given AST.
        """
        # Clear any previous errors
        self.clear_errors()
        
        # Reset state
        self.main_function_found = False
        self.loop_depth = 0
        self.current_function_return_type = None
        
        # Start analysis
        try:
            self.visit_program(ast)
            
            # If no errors found, analysis passed
            if not self.has_errors():
                return
            
            # If errors found, raise the first one
            raise self.errors[0]
            
        except StaticError:
            # Re-raise static errors
            raise
        except Exception as e:
            # Convert unexpected errors to static errors
            raise StaticError(f"Internal error during semantic analysis: {str(e)}")
    
    def print_error_summary(self):
        """Print a summary of all errors found."""
        print(self.format_error_report())
    
    # ========================================================================
    # TASK 3.2: Type System Infrastructure
    # ========================================================================
    
    def are_types_equal(self, type1: Any, type2: Any) -> bool:
        """Check if two types are exactly equal."""
        if type1 is None or type2 is None:
            return type1 is type2
        
        if type(type1) != type(type2):
            return False
        
        if isinstance(type1, ArrayType):
            return (self.are_types_equal(type1.element_type, type2.element_type) 
                   and type1.size == type2.size)
        
        return True
    
    def is_numeric_type(self, type_node: Any) -> bool:
        """Check if a type is numeric (int or float)."""
        return isinstance(type_node, (IntType, FloatType))
    
    def is_integer_type(self, type_node: Any) -> bool:
        """Check if a type is integer."""
        return isinstance(type_node, IntType)
    
    def is_float_type(self, type_node: Any) -> bool:
        """Check if a type is float."""
        return isinstance(type_node, FloatType)
    
    def is_boolean_type(self, type_node: Any) -> bool:
        """Check if a type is boolean."""
        return isinstance(type_node, BoolType)
    
    def is_string_type(self, type_node: Any) -> bool:
        """Check if a type is string."""
        return isinstance(type_node, StringType)
    
    def is_void_type(self, type_node: Any) -> bool:
        """Check if a type is void."""
        return isinstance(type_node, VoidType)
    
    def check_all_paths_return(self, statements: List[Any], return_type: Any) -> bool:
        """
        Check if all execution paths in the given statements return a value.
        Returns True if all paths return, False otherwise.
        """
        if not statements:
            return False
        
        # Check each statement for return behavior
        for i, stmt in enumerate(statements):
            if isinstance(stmt, ReturnStmt):
                # Found a return statement - remaining statements unreachable
                return True
            elif isinstance(stmt, IfStmt):
                # For if-statements, all branches must return
                then_returns = self.check_all_paths_return([stmt.then_stmt], return_type) if hasattr(stmt, 'then_stmt') else False
                else_returns = self.check_all_paths_return([stmt.else_stmt], return_type) if hasattr(stmt, 'else_stmt') and stmt.else_stmt else False
                
                # Also check elif branches if they exist
                elif_returns = True
                if hasattr(stmt, 'elif_branches') and stmt.elif_branches:
                    for _, elif_block in stmt.elif_branches:
                        if not self.check_all_paths_return([elif_block], return_type):
                            elif_returns = False
                            break
                
                # If this if-statement covers all paths and they all return, we're good
                if then_returns and else_returns and elif_returns and stmt.else_stmt is not None:
                    return True
            elif isinstance(stmt, BlockStmt):
                # Check if the block returns on all paths
                if self.check_all_paths_return(stmt.statements, return_type):
                    return True
            elif isinstance(stmt, WhileStmt) or isinstance(stmt, ForStmt):
                # Loops don't guarantee execution, so can't rely on them for returns
                continue
        
        # No guaranteed return found
        return False

    def is_array_type(self, type_node: Any) -> bool:
        """Check if a type is array."""
        return isinstance(type_node, ArrayType)
    
    def get_array_element_type(self, array_type: ArrayType) -> Any:
        """Get the element type of an array type."""
        return array_type.element_type
    
    def get_array_size(self, array_type: ArrayType) -> int:
        """Get the size of an array type."""
        return array_type.size
    
    def is_compatible_for_assignment(self, target_type: Any, source_type: Any) -> bool:
        """Check if source type can be assigned to target type."""
        # For now, require exact type match (no implicit conversions)
        return self.are_types_equal(target_type, source_type)
    
    def can_apply_binary_op(self, op: str, left_type: Any, right_type: Any) -> Tuple[bool, Optional[Any]]:
        """
        Check if binary operation can be applied to given types.
        Returns (is_valid, result_type).
        """
        # Arithmetic operators: +, -, *, /, %
        if op in ['+', '-', '*', '/']:
            if self.is_numeric_type(left_type) and self.is_numeric_type(right_type):
                # If either operand is float, result is float
                if self.is_float_type(left_type) or self.is_float_type(right_type):
                    return True, FloatType()
                else:
                    return True, IntType()
            # Special case: string concatenation
            elif op == '+' and self.is_string_type(left_type) and self.is_string_type(right_type):
                return True, StringType()
            else:
                return False, None
        
        # Modulo operator: % (only for integers)
        elif op == '%':
            if self.is_integer_type(left_type) and self.is_integer_type(right_type):
                return True, IntType()
            else:
                return False, None
        
        # Comparison operators: <, <=, >, >=
        elif op in ['<', '<=', '>', '>=']:
            if self.is_numeric_type(left_type) and self.is_numeric_type(right_type):
                return True, BoolType()
            else:
                return False, None
        
        # Equality operators: ==, !=
        elif op in ['==', '!=']:
            if self.are_types_equal(left_type, right_type):
                return True, BoolType()
            else:
                return False, None
        
        # Logical operators: &&, ||
        elif op in ['&&', '||']:
            if self.is_boolean_type(left_type) and self.is_boolean_type(right_type):
                return True, BoolType()
            else:
                return False, None
        
        # Pipeline operator: >>
        elif op == '>>':
            return self.can_apply_pipeline_op(left_type, right_type)
        
        else:
            return False, None
    
    def can_apply_unary_op(self, op: str, operand_type: Any) -> Tuple[bool, Optional[Any]]:
        """
        Check if unary operation can be applied to given type.
        Returns (is_valid, result_type).
        """
        if op in ['+', '-']:
            if self.is_numeric_type(operand_type):
                return True, operand_type
            else:
                return False, None
        elif op == '!':
            if self.is_boolean_type(operand_type):
                return True, BoolType()
            else:
                return False, None
        else:
            return False, None
    
    def can_apply_pipeline_op(self, left_type: Any, right_type: Any) -> Tuple[bool, Optional[Any]]:
        """
        Check if pipeline operation (>>) can be applied.
        This is a placeholder as the logic is now in handle_pipeline_operation.
        """
        return True, None

    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        """
        Visit binary operation - Task 3.11.
        Handles type checking for all binary operations.
        """
        op = node.op
        
        if op == '>>':
            return self.handle_pipeline_operation(node)

        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        
        if left_type is None or right_type is None:
            return None
        
        is_valid, result_type = self.can_apply_binary_op(op, left_type, right_type)
        
        if not is_valid:
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        return result_type
    
    def handle_pipeline_operation(self, node: "BinaryOp") -> Optional[Any]:
        """
        Handle pipeline operation: left >> right
        """
        left_type = self.visit(node.left)
        if left_type is None:
            return None

        # Case 1: Right side is a function identifier (e.g., value >> func)
        if isinstance(node.right, Identifier):
            func_name = node.right.name
            func_symbol = self.symbol_table.lookup(func_name)

            if func_symbol is None or func_symbol.kind != SymbolKind.FUNCTION:
                self.add_error_at_node(Undeclared(FunctionMarker(), func_name), node.right)
                return None

            func_info = func_symbol.type_info
            param_types = func_info.get('param_types', [])
            
            if len(param_types) != 1:
                self.add_error_at_node(TypeMismatchInExpression(node), node)
                return None

            if not self.are_types_equal(left_type, param_types[0]):
                self.add_error_at_node(TypeMismatchInExpression(node), node)
                return None
            
            return func_info.get('return_type')

        # Case 2: Right side is a function call (e.g., value >> func(arg1, arg2))
        elif isinstance(node.right, FunctionCall):
            if not isinstance(node.right.function, Identifier):
                self.add_error_at_node(TypeMismatchInExpression(node), node.right)
                return None

            func_name = node.right.function.name
            func_symbol = self.symbol_table.lookup(func_name)

            if func_symbol is None or func_symbol.kind != SymbolKind.FUNCTION:
                self.add_error_at_node(Undeclared(FunctionMarker(), func_name), node.right.function)
                return None

            func_info = func_symbol.type_info
            param_types = func_info.get('param_types', [])

            # Prepend the piped value's type to the arguments
            arg_types = [left_type] + [self.visit(arg) for arg in node.right.args]
            
            if any(t is None for t in arg_types):
                return None # Error in argument expression

            if len(arg_types) != len(param_types):
                self.add_error_at_node(TypeMismatchInExpression(node), node)
                return None

            for arg_type, param_type in zip(arg_types, param_types):
                if not self.are_types_equal(arg_type, param_type):
                    self.add_error_at_node(TypeMismatchInExpression(node), node)
                    return None
            
            return func_info.get('return_type')

        else:
            # Right side is not a valid function for pipeline
            self.add_error_at_node(TypeMismatchInExpression(node), node)
            return None
        
        # Case 1: value >> function_identifier
        if isinstance(node.right, Identifier):
            func_name = node.right.name
            func_symbol = self.symbol_table.lookup(func_name)
            
            if func_symbol is None:
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None

            if func_symbol.kind != SymbolKind.FUNCTION:
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None            # Check if function signature is compatible
            func_type = func_symbol.type_info
            if not hasattr(func_type, 'param_types') or not func_type.param_types:
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
            
            # Check if left type matches first parameter
            if not self.are_types_equal(left_type, func_type.param_types[0]):
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
            
            # Check if function expects exactly one parameter
            if len(func_type.param_types) != 1:
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
            
            return func_type.return_type
        
        # Case 2: value >> function_call(other_args) - partial application
        elif isinstance(node.right, FunctionCall):
            # Get the function being called
            if not isinstance(node.right.function, Identifier):
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
            
            func_name = node.right.function.name
            func_symbol = self.symbol_table.lookup(func_name)
            
            if func_symbol is None:
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
            
            if func_symbol.kind != SymbolKind.FUNCTION:
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
            
            # Check function signature compatibility
            func_type = func_symbol.type_info
            if not hasattr(func_type, 'param_types'):
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
            
            # Check if left type matches first parameter
            if not func_type.param_types or not self.are_types_equal(left_type, func_type.param_types[0]):
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
            
            # Check if remaining arguments match remaining parameters
            provided_args = node.right.arguments
            expected_params = func_type.param_types[1:]  # Skip first parameter (piped value)
            
            if len(provided_args) != len(expected_params):
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
            
            # Type check the provided arguments
            for i, arg in enumerate(provided_args):
                arg_type = self.visit(arg)
                if arg_type is None or not self.are_types_equal(arg_type, expected_params[i]):
                    self.add_error_at_node(
                        TypeMismatchInExpression(node),
                        node
                    )
                    return None
            
            return func_type.return_type
        
        else:
            # Right side is not a function identifier or function call
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
    
    def infer_array_literal_type(self, elements: List[Any]) -> Tuple[bool, Optional[Any]]:
        """
        Infer type of array literal from its elements.
        Returns (success, array_type).
        """
        if not elements:
            return False, None  # Cannot infer type of empty array
        
        # Get type of first element
        first_element_type = self.visit(elements[0])
        if first_element_type is None:
            return False, None
        
        # Check that all elements have the same type
        for element in elements[1:]:
            element_type = self.visit(element)
            if not self.are_types_equal(first_element_type, element_type):
                return False, None
        
        # Create array type
        array_size = len(elements)
        array_type = ArrayType(first_element_type, array_size)
        return True, array_type
    
    def check_function_signature_compatibility(self, func_name: str, arg_types: List[Any]) -> Tuple[bool, Optional[Any]]:
        """
        Check if function call arguments are compatible with function signature.
        Returns (is_valid, return_type).
        """
        func_symbol = self.symbol_table.lookup(func_name)
        if func_symbol is None or func_symbol.kind != SymbolKind.FUNCTION:
            return False, None
        
        # Extract function information (this will be detailed in Task 3.5)
        # For now, this is a placeholder
        return True, None
    
    # ========================================================================
    # TASK 3.15: Array Type Compatibility Enhancement
    # ========================================================================
    
    def check_array_assignment_compatibility(self, target_array_type: ArrayType, source_array_type: ArrayType) -> bool:
        """
        Check if source array type can be assigned to target array type.
        Arrays must match exactly in both element type and size.
        """
        # Check element type compatibility
        if not self.are_types_equal(target_array_type.element_type, source_array_type.element_type):
            return False
        
        # Check size compatibility
        if target_array_type.size != source_array_type.size:
            return False
        
        return True
    
    def validate_array_literal_assignment(self, target_type: Any, array_literal: "ArrayLiteral") -> bool:
        """
        Validate that an array literal can be assigned to the target type.
        """
        if not self.is_array_type(target_type):
            return False
        
        # Check if literal has correct number of elements
        if len(array_literal.elements) != target_type.size:
            return False
        
        # Check that all elements are compatible with target element type
        target_element_type = target_type.element_type
        for element in array_literal.elements:
            element_type = self.visit(element)
            if element_type is None or not self.are_types_equal(target_element_type, element_type):
                return False
        
        return True
    
    def check_multidimensional_array_compatibility(self, type1: Any, type2: Any) -> bool:
        """
        Check compatibility for multi-dimensional arrays.
        """
        if not (self.is_array_type(type1) and self.is_array_type(type2)):
            return False
        
        # Check sizes match
        if type1.size != type2.size:
            return False
        
        # Check element types
        elem1 = type1.element_type
        elem2 = type2.element_type
        
        # If elements are also arrays, check recursively
        if self.is_array_type(elem1) and self.is_array_type(elem2):
            return self.check_multidimensional_array_compatibility(elem1, elem2)
        else:
            return self.are_types_equal(elem1, elem2)
    
    def is_compatible_for_assignment(self, target_type: Any, source_type: Any) -> bool:
        """
        Enhanced assignment compatibility checking with array support.
        """
        # Handle array type compatibility
        if self.is_array_type(target_type) and self.is_array_type(source_type):
            return self.check_array_assignment_compatibility(target_type, source_type)
        
        # For non-array types, require exact match (no implicit conversions)
        return self.are_types_equal(target_type, source_type)
    
    # ========================================================================
    # TASK 3.16: Type Inference Failure Detection Enhancement
    # ========================================================================
    
    def detect_circular_type_dependency(self, node: ASTNode, visited: set = None) -> bool:
        """
        Detect circular dependencies in type inference.
        This is a simplified version - full implementation would require more context.
        """
        if visited is None:
            visited = set()
        
        node_id = id(node)
        if node_id in visited:
            return True  # Circular dependency detected
        
        visited.add(node_id)
        # In a full implementation, we would traverse dependent nodes
        return False
    
    def can_infer_type_from_context(self, node: ASTNode) -> Tuple[bool, Optional[Any]]:
        """
        Determine if a type can be inferred from the given context.
        """
        if isinstance(node, ArrayLiteral):
            if not node.elements:
                return False, None  # Empty array
            
            # Check if all elements have the same type
            element_types = []
            for element in node.elements:
                element_type = self.visit(element)
                if element_type is None:
                    return False, None
                element_types.append(element_type)
            
            # Check consistency
            first_type = element_types[0]
            for elem_type in element_types[1:]:
                if not self.are_types_equal(first_type, elem_type):
                    return False, None  # Inconsistent types
            
            return True, ArrayType(first_type, len(node.elements))
        
        # For other node types, type can usually be inferred
        return True, None
    
    def visit_array_literal(self, node: "ArrayLiteral", o: Any = None):
        """
        Enhanced array literal visitor with better type inference.
        """
        if not node.elements:
            # Empty array - cannot infer type without context
            self.add_error_at_node(
                TypeCannotBeInferred(node),
                node
            )
            return None
        
        # Check for type inference ability
        can_infer, inferred_type = self.can_infer_type_from_context(node)
        if not can_infer:
            if inferred_type is None:
                self.add_error_at_node(
                    TypeCannotBeInferred(node),
                    node
                )
            else:
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
            return None
        
        # Use existing inference logic
        success, array_type = self.infer_array_literal_type(node.elements)
        if not success:
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        return array_type
    
    # ========================================================================
    # TASK 3.17: Function Parameter/Argument Matching Enhancement
    # ========================================================================
    
    def check_function_signature_match(self, func_symbol: SymbolInfo, args: List[Any]) -> Tuple[bool, List[str]]:
        """
        Comprehensive function signature matching with detailed error reporting.
        Returns (is_valid, error_messages).
        """
        errors = []
        func_info = func_symbol.type_info
        expected_param_types = func_info['param_types']
        param_names = func_info['param_names']
        
        # Check argument count
        if len(args) != len(expected_param_types):
            if len(args) < len(expected_param_types):
                errors.append(f"Too few arguments: expected {len(expected_param_types)}, got {len(args)}")
            else:
                errors.append(f"Too many arguments: expected {len(expected_param_types)}, got {len(args)}")
            return False, errors
        
        # Check argument types
        for i, (arg, expected_type) in enumerate(zip(args, expected_param_types)):
            arg_type = self.visit(arg)
            if arg_type is None:
                errors.append(f"Invalid argument {i+1}")
                continue
            
            if not self.are_types_equal(arg_type, expected_type):
                param_name = param_names[i] if i < len(param_names) else f"param{i+1}"
                errors.append(f"Argument {i+1} ({param_name}): expected {self.type_to_string(expected_type)}, got {self.type_to_string(arg_type)}")
        
        return len(errors) == 0, errors
    
    def validate_function_call_context(self, node: "FunctionCall", func_symbol: SymbolInfo) -> bool:
        """
        Validate function call in its context (expression vs statement).
        """
        func_info = func_symbol.type_info
        return_type = func_info['return_type']
        
        # If return type is void, function should only be called as statement
        # This check would need context about whether we're in expression or statement
        # For now, we allow void functions in expressions and catch it elsewhere
        return True
    
    def check_nested_function_calls(self, node: "FunctionCall") -> bool:
        """
        Validate nested function calls for type consistency.
        """
        # Check each argument - if it's a function call, ensure it returns appropriate type
        for arg in node.args:
            if isinstance(arg, FunctionCall):
                arg_return_type = self.visit(arg)
                if arg_return_type is None:
                    return False
                # Additional nested call validations can be added here
        
        return True
    
    def visit_function_call(self, node: "FunctionCall", o: Any = None):
        """
        Enhanced function call visitor with comprehensive validation.
        """
        # The function should be an identifier
        if not isinstance(node.function, Identifier):
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        function_name = node.function.name
        
        # Look up function
        func_symbol = self.symbol_table.lookup(function_name)
        if func_symbol is None:
            self.add_error_at_node(
                Undeclared(FunctionMarker(), function_name),
                node
            )
            return None
        
        if func_symbol.kind != SymbolKind.FUNCTION:
            self.add_error_at_node(
                Undeclared(FunctionMarker(), function_name),
                node
            )
            return None
        
        # Validate nested function calls
        if not self.check_nested_function_calls(node):
            return None
        
        # Comprehensive signature matching
        is_valid, error_messages = self.check_function_signature_match(func_symbol, node.args)
        if not is_valid:
            # For now, just report the first error as TypeMismatchInExpression
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        # Validate context
        if not self.validate_function_call_context(node, func_symbol):
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        # Return the function's return type
        func_info = func_symbol.type_info
        return func_info['return_type']
    
    def check_function_signature_compatibility(self, func_name: str, arg_types: List[Any]) -> Tuple[bool, Optional[Any]]:
        """
        Enhanced function signature compatibility checking.
        """
        func_symbol = self.symbol_table.lookup(func_name)
        if func_symbol is None or func_symbol.kind != SymbolKind.FUNCTION:
            return False, None
        
        func_info = func_symbol.type_info
        expected_param_types = func_info['param_types']
        return_type = func_info['return_type']
        
        # Check argument count and types
        if len(arg_types) != len(expected_param_types):
            return False, None
        
        for arg_type, expected_type in zip(arg_types, expected_param_types):
            if not self.are_types_equal(arg_type, expected_type):
                return False, None
        
        return True, return_type
    
    def type_to_string(self, type_node: Any) -> str:
        """Convert a type node to its string representation."""
        if isinstance(type_node, IntType):
            return "int"
        elif isinstance(type_node, FloatType):
            return "float"
        elif isinstance(type_node, BoolType):
            return "bool"
        elif isinstance(type_node, StringType):
            return "string"
        elif isinstance(type_node, VoidType):
            return "void"
        elif isinstance(type_node, ArrayType):
            element_type_str = self.type_to_string(type_node.element_type)
            return f"[{element_type_str}; {type_node.size}]"
        else:
            return "unknown"
    
    # ========================================================================
    # Placeholder visitor methods (to be implemented in subsequent tasks)
    # ========================================================================
    
    def visit_program(self, node: "Program", o: Any = None):
        """Visit program node - entry point for semantic analysis."""
        # Task 3.4: Process constant declarations
        for const_decl in node.const_decls:
            self.visit(const_decl)
        
        # Task 3.5: Process function declarations (two-pass approach)
        # First pass: Register all function signatures for forward declarations
        for func_decl in node.func_decls:
            self.register_function_signature(func_decl)
        
        # Second pass: Check function bodies
        for func_decl in node.func_decls:
            self.check_function_body(func_decl)
        
        # Task 3.6: Check for main function
        if not self.main_function_found:
            self.add_error(NoEntryPoint())
        
        return None
    
    def visit_const_decl(self, node: "ConstDecl", o: Any = None):
        """
        Visit constant declaration - Task 3.4.
        Handles global constant declarations and redeclaration checking.
        """
        # Check if we're in global scope (constants are only allowed globally)
        if not self.symbol_table.is_global_scope():
            # This shouldn't happen if the parser is correct, but add safety check
            self.add_error_at_node(
                TypeMismatchInStatement(node), 
                node
            )
            return
        
        # Check for redeclaration in current scope
        if self.symbol_table.lookup_current_scope(node.name):
            existing_symbol = self.symbol_table.lookup_current_scope(node.name)
            self.add_error_at_node(
                Redeclared("Constant", node.name),
                node
            )
            return
        
        # Check for any existing symbol with same name in any scope
        existing_symbol = self.symbol_table.lookup(node.name)
        if existing_symbol:
            self.add_error_at_node(
                Redeclared("Constant", node.name),
                node
            )
            return
        
        # Evaluate the constant value to get its type
        value_type = self.visit(node.value)
        if value_type is None:
            # Error in value expression, already reported
            return
        
        # Check type annotation compatibility if provided
        declared_type = None
        if node.type_annotation:
            declared_type = self.visit(node.type_annotation)
            if not self.are_types_equal(declared_type, value_type):
                self.add_error_at_node(
                    TypeMismatchInStatement(node),
                    node
                )
                return
        
        # Use declared type if available, otherwise inferred type
        final_type = declared_type if declared_type else value_type
        
        # Register the constant in the symbol table
        symbol_info = SymbolInfo(
            name=node.name,
            kind=SymbolKind.CONSTANT,
            type_info=final_type,
            line=getattr(node, 'line', None),
            column=getattr(node, 'column', None)
        )
        
        if not self.symbol_table.declare(symbol_info):
            # This should not happen since we checked above, but add safety
            self.add_error_at_node(
                Redeclared("Constant", node.name),
                node
            )
        
        return final_type
    
    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        """
        Visit function declaration - Task 3.5.
        Handles function signature registration and parameter validation.
        """
        # Check for redeclaration in global scope
        if self.symbol_table.lookup_current_scope(node.name):
            self.add_error_at_node(
                Redeclared("Function", node.name),
                node
            )
            return
        
        # Check if this is the main function (Task 3.6)
        if node.name == "main":
            if self.main_function_found:
                # Multiple main functions
                self.add_error_at_node(
                    Redeclared("Function", "main"),
                    node
                )
                return
            
            # Validate main function signature
            if len(node.params) != 0:
                # Main function should have no parameters
                self.add_error_at_node(NoEntryPoint(), node)
                return
            
            if not isinstance(node.return_type, VoidType):
                # Main function should return void
                self.add_error_at_node(NoEntryPoint(), node)
                return
            
            self.main_function_found = True
        
        # Get return type
        return_type = self.visit(node.return_type)
        
        # Process parameters and check for redeclaration
        param_types = []
        param_names = set()
        
        for param in node.params:
            if param.name in param_names:
                self.add_error_at_node(
                    Redeclared("Parameter", param.name),
                    param
                )
                continue
            
            param_names.add(param.name)
            param_type = self.visit(param.param_type)
            param_types.append(param_type)
        
        # Create function symbol info
        # Store parameter info in a way we can retrieve later
        function_info = {
            'return_type': return_type,
            'param_types': param_types,
            'param_names': list(param_names)
        }
        
        symbol_info = SymbolInfo(
            name=node.name,
            kind=SymbolKind.FUNCTION,
            type_info=function_info,
            line=getattr(node, 'line', None),
            column=getattr(node, 'column', None)
        )
        
        if not self.symbol_table.declare(symbol_info):
            self.add_error_at_node(
                Redeclared("Function", node.name),
                node
            )
            return
        
        # Enter function scope for body analysis
        self.symbol_table.enter_scope(f"function_{node.name}")
        
        # Store current function return type for return statement checking
        previous_return_type = self.current_function_return_type
        self.current_function_return_type = return_type
        
        # Register parameters in function scope
        for param in node.params:
            if param.name not in param_names:  # Skip if redeclared
                continue
                
            param_type = self.visit(param.param_type)
            param_symbol = SymbolInfo(
                name=param.name,
                kind=SymbolKind.PARAMETER,
                type_info=param_type,
                line=getattr(param, 'line', None),
                column=getattr(param, 'column', None)
            )
            self.symbol_table.declare(param_symbol)
        
        # Process function body
        for stmt in node.body:
            self.visit(stmt)
        
        # Check return path analysis for non-void functions (Task 3.18)
        if not isinstance(return_type, VoidType):
            if not self.check_all_paths_return(node.body, return_type):
                self.add_error_at_node(
                    TypeMismatchInStatement(node),
                    node
                )
        
        # Restore previous function context
        self.current_function_return_type = previous_return_type
        self.symbol_table.exit_scope()
        
        return return_type
    
    def register_function_signature(self, node: "FuncDecl"):
        """
        Register function signature in the symbol table (first pass).
        """
        # Check for redeclaration in global scope
        if self.symbol_table.lookup_current_scope(node.name):
            self.add_error_at_node(
                Redeclared("Function", node.name),
                node
            )
            return
        
        # Check if this is the main function (Task 3.6)
        if node.name == "main":
            if self.main_function_found:
                # Multiple main functions
                self.add_error_at_node(
                    Redeclared("Function", "main"),
                    node
                )
                return
            
            # Validate main function signature
            if len(node.params) != 0:
                # Main function should have no parameters
                self.add_error_at_node(NoEntryPoint(), node)
                return
            
            if not isinstance(node.return_type, VoidType):
                # Main function should return void
                self.add_error_at_node(NoEntryPoint(), node)
                return
            
            self.main_function_found = True
        
        # Get return type
        return_type = self.visit(node.return_type)
        
        # Process parameters and check for redeclaration
        param_types = []
        param_names = set()
        
        for param in node.params:
            if param.name in param_names:
                self.add_error_at_node(
                    Redeclared("Parameter", param.name),
                    param
                )
                continue
            
            param_names.add(param.name)
            param_type = self.visit(param.param_type)
            param_types.append(param_type)
        
        # Create function symbol info
        function_info = {
            'return_type': return_type,
            'param_types': param_types,
            'param_names': list(param_names)
        }
        
        symbol_info = SymbolInfo(
            name=node.name,
            kind=SymbolKind.FUNCTION,
            type_info=function_info,
            line=getattr(node, 'line', None),
            column=getattr(node, 'column', None)
        )
        
        if not self.symbol_table.declare(symbol_info):
            self.add_error_at_node(
                Redeclared("Function", node.name),
                node
            )

    def check_function_body(self, node: "FuncDecl"):
        """
        Check function body implementation (second pass).
        """
        # Get function signature from symbol table
        func_symbol = self.symbol_table.lookup(node.name)
        if func_symbol is None:
            return  # Error already reported in first pass
        
        function_info = func_symbol.type_info
        return_type = function_info['return_type']
        
        # Enter function scope for body analysis
        self.symbol_table.enter_scope(f"function_{node.name}")
        
        # Store current function return type for return statement checking
        previous_return_type = self.current_function_return_type
        self.current_function_return_type = return_type
        
        # Register parameters in function scope
        for param in node.params:
            param_type = self.visit(param.param_type)
            param_symbol = SymbolInfo(
                name=param.name,
                kind=SymbolKind.PARAMETER,
                type_info=param_type,
                line=getattr(param, 'line', None),
                column=getattr(param, 'column', None)
            )
            self.symbol_table.declare(param_symbol)
        
        # Process function body
        for stmt in node.body:
            self.visit(stmt)
        
        # Check return path analysis for non-void functions (Task 3.18)
        if not isinstance(return_type, VoidType):
            if not self.check_all_paths_return(node.body, return_type):
                self.add_error_at_node(
                    TypeMismatchInStatement(node),
                    node
                )
        
        # Restore previous function context
        self.current_function_return_type = previous_return_type
        self.symbol_table.exit_scope()

    def visit_param(self, node: "Param", o: Any = None):
        """
        Visit parameter - part of Task 3.5.
        Parameters are handled in visit_func_decl.
        """
        return self.visit(node.param_type)
    
    # Type system visitors
    def visit_int_type(self, node: "IntType", o: Any = None):
        return node
    
    def visit_float_type(self, node: "FloatType", o: Any = None):
        return node
    
    def visit_bool_type(self, node: "BoolType", o: Any = None):
        return node
    
    def visit_string_type(self, node: "StringType", o: Any = None):
        return node
    
    def visit_void_type(self, node: "VoidType", o: Any = None):
        return node
    
    def visit_array_type(self, node: "ArrayType", o: Any = None):
        return node
    
    # Statement visitors (Task 3.7-3.10)
    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        """
        Visit variable declaration - Task 3.7.
        Handles local variable declarations and type inference.
        """
        # Check for redeclaration in current scope
        if self.symbol_table.lookup_current_scope(node.name):
            self.add_error_at_node(
                Redeclared("Variable", node.name),
                node
            )
            return
        
        # Check for shadowing of functions and constants (forbidden)
        existing_symbol = self.symbol_table.lookup(node.name)
        if existing_symbol:
            if existing_symbol.kind == SymbolKind.FUNCTION:
                self.add_error_at_node(
                    Redeclared("Variable", node.name),
                    node
                )
                return
            elif existing_symbol.kind == SymbolKind.CONSTANT:
                self.add_error_at_node(
                    Redeclared("Constant", node.name),
                    node
                )
                return
        
        # Evaluate initialization expression to get its type
        init_type = None
        if node.value:
            # Special case: Empty array literal cannot be inferred without type annotation
            if isinstance(node.value, ArrayLiteral) and not node.value.elements and not node.type_annotation:
                self.add_error_at_node(
                    TypeCannotBeInferred(node),
                    node
                )
                return
            
            init_type = self.visit(node.value)
            if init_type is None:
                return  # Error already reported in expression
            
            # Check if trying to assign void type (forbidden)
            if isinstance(init_type, VoidType):
                self.add_error_at_node(
                    TypeMismatchInStatement(node),
                    node
                )
                return
        
        # Handle type annotation and inference
        declared_type = None
        if node.type_annotation:
            declared_type = self.visit(node.type_annotation)
            
            # If both type annotation and initialization exist, check compatibility
            if init_type:
                # Special handling for array literals
                if isinstance(node.value, ArrayLiteral) and self.is_array_type(declared_type):
                    if not self.validate_array_literal_assignment(declared_type, node.value):
                        self.add_error_at_node(
                            TypeMismatchInStatement(node),
                            node
                        )
                        return
                elif not self.is_compatible_for_assignment(declared_type, init_type):
                    self.add_error_at_node(
                        TypeMismatchInStatement(node),
                        node
                    )
                    return
        
        # Determine final type
        if declared_type:
            final_type = declared_type
        elif init_type:
            final_type = init_type
        else:
            # No type annotation and no initialization - cannot infer
            self.add_error_at_node(
                TypeCannotBeInferred(node),
                node
            )
            return
        
        # Register variable in current scope
        symbol_info = SymbolInfo(
            name=node.name,
            kind=SymbolKind.VARIABLE,
            type_info=final_type,
            line=getattr(node, 'line', None),
            column=getattr(node, 'column', None)
        )
        
        if not self.symbol_table.declare(symbol_info):
            self.add_error_at_node(
                Redeclared("Variable", node.name),
                node
            )
        
        return final_type
    
    def visit_assignment(self, node: "Assignment", o: Any = None):
        """Visit assignment statement - Task 3.7."""
        # Check if we're trying to assign to a constant
        if isinstance(node.lvalue, IdLValue):
            symbol = self.symbol_table.lookup(node.lvalue.name)
            if symbol and symbol.kind == SymbolKind.CONSTANT:
                self.add_error_at_node(
                    TypeMismatchInStatement(node),
                    node
                )
                return
        
        # Get the left-hand side type
        lhs_type = self.visit(node.lvalue)
        if lhs_type is None:
            return  # Error already reported
        
        # Get the right-hand side type
        rhs_type = self.visit(node.value)
        if rhs_type is None:
            return  # Error already reported
        
        # Check type compatibility
        if not self.is_compatible_for_assignment(lhs_type, rhs_type):
            self.add_error_at_node(
                TypeMismatchInStatement(node),
                node
            )
        
        return lhs_type
    
    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        """Visit if statement - Task 3.8."""
        # Check condition type
        condition_type = self.visit(node.condition)
        if condition_type and not self.is_boolean_type(condition_type):
            self.add_error_at_node(
                TypeMismatchInStatement(node),
                node
            )
        
        # Visit then branch
        self.symbol_table.enter_scope("if_then")
        self.visit(node.then_stmt)
        self.symbol_table.exit_scope()
        
        # Visit elif branches if present
        if node.elif_branches:
            for condition, block in node.elif_branches:
                # Check elif condition type
                elif_condition_type = self.visit(condition)
                if elif_condition_type and not self.is_boolean_type(elif_condition_type):
                    self.add_error_at_node(
                        TypeMismatchInStatement(node),
                        node
                    )
                
                # Visit elif block
                self.symbol_table.enter_scope("if_elif")
                self.visit(block)
                self.symbol_table.exit_scope()
        
        # Visit else branch if present
        if node.else_stmt:
            self.symbol_table.enter_scope("if_else")
            self.visit(node.else_stmt)
            self.symbol_table.exit_scope()
    
    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        """Visit while statement - Task 3.8."""
        # Check condition type
        condition_type = self.visit(node.condition)
        if condition_type and not self.is_boolean_type(condition_type):
            self.add_error_at_node(
                TypeMismatchInStatement(node),
                node
            )
        
        # Enter loop context
        self.loop_depth += 1
        self.symbol_table.enter_scope("while_body")
        
        # Visit body (BlockStmt)
        self.visit(node.body)
        
        # Exit loop context
        self.symbol_table.exit_scope()
        self.loop_depth -= 1
    
    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        """Visit for statement - Task 3.8."""
        # Check that collection is array type
        collection_type = self.visit(node.iterable)
        if collection_type and not self.is_array_type(collection_type):
            self.add_error_at_node(
                TypeMismatchInStatement(node),
                node
            )
            return
        
        # Enter loop context and new scope
        self.loop_depth += 1
        self.symbol_table.enter_scope("for_body")
        
        # Check for variable shadowing before registering loop variable
        existing_symbol = self.symbol_table.lookup(node.variable)
        if existing_symbol and existing_symbol.kind == SymbolKind.PARAMETER:
            # Loop variable shadows a parameter
            self.add_error_at_node(
                Redeclared("Variable", node.variable),
                node
            )
            # Exit loop context on error
            self.symbol_table.exit_scope()
            self.loop_depth -= 1
            return
        
        # Register loop variable with element type
        if collection_type and self.is_array_type(collection_type):
            element_type = self.get_array_element_type(collection_type)
            loop_var_symbol = SymbolInfo(
                name=node.variable,
                kind=SymbolKind.VARIABLE,
                type_info=element_type,
                line=getattr(node, 'line', None),
                column=getattr(node, 'column', None)
            )
            self.symbol_table.declare(loop_var_symbol)
        
        # Visit body (BlockStmt)
        self.visit(node.body)
        
        # Exit loop context
        self.symbol_table.exit_scope()
        self.loop_depth -= 1
    
    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        """Visit return statement - Task 3.10."""
        if self.current_function_return_type is None:
            # Return outside of function (shouldn't happen with correct parser)
            return
        
        # Check return value
        if node.value:
            # Return with expression
            expr_type = self.visit(node.value)
            if expr_type and not self.are_types_equal(self.current_function_return_type, expr_type):
                self.add_error_at_node(
                    TypeMismatchInStatement(node),
                    node
                )
        else:
            # Return without expression - should be void
            if not self.is_void_type(self.current_function_return_type):
                self.add_error_at_node(
                    TypeMismatchInStatement(node),
                    node
                )
    
    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        """Visit break statement - Task 3.9."""
        if self.loop_depth == 0:
            self.add_error_at_node(
                MustInLoop(node),
                node
            )
    
    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        """Visit continue statement - Task 3.9."""
        if self.loop_depth == 0:
            self.add_error_at_node(
                MustInLoop(node),
                node
            )
    
    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        """Visit expression statement."""
        # Special handling for function calls in statement context
        if isinstance(node.expr, FunctionCall):
            # Check if function exists
            if isinstance(node.expr.function, Identifier):
                function_name = node.expr.function.name
                func_symbol = self.symbol_table.lookup(function_name)
                if func_symbol is None:
                    self.add_error_at_node(
                        TypeMismatchInStatement(node),
                        node
                    )
                    return None
                elif func_symbol.kind != SymbolKind.FUNCTION:
                    self.add_error_at_node(
                        TypeMismatchInStatement(node),
                        node
                    )
                    return None
                else:
                    # Check function call compatibility in statement context
                    func_info = func_symbol.type_info
                    expected_param_types = func_info['param_types']
                    
                    # Check argument count and types
                    if len(node.expr.args) != len(expected_param_types):
                        self.add_error_at_node(
                            TypeMismatchInStatement(node.expr),
                            node
                        )
                        return None
                    
                    # Check argument types
                    for i, (arg, expected_type) in enumerate(zip(node.expr.args, expected_param_types)):
                        arg_type = self.visit(arg)
                        if arg_type and not self.are_types_equal(arg_type, expected_type):
                            self.add_error_at_node(
                                TypeMismatchInStatement(node.expr),
                                node
                            )
                            return None
                    
                    return func_info['return_type']
        
        return self.visit(node.expr)
    
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        """Visit block statement."""
        self.symbol_table.enter_scope("block")
        for stmt in node.statements:
            self.visit(stmt)
        self.symbol_table.exit_scope()
    
    # Left-value visitors
    def visit_id_lvalue(self, node: "IdLValue", o: Any = None):
        """Visit identifier left-value."""
        symbol = self.symbol_table.lookup(node.name)
        if symbol is None:
            self.add_error_at_node(
                Undeclared(IdentifierMarker(), node.name),
                node
            )
            return None
        
        return symbol.type_info
    
    def visit_array_access_lvalue(self, node: "ArrayAccessLValue", o: Any = None):
        """Visit array access left-value."""
        # Get array type
        array_type = self.visit(node.array)
        if array_type is None:
            return None
        
        # Check that it's actually an array
        if not self.is_array_type(array_type):
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        # Check index type
        index_type = self.visit(node.index)
        if index_type and not self.is_integer_type(index_type):
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        return self.get_array_element_type(array_type)
    
    # Expression visitors
    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        """Visit binary operation - Task 3.11."""
        # Special handling for pipeline operator
        if node.operator == '>>':
            return self.handle_pipeline_operation(node)
        
        left_type = self.visit(node.left)
        right_type = self.visit(node.right)
        
        if left_type is None or right_type is None:
            return None  # Error already reported
        
        # Check if operation is valid
        is_valid, result_type = self.can_apply_binary_op(node.operator, left_type, right_type)
        if not is_valid:
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        return result_type
    
    def visit_unary_op(self, node: "UnaryOp", o: Any = None):
        """Visit unary operation - Task 3.12."""
        operand_type = self.visit(node.operand)
        if operand_type is None:
            return None  # Error already reported
        
        # Check if operation is valid
        is_valid, result_type = self.can_apply_unary_op(node.operator, operand_type)
        if not is_valid:
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        return result_type
    
    def visit_function_call(self, node: "FunctionCall", o: Any = None):
        """Visit function call - Task 3.12."""
        # The function should be an identifier
        if not isinstance(node.function, Identifier):
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        function_name = node.function.name
        
        # Look up function
        func_symbol = self.symbol_table.lookup(function_name)
        if func_symbol is None:
            self.add_error_at_node(
                Undeclared(FunctionMarker(), function_name),
                node
            )
            return None
        
        if func_symbol.kind != SymbolKind.FUNCTION:
            # Trying to call a variable as a function
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        # Get function info
        func_info = func_symbol.type_info
        expected_param_types = func_info['param_types']
        return_type = func_info['return_type']
        
        # Check argument count
        if len(node.args) != len(expected_param_types):
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        # Check argument types
        for i, (arg, expected_type) in enumerate(zip(node.args, expected_param_types)):
            arg_type = self.visit(arg)
            if arg_type and not self.are_types_equal(arg_type, expected_type):
                self.add_error_at_node(
                    TypeMismatchInExpression(node),
                    node
                )
                return None
        
        return return_type
    
    def visit_array_access(self, node: "ArrayAccess", o: Any = None):
        """Visit array access - Task 3.13."""
        # Get array type
        array_type = self.visit(node.array)
        if array_type is None:
            return None
        
        # Check that it's actually an array
        if not self.is_array_type(array_type):
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        # Check index type
        index_type = self.visit(node.index)
        if index_type and not self.is_integer_type(index_type):
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        return self.get_array_element_type(array_type)
    
    def visit_array_literal(self, node: "ArrayLiteral", o: Any = None):
        """Visit array literal - Task 3.15."""
        if not node.elements:
            # Empty array - cannot infer type, return None and let parent handle error
            return None
        
        # Infer type from elements
        success, array_type = self.infer_array_literal_type(node.elements)
        if not success:
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        return array_type
    
    def visit_identifier(self, node: "Identifier", o: Any = None):
        """Visit identifier - Task 3.14."""
        symbol = self.symbol_table.lookup(node.name)
        if symbol is None:
            self.add_error_at_node(
                Undeclared(IdentifierMarker(), node.name),
                node
            )
            return None
        
        # Check if it's a function being used as identifier
        if symbol.kind == SymbolKind.FUNCTION:
            self.add_error_at_node(
                TypeMismatchInExpression(node),
                node
            )
            return None
        
        return symbol.type_info
    
    # Literal visitors
    def visit_integer_literal(self, node: "IntegerLiteral", o: Any = None):
        return IntType()
    
    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return FloatType()
    
    def visit_boolean_literal(self, node: "BooleanLiteral", o: Any = None):
        return BoolType()
    
    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return StringType()