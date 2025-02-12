import ast

def secure_math_eval(exp_str: str):
    try:
        tree = ast.parse(exp_str, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid mathematical expression")
    allowed_nodes = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.UAdd, ast.USub
    )
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise ValueError("Disallowed operation detected")
    return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
