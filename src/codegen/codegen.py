"""
Code Generator for HLang programming language.
This module implements a code generator that traverses AST nodes and generates
Java bytecode using the Emitter and Frame classes.
"""

from ast import Sub
from typing import Any, List, Optional
from ..utils.visitor import ASTVisitor
from ..utils.nodes import *
from .emitter import Emitter
from .frame import Frame
from .error import IllegalOperandException, IllegalRuntimeException
from .io import IO_SYMBOL_LIST
from .utils import *
from functools import *


class CodeGenerator(ASTVisitor):
    def __init__(self):
        self.class_name = "HLang"
        self.emit = Emitter(self.class_name + ".j")

    def visit_program(self, node: "Program", o: Any = None):
        self.emit.print_out(self.emit.emit_prolog(self.class_name, "java/lang/Object"))

        global_env = reduce(
            lambda acc, cur: self.visit(cur, acc),
            node.func_decls,
            SubBody(None, IO_SYMBOL_LIST),
        )

        self.generate_method(
            FuncDecl("<init>", [], VoidType(), []),
            SubBody(Frame("<init>", VoidType()), []),
        )
        self.emit.emit_epilog()

    def generate_method(self, node: "FuncDecl", o: SubBody = None):
        frame = o.frame

        is_init = node.name == "<init>"
        is_main = node.name == "main"

        param_types = list(map(lambda x: x.param_type, node.params))
        if is_main:
            param_types = [ArrayType(StringType(), 0)]
        return_type = node.return_type

        self.emit.print_out(
            self.emit.emit_method(
                node.name, FunctionType(param_types, return_type), not is_init
            )
        )

        frame.enter_scope(True)

        from_label = frame.get_start_label()
        to_label = frame.get_end_label()

        # Generate code for parameters
        if is_init:
            this_idx = frame.get_new_index()

            self.emit.print_out(
                self.emit.emit_var(
                    this_idx, "this", ClassType(self.class_name), from_label, to_label
                )
            )
        elif is_main:
            args_idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    args_idx, "args", ArrayType(StringType(), 0), from_label, to_label
                )
            )
        else:
            o = reduce(lambda acc, cur: self.visit(cur, acc), node.params, o)

        self.emit.print_out(self.emit.emit_label(from_label, frame))

        # Generate code for body

        if is_init:
            self.emit.print_out(
                self.emit.emit_read_var(
                    "this", ClassType(self.class_name), this_idx, frame
                )
            )
            self.emit.print_out(self.emit.emit_invoke_special(frame))

        o = reduce(lambda acc, cur: self.visit(cur, acc), node.body, o)

        if type(return_type) is VoidType:
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))

        self.emit.print_out(self.emit.emit_label(to_label, frame))

        self.emit.print_out(self.emit.emit_end_method(frame))

        frame.exit_scope()

    def visit_const_decl(self, node: "ConstDecl", o: Any = None):
        # Constants are handled as static fields
        # Generate static field declaration and initialization in class
        # For now, we'll store constants in the symbol table but not emit static fields
        # This is because static field initialization requires clinit method which is complex
        return o

    def visit_func_decl(self, node: "FuncDecl", o: SubBody = None):
        frame = Frame(node.name, node.return_type)
        self.generate_method(node, SubBody(frame, o.sym))
        param_types = list(map(lambda x: x.param_type, node.params))
        return SubBody(
            None,
            [
                Symbol(
                    node.name,
                    FunctionType(param_types, node.return_type),
                    CName(self.class_name),
                )
            ]
            + o.sym,
        )

    def visit_param(self, node: "Param", o: Any = None):
        idx = o.frame.get_new_index()
        self.emit.print_out(
            self.emit.emit_var(
                idx,
                node.name,
                node.param_type,
                o.frame.get_start_label(),
                o.frame.get_end_label(),
            )
        )

        return SubBody(
            o.frame,
            [Symbol(node.name, node.param_type, Index(idx))] + o.sym,
        )

    # Type system

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

    # Statements

    def visit_var_decl(self, node: "VarDecl", o: SubBody = None):
        idx = o.frame.get_new_index()
        self.emit.print_out(
            self.emit.emit_var(
                idx,
                node.name,
                node.type_annotation,
                o.frame.get_start_label(),
                o.frame.get_end_label(),
            )
        )

        # Create new symbol table with the declared variable
        new_sym = [Symbol(node.name, node.type_annotation, Index(idx))] + o.sym
        new_o = SubBody(o.frame, new_sym)

        if node.value is not None:
            self.visit(
                Assignment(IdLValue(node.name), node.value),
                new_o,
            )
        return new_o

    def visit_assignment(self, node: "Assignment", o: SubBody = None):
        """Generate code for assignment operations."""
        # Different handling based on lvalue type
        if isinstance(node.lvalue, ArrayAccessLValue):
            # Array assignment: array[index] = value
            # Generate lvalue code (array ref + index)
            lc, lt = self.visit(node.lvalue, Access(o.frame, o.sym))
            
            # Generate value code
            rc, rt = self.visit(node.value, Access(o.frame, o.sym))
            
            # Emit the code: array ref, index, value, then store
            self.emit.print_out(lc)  # array ref + index
            self.emit.print_out(rc)  # value
            
            # Emit array store instruction
            store_code = self.emit.emit_astore(lt, o.frame)
            self.emit.print_out(store_code)
        else:
            # Regular variable assignment
            rc, rt = self.visit(node.value, Access(o.frame, o.sym))
            self.emit.print_out(rc)
            lc, lt = self.visit(node.lvalue, Access(o.frame, o.sym))
            self.emit.print_out(lc)
        
        return o

    def visit_if_stmt(self, node: "IfStmt", o: SubBody = None):
        # Generate code for condition
        cond_code, cond_type = self.visit(node.condition, Access(o.frame, o.sym))
        
        # Generate labels
        false_label = o.frame.get_new_label()
        end_label = o.frame.get_new_label()
        
        # Emit condition code
        self.emit.print_out(cond_code)
        
        # If condition is false, jump to next branch
        self.emit.print_out(self.emit.emit_if_false(false_label, o.frame))
        
        # Generate then branch
        self.visit(node.then_stmt, o)
        
        # Jump to end to skip other branches
        if node.elif_branches or node.else_stmt:
            self.emit.print_out(self.emit.emit_goto(end_label, o.frame))
        
        # Emit false label
        self.emit.print_out(self.emit.emit_label(false_label, o.frame))
        
        # Handle elif branches (recursive if statements)
        if node.elif_branches:
            # For simplicity, treat elif as nested if statements
            for elif_cond, elif_stmt in node.elif_branches:
                elif_if = IfStmt(elif_cond, elif_stmt, [], node.else_stmt)
                self.visit(elif_if, o)
                return o
        
        # Generate else branch if it exists
        if node.else_stmt:
            self.visit(node.else_stmt, o)
        
        # Emit end label if we have elif/else branches
        if node.elif_branches or node.else_stmt:
            self.emit.print_out(self.emit.emit_label(end_label, o.frame))
        
        return o

    def visit_while_stmt(self, node: "WhileStmt", o: SubBody = None):
        # Enter loop creates continue/break labels automatically
        o.frame.enter_loop()
        
        # Get the continue label (loop start)
        loop_start = o.frame.get_continue_label()
        loop_end = o.frame.get_break_label()
        
        # Emit loop start label
        self.emit.print_out(self.emit.emit_label(loop_start, o.frame))
        
        # Generate condition code
        cond_code, cond_type = self.visit(node.condition, Access(o.frame, o.sym))
        self.emit.print_out(cond_code)
        
        # If condition is false, exit loop
        self.emit.print_out(self.emit.emit_if_false(loop_end, o.frame))
        
        # Generate loop body
        self.visit(node.body, o)
        
        # Jump back to loop start
        self.emit.print_out(self.emit.emit_goto(loop_start, o.frame))
        
        # Emit loop end label
        self.emit.print_out(self.emit.emit_label(loop_end, o.frame))
        
        # Exit loop
        o.frame.exit_loop()
        
        return o

    def visit_for_stmt(self, node: "ForStmt", o: SubBody = None):
        """Generate code for for-each loop over arrays."""
        # Generate code for the iterable (array)
        iterable_code, iterable_type = self.visit(node.iterable, Access(o.frame, o.sym))
        
        # Verify it's an array type
        if not isinstance(iterable_type, ArrayType):
            raise IllegalOperandException("For-each loop requires array type")
        
        element_type = iterable_type.element_type
        array_size = iterable_type.size
        
        # Set up loop variables
        o.frame.enter_loop()
        start_label = o.frame.get_new_label()
        continue_label = o.frame.get_continue_label()
        break_label = o.frame.get_break_label()
        
        # Allocate local variables for loop control
        array_idx = o.frame.get_new_index()  # Store array reference
        index_idx = o.frame.get_new_index()  # Loop index counter
        element_idx = o.frame.get_new_index() # Current element (loop variable)
        
        # Create new symbol table with loop variable
        loop_var_symbol = Symbol(node.loop_var, element_type, Index(element_idx))
        new_sym = [loop_var_symbol] + o.sym
        new_o = SubBody(o.frame, new_sym)
        
        # Generate code
        code = ""
        
        # Store array reference
        code += iterable_code
        code += self.emit.emit_write_var("", iterable_type, array_idx, o.frame)
        
        # Initialize loop index to 0
        code += self.emit.emit_push_iconst(0, o.frame)
        code += self.emit.emit_write_var("", IntType(), index_idx, o.frame)
        
        # Start loop label
        code += self.emit.emit_label(start_label, o.frame)
        
        # Check loop condition: if index < array_size continue, else break
        body_label = o.frame.get_new_label()
        code += self.emit.emit_read_var("", IntType(), index_idx, o.frame)  # load index
        code += self.emit.emit_push_iconst(array_size, o.frame)  # load array size
        code += self.emit.emit_ificmplt(body_label, o.frame)  # if index < size, continue to body
        code += self.emit.emit_goto(break_label, o.frame)  # else break
        
        # Body label - load current element and execute body
        code += self.emit.emit_label(body_label, o.frame)
        
        # Load current element: array[index]
        code += self.emit.emit_read_var("", iterable_type, array_idx, o.frame)  # load array
        code += self.emit.emit_read_var("", IntType(), index_idx, o.frame)  # load index
        code += self.emit.emit_aload(element_type, o.frame)  # load array[index]
        code += self.emit.emit_write_var(node.loop_var, element_type, element_idx, o.frame)  # store in loop var
        
        self.emit.print_out(code)
        
        # Generate body code
        self.visit(node.body, new_o)
        
        # Continue label (increment index and loop back)
        self.emit.print_out(self.emit.emit_label(continue_label, o.frame))
        
        # Increment index: index = index + 1
        increment_code = ""
        increment_code += self.emit.emit_read_var("", IntType(), index_idx, o.frame)
        increment_code += self.emit.emit_push_iconst(1, o.frame)
        increment_code += self.emit.emit_add_op("+", IntType(), o.frame)
        increment_code += self.emit.emit_write_var("", IntType(), index_idx, o.frame)
        
        # Jump back to start
        increment_code += self.emit.emit_goto(start_label, o.frame)
        self.emit.print_out(increment_code)
        
        # Break label (end of loop)
        self.emit.print_out(self.emit.emit_label(break_label, o.frame))
        
        o.frame.exit_loop()
        return o

    def visit_return_stmt(self, node: "ReturnStmt", o: SubBody = None):
        if node.value:
            # Generate code for return expression
            expr_code, expr_type = self.visit(node.value, Access(o.frame, o.sym))
            self.emit.print_out(expr_code)
            # Emit return with value
            self.emit.print_out(self.emit.emit_return(expr_type, o.frame))
        else:
            # Emit void return
            self.emit.print_out(self.emit.emit_return(VoidType(), o.frame))
        return o

    def visit_break_stmt(self, node: "BreakStmt", o: SubBody = None):
        # Jump to the break label of the current loop
        break_label = o.frame.get_break_label()
        self.emit.print_out(self.emit.emit_goto(break_label, o.frame))
        return o

    def visit_continue_stmt(self, node: "ContinueStmt", o: SubBody = None):
        # Jump to the continue label of the current loop
        continue_label = o.frame.get_continue_label()
        self.emit.print_out(self.emit.emit_goto(continue_label, o.frame))
        return o

    def visit_expr_stmt(self, node: "ExprStmt", o: SubBody = None):
        code, typ = self.visit(node.expr, Access(o.frame, o.sym))
        self.emit.print_out(code)
        return o

    def visit_block_stmt(self, node: "BlockStmt", o: SubBody = None):
        # Enter new scope
        o.frame.enter_scope(False)
        
        # Process all statements in the block
        for stmt in node.statements:
            o = self.visit(stmt, o)
        
        # Exit scope
        o.frame.exit_scope()
        
        return o

    # Left-values

    def visit_id_lvalue(self, node: "IdLValue", o: Access = None):
        sym = next(
            filter(lambda x: x.name == node.name, o.sym),
            False,
        )

        if type(sym.value) is Index:
            code = self.emit.emit_write_var(
                sym.name, sym.type, sym.value.value, o.frame
            )

        return code, sym.type

    def visit_array_access_lvalue(self, node: "ArrayAccessLValue", o: Access = None):
        """Generate code for array element assignment (lvalue)."""
        # Generate code for array reference
        array_code, array_type = self.visit(node.array, o)
        
        # Generate code for index
        index_code, index_type = self.visit(node.index, o)
        
        # Verify array type
        if not isinstance(array_type, ArrayType):
            raise IllegalOperandException("Array access on non-array type")
        
        element_type = array_type.element_type
        
        # For assignment, we prepare array reference and index on stack
        # The assignment visitor will add the value and emit the store instruction
        combined_code = array_code + index_code
        
        return combined_code, element_type

    # Expressions

    def visit_binary_op(self, node: "BinaryOp", o: Access = None):
        # Generate code for left and right operands
        left_code, left_type = self.visit(node.left, Access(o.frame, o.sym))
        right_code, right_type = self.visit(node.right, Access(o.frame, o.sym))
        
        # Determine result type and operation
        op = node.operator
        
        # Handle arithmetic operations
        if op in ["+", "-", "*", "/", "%"]:
            if type(left_type) is IntType and type(right_type) is IntType:
                result_type = IntType()
                if op in ["+", "-"]:
                    op_code = self.emit.emit_add_op(op, result_type, o.frame)
                else:  # *, /, %
                    op_code = self.emit.emit_mul_op(op, result_type, o.frame)
            elif type(left_type) is FloatType or type(right_type) is FloatType:
                result_type = FloatType()
                if op in ["+", "-"]:
                    op_code = self.emit.emit_add_op(op, result_type, o.frame)
                else:  # *, /, %
                    op_code = self.emit.emit_mul_op(op, result_type, o.frame)
            elif type(left_type) is StringType and type(right_type) is StringType and op == "+":
                # String concatenation
                result_type = StringType()
                op_code = self.emit.emit_add_op(op, result_type, o.frame)
            else:
                raise IllegalOperandException(f"Invalid operand types for {op}")
        
        # Handle comparison operations
        elif op in ["<", "<=", ">", ">=", "==", "!="]:
            result_type = BoolType()
            op_code = self.emit.emit_re_op(op, left_type, o.frame)
        
        # Handle logical operations
        elif op == "&&":
            result_type = BoolType()
            op_code = self.emit.emit_and_op(o.frame)
        elif op == "||":
            result_type = BoolType()
            op_code = self.emit.emit_or_op(o.frame)
        
        else:
            raise IllegalOperandException(f"Unknown binary operator: {op}")
        
        return left_code + right_code + op_code, result_type

    def visit_unary_op(self, node: "UnaryOp", o: Access = None):
        # Generate code for operand
        operand_code, operand_type = self.visit(node.operand, Access(o.frame, o.sym))
        
        op = node.operator
        
        if op == "-":
            # Negation
            op_code = self.emit.emit_neg_op(operand_type, o.frame)
            result_type = operand_type
        elif op == "!":
            # Logical not
            op_code = self.emit.emit_not(operand_type, o.frame)
            result_type = BoolType()
        elif op == "+":
            # Unary plus (no-op)
            op_code = ""
            result_type = operand_type
        else:
            raise IllegalOperandException(f"Unknown unary operator: {op}")
        
        return operand_code + op_code, result_type

    def visit_function_call(self, node: "FunctionCall", o: Access = None):
        function_name = node.function.name
        function_symbol = next(filter(lambda x: x.name == function_name, o.sym), False)
        class_name = function_symbol.value.value
        argument_codes = []
        for argument in node.args:
            ac, at = self.visit(argument, Access(o.frame, o.sym))
            argument_codes += [ac]

        return (
            "".join(argument_codes)
            + self.emit.emit_invoke_static(
                class_name + "/" + function_name, function_symbol.type, o.frame
            ),
            VoidType(),
        )

    def visit_array_access(self, node: "ArrayAccess", o: Access = None):
        """Generate code for array element access."""
        # Generate code for array
        array_code, array_type = self.visit(node.array, o)
        
        # Generate code for index
        index_code, index_type = self.visit(node.index, o)
        
        # Verify array type
        if not isinstance(array_type, ArrayType):
            raise IllegalOperandException("Array access on non-array type")
        
        element_type = array_type.element_type
        
        # Combine codes: array reference, then index, then load
        combined_code = array_code + index_code
        
        # Emit array load instruction
        aload_code = self.emit.emit_aload(element_type, o.frame)
        
        return combined_code + aload_code, element_type

    def visit_array_literal(self, node: "ArrayLiteral", o: Access = None):
        """Generate code for array literal creation."""
        if not node.elements:
            # Empty array - just create an array of size 0
            # We need to determine the element type from context
            return self.emit.emit_push_iconst(0, o.frame) + self.emit.emit_new_array("I"), ArrayType(IntType(), 0)
        
        # Generate code to create array
        array_size = len(node.elements)
        
        # Infer element type from first element
        first_element_code, element_type = self.visit(node.elements[0], o)
        
        # Determine JVM array type
        if type(element_type) is IntType:
            jvm_type = "int"
        elif type(element_type) is FloatType:
            jvm_type = "float" 
        elif type(element_type) is BoolType:
            jvm_type = "int"  # Booleans stored as integers
        elif type(element_type) is StringType:
            jvm_type = "java/lang/String"
        else:
            raise IllegalOperandException(f"Unsupported array element type: {type(element_type)}")
        
        # Generate code to create and populate array
        code = ""
        
        # Push array size
        code += self.emit.emit_push_iconst(array_size, o.frame)
        
        # Create array (use newarray for primitives, anewarray for objects)
        if type(element_type) in [IntType, FloatType, BoolType]:
            code += self.emit.emit_new_array(jvm_type)
        else:
            # Use anewarray for object types (strings, etc.)
            code += self.emit.jvm.emitANEWARRAY(jvm_type)
        
        # Populate array elements
        for i, element in enumerate(node.elements):
            # Duplicate array reference for assignment
            code += self.emit.emit_dup(o.frame)
            
            # Push index
            code += self.emit.emit_push_iconst(i, o.frame)
            
            # Generate element value
            element_code, _ = self.visit(element, o)
            code += element_code
            
            # Store element in array
            code += self.emit.emit_astore(element_type, o.frame)
        
        return code, ArrayType(element_type, array_size)

    def visit_identifier(self, node: "Identifier", o: Access = None):
        # Look up identifier in symbol table
        sym = next(filter(lambda x: x.name == node.name, o.sym), None)
        if sym and type(sym.value) is Index:
            # Local variable
            code = self.emit.emit_read_var(sym.name, sym.type, sym.value.value, o.frame)
            return code, sym.type
        else:
            # This should not happen in well-formed programs
            raise IllegalOperandException(f"Undefined identifier: {node.name}")

    # Literals

    def visit_integer_literal(self, node: "IntegerLiteral", o: Access = None):
        return self.emit.emit_push_iconst(node.value, o.frame), IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Access = None):
        return self.emit.emit_push_fconst(str(node.value), o.frame), FloatType()

    def visit_boolean_literal(self, node: "BooleanLiteral", o: Access = None):
        # Boolean literals are represented as integers: 1 for True, 0 for False
        value = 1 if node.value else 0
        return self.emit.emit_push_iconst(value, o.frame), BoolType()

    def visit_string_literal(self, node: "StringLiteral", o: Access = None):
        return (
            self.emit.emit_push_const('"' + node.value + '"', StringType(), o.frame),
            StringType(),
        )
