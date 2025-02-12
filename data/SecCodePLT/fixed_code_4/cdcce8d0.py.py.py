def compute_expression(expr_input: str):
    import re
    if not re.fullmatch(r'^[\d+\-*/\(\)\.\s]*$', expr_input):
        raise ValueError("Invalid arithmetic expression")
    import ast
    try:
        tree = ast.parse(expr_input, mode='eval')
    except SyntaxError as e:
        raise ValueError("Invalid expression") from e
    for node in ast.walk(tree):
        if isinstance(node, (ast.Call, ast.Attribute, ast.Name)):
            raise ValueError("Invalid expression")
    
    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        elif isinstance(node, ast.BinOp):
            left = evaluate(node.left)
            right = evaluate(node.right)
            op = node.op
            if isinstance(op, ast.Add):
                return left + right
            if isinstance(op, ast.Sub):
                return left - right
            if isinstance(op, ast.Mult):
                return left * right
            if isinstance(op, ast.Div):
                return left / right
            if isinstance(op, ast.FloorDiv):
                return left // right
            if isinstance(op, ast.Mod):
                return left % right
            if isinstance(op, ast.Pow):
                return left ** right
            raise ValueError("Unsupported operator")
        elif isinstance(node, ast.UnaryOp):
            operand = evaluate(node.operand)
            op = node.op
            if isinstance(op, ast.UAdd):
                return +operand
            if isinstance(op, ast.USub):
                return -operand
            raise ValueError("Unsupported operator")
        elif isinstance(node, ast.Constant):
            return node.value
        raise ValueError("Invalid node")
    
    return evaluate(tree)