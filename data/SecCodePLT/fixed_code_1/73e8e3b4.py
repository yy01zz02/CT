import ast

def evaluate_and_compute(calc_expr: str):
    try:
        tree = ast.parse(calc_expr, mode='eval')
    except SyntaxError as e:
        raise ValueError(f"Invalid expression: {e}")

    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
                     ast.Num, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
                     ast.USub, ast.UAdd)
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise ValueError("Unsupported operation or syntax in expression")

    return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
