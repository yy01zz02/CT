import ast

def check_expression(node):
    allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
               ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)
    if not isinstance(node, allowed):
        raise ValueError("Disallowed node")
    for child in ast.iter_child_nodes(node):
        check_expression(child)

def _evaluate_node(node):
    if isinstance(node, ast.Expression):
        return _evaluate_node(node.body)
    elif isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right
    elif isinstance(node, ast.UnaryOp):
        operand = _evaluate_node(node.operand)
        if isinstance(node.op, ast.USub):
            return -operand
        elif isinstance(node.op, ast.UAdd):
            return +operand
    raise ValueError("Unsupported node")

def compute_expression(expression: str) -> str:
    try:
        tree = ast.parse(expression, mode='eval')
        check_expression(tree)
        result = _evaluate_node(tree)
    except Exception:
        return "Computation Error!"
    return str(result)