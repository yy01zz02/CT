import ast

def calculate_user_input(user_input: str):
    try:
        tree = ast.parse(user_input, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid expression")
    for node in ast.walk(tree):
        if isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant)):
            if isinstance(node, ast.BinOp) and not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)):
                raise ValueError("Unsupported operator")
            if isinstance(node, ast.UnaryOp) and not isinstance(node.op, ast.USub):
                raise ValueError("Unsupported operator")
        else:
            if not isinstance(node, (ast.Expression, ast.Load)):
                raise ValueError("Disallowed syntax")

    def evaluate_node(node):
        if isinstance(node, ast.Expression):
            return evaluate_node(node.body)
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.UnaryOp):
            operand = evaluate_node(node.operand)
            if isinstance(node.op, ast.USub):
                return -operand
            else:
                raise ValueError("Unsupported unary operator")
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
        else:
            raise ValueError("Unexpected node during evaluation")

    return evaluate_node(tree)