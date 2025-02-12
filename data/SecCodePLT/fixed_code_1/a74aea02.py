import ast

def calculate_user_input(expr: str):
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError as e:
        raise ValueError("Invalid expression") from e

    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant)
    allowed_ops = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)

    for node in ast.walk(tree):
        if isinstance(node, allowed_nodes):
            if isinstance(node, (ast.BinOp, ast.UnaryOp)):
                if type(node.op) not in allowed_ops:
                    raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
        else:
            raise ValueError(f"Disallowed node type: {type(node).__name__}")

    return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
