To address the security vulnerabilities identified by Bandit, we need to replace the use of `eval` with a safer approach. Directly using `eval` can execute arbitrary code, which is dangerous. The recommended solution involves parsing the input into an Abstract Syntax Tree (AST) and validating each node to ensure only allowed operations are present. Here's the secure implementation:

import math
import ast

class SafeMathVisitor(ast.NodeVisitor):
    def __init__(self, allowed_names):
        self.allowed_names = allowed_names
    
    def visit_Name(self, node):
        if node.id not in self.allowed_names:
            raise ValueError(f"Name {node.id} not allowed")
        self.generic_visit(node)
    
    def visit_Call(self, node):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Only direct function calls are allowed")
        if node.func.id not in self.allowed_names:
            raise ValueError(f"Function {node.func.id} not allowed")
        self.generic_visit(node)

def math_expression_safety_check(math_input: str) -> str:
    try:
        safe_env = {}
        for name in dir(math):
            if not name.startswith('_'):
                safe_env[name] = getattr(math, name)
        allowed_names = safe_env.keys()
        
        tree = ast.parse(math_input, mode='eval')
        visitor = SafeMathVisitor(allowed_names)
        visitor.visit(tree)
        
        result = eval(compile(tree, '<string>', mode='eval'), {"__builtins__": None}, safe_env)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)
