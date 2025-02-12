import ast

def evaluate_and_compute(calc_expr: str):
    try:
        tree = ast.parse(calc_expr, mode='eval')
    except SyntaxError as e:
        raise ValueError(f"Invalid expression: {e}")

    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
                     ast.Num, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
                     ast.USub, ast.UAdd)
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise ValueError("Unsupported operation or syntax in expression")

    def evaluate_node(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Num):
            return node.n
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
                raise ValueError("Unsupported binary operator")
        elif isinstance(node, ast.UnaryOp):
            operand = evaluate_node(node.operand)
            op = node.op
            if isinstance(op, ast.USub):
                return -operand
            elif isinstance(op, ast.UAdd):
                return +operand
            else:
                raise ValueError("Unsupported unary operator")
        else:
            raise ValueError("Unsupported node type")

    return evaluate_node(tree.body)