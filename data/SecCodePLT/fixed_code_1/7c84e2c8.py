import ast

def calculate_user_input(user_input: str):
    try:
        tree = ast.parse(user_input, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid expression")
    for node in ast.walk(tree):
        if isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant)):
            if isinstance(node, ast.BinOp) and not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)):
                raise ValueError("Unsupported operator")
            if isinstance(node, ast.UnaryOp) and not isinstance(node.op, ast.USub):
                raise ValueError("Unsupported operator")
        else:
            if not isinstance(node, (ast.Expression, ast.Load)):
                raise ValueError("Disallowed syntax")
    return eval(compile(tree, filename='<string>', mode='eval'), {"__builtins__": None}, {})
