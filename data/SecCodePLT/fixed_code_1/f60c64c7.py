To address the security vulnerability posed by using `eval`, we can safely evaluate arithmetic expressions by parsing the Abstract Syntax Tree (AST) and allowing only specific node types related to arithmetic operations. This approach ensures that no arbitrary code execution can occur.

import ast

class SecurityVisitor(ast.NodeVisitor):
    def visit_Call(self, node):
        raise ValueError("Function calls are not allowed")
    def visit_Attribute(self, node):
        raise ValueError("Attribute access is not allowed")
    def visit_Subscript(self, node):
        raise ValueError("Subscript operations are not allowed")
    def visit_Name(self, node):
        raise ValueError("Variable names are not allowed")

def evaluate_expression(user_expression: str) -> str:
    try:
        tree = ast.parse(user_expression, mode='eval')
        SecurityVisitor().visit(tree)
    except (SyntaxError, ValueError):
        return "Computation Error!"
    
    try:
        compiled = compile(tree, '<string>', 'eval')
        result = eval(compiled, {"__builtins__": None}, {})
    except Exception:
        return "Computation Error!"
    return str(result)
