import ast

def check_expression(node):
    allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
               ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)
    if not isinstance(node, allowed):
        raise ValueError("Disallowed node")
    for child in ast.iter_child_nodes(node):
        check_expression(child)

def compute_expression(expression: str) -> str:
    try:
        tree = ast.parse(expression, mode='eval')
        check_expression(tree)
        result = eval(compile(tree, filename='', mode='eval'))
    except Exception:
        return "Computation Error!"
    return str(result)
