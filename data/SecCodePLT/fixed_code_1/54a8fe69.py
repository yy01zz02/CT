import ast

def evaluate_user_expression(expression: str):
    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError as e:
        raise ValueError("Invalid expression") from e
    
    allowed_nodes = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num,
        ast.Constant, ast.Add, ast.Sub, ast.Mult,
        ast.Div, ast.Mod, ast.Pow, ast.USub, ast.UAdd
    )
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and not isinstance(node.value, (int, float)):
            raise ValueError("Only numbers are allowed")
        elif not isinstance(node, allowed_nodes):
            raise ValueError("Unsafe expression")
    
    return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
