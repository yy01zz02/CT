import ast

def compute_math_expression(expression_input: str):
    try:
        tree = ast.parse(expression_input, mode='eval')
    except SyntaxError:
        return None
    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
                     ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd)
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            return None
    try:
        return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
    except:
        return None
