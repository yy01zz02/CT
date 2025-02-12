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

    def evaluate(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = evaluate(node.left)
            right = evaluate(node.right)
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
        elif isinstance(node, ast.UnaryOp):
            operand = evaluate(node.operand)
            op = node.op
            if isinstance(op, ast.USub):
                return -operand
            elif isinstance(op, ast.UAdd):
                return +operand
        elif isinstance(node, ast.Expression):
            return evaluate(node.body)
        raise ValueError("Invalid node")

    try:
        return evaluate(tree)
    except:
        return None
