To address the security vulnerability posed by using `eval`, I employed AST parsing and restricted evaluation. Here's the approach:

1. **AST Parsing and Validation**: Parse the input string into an Abstract Syntax Tree (AST) and validate that only safe nodes (constants, arithmetic operations) are present. This prevents injection of malicious code.
2. **Restricted Environment**: Evaluate the parsed AST in an environment with no access to built-in functions or variables, ensuring only mathematical operations are performed.

The provided solution ensures that only valid arithmetic expressions are evaluated securely.

import ast

def calculate_expression(math_expression: str) -> str:
    try:
        tree = ast.parse(math_expression, mode='eval')
    except SyntaxError:
        return "Computation Error!"
    
    allowed_nodes = (
        ast.Expression, ast.BinOp, ast.UnaryOp,
        ast.Constant, ast.Num, ast.Add, ast.Sub,
        ast.Mult, ast.Div, ast.FloorDiv, ast.Mod,
        ast.Pow, ast.USub, ast.UAdd
    )
    
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            return "Computation Error!"
    
    try:
        compiled = compile(tree, filename='<string>', mode='eval')
        result = eval(compiled, {'__builtins__': None}, {})
    except Exception:
        return "Computation Error!"
    
    return str(result)
