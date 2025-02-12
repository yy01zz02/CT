import ast

def handle_user_expression(expression: str):
    tree = ast.parse(expression, mode='eval')
    
    allowed = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub
    )
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if not isinstance(node.value, (int, float)):
                raise ValueError("Only numeric expressions are allowed")
        elif not isinstance(node, allowed):
            raise ValueError("Unsafe operation detected")
    
    return eval(compile(tree, filename='', mode='eval'))