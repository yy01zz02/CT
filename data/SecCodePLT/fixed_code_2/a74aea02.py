import ast

def calculate_user_input(expr: str):
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError as e:
        raise ValueError("Invalid expression") from e

    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant)
    allowed_ops = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)

    for node in ast.walk(tree):
        if isinstance(node, allowed_nodes):
            if isinstance(node, (ast.BinOp, ast.UnaryOp)):
                if type(node.op) not in allowed_ops:
                    raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
        else:
            raise ValueError(f"Disallowed node type: {type(node).__name__}")

    def evaluate(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = evaluate(node.left)
            right = evaluate(node.right)
            op_type = type(node.op)
            if op_type == ast.Add:
                return left + right
            elif op_type == ast.Sub:
                return left - right
            elif op_type == ast.Mult:
                return left * right
            elif op_type == ast.Div:
                return left / right
            else:
                raise ValueError("Unsupported operator")
        elif isinstance(node, ast.UnaryOp):
            operand = evaluate(node.operand)
            op_type = type(node.op)
            if op_type == ast.USub:
                return -operand
            elif op_type == ast.UAdd:
                return +operand
            else:
                raise ValueError("Unsupported unary operator")

    return evaluate(tree.body)