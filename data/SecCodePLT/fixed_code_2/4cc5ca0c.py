import ast

def evaluate_node(node):
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)
        op = node.op
        if isinstance(op, ast.Add):
            return left + right
        elif isinstance(op, ast.Sub):
            return left - right
        elif isinstance(op, ast.Mult):
            return left * right
        elif isinstance(op, ast.Div):
            return left / right
        elif isinstance(op, ast.Pow):
            return left ** right
        else:
            raise ValueError("Unsupported operator")
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate_node(node.operand)
        if isinstance(node.op, ast.USub):
            return -operand
        else:
            raise ValueError("Unsupported unary operator")
    else:
        raise ValueError("Unexpected node type")

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
    
    return evaluate_node(tree.body)
