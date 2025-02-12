Here's the fixed code:

import ast

def evaluate_input_expression(expression: str) -> str:
    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError:
        return "Processing Failed!"
    
    allowed_nodes = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
        ast.Num, ast.Compare, ast.BoolOp, ast.Add, ast.Sub,
        ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow,
        ast.USub, ast.UAdd, ast.Eq, ast.NotEq, ast.Lt,
        ast.LtE, ast.Gt, ast.GtE, ast.And, ast.Or
    )
    
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            return "Processing Failed!"
    
    try:
        result = eval(compile(tree, filename='', mode='eval'), {'__builtins__': None}, {})
    except Exception:
        return "Processing Failed!"
    
    return str(result)
