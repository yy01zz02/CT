import ast

def evaluate_math_expression(expression: str):
    expr = expression.strip().replace(" ", "")
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid mathematical expression.")
    
    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Num, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod, ast.USub)
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.Call, ast.Name, ast.Attribute, ast.Subscript)):
            raise ValueError("Expression contains disallowed elements.")
        if not isinstance(node, allowed_nodes):
            raise ValueError("Expression contains disallowed elements.")
    
    return eval(expr, {'__builtins__': None}, {})
