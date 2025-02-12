To fix the vulnerability in the code where `eval` is used unsafely, we need to ensure that only mathematical expressions are evaluated. This involves parsing and validating the input to restrict it to safe arithmetic operations. Here's how the code is secured:

1. **Import AST**: Use Python's `ast` module to parse and analyze the abstract syntax tree of the input.
2. **Parse and Validate Syntax**: Parse the input expression to check for valid syntax. Any invalid syntax raises an error.
3. **Check AST Nodes**: Walk through the parsed AST to ensure only allowed node types (related to arithmetic operations and numeric literals) are present.
4. **Restricted Evaluation**: Evaluate the validated expression in a restricted environment with no access to built-in functions or external variables.

import ast

def process_math_expression(math_expr: str):
    try:
        tree = ast.parse(math_expr, mode='eval')
    except SyntaxError as e:
        raise ValueError("Invalid math expression") from e

    allowed_nodes = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd, ast.Pow
    )

    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise ValueError("Disallowed node in expression")

    return eval(math_expr, {'__builtins__': None}, {})
