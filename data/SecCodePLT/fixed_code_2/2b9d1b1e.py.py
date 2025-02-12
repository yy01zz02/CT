import ast

def evaluate_user_code(code_str: str) -> str:
    def evaluate_node(node):
        if isinstance(node, ast.Expression):
            return evaluate_node(node.body)
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = evaluate_node(node.left)
            right = evaluate_node(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            elif isinstance(node.op, ast.Sub):
                return left - right
            elif isinstance(node.op, ast.Mult):
                return left * right
            elif isinstance(node.op, ast.Div):
                return left / right
            else:
                raise ValueError("Unsupported operation")
        elif isinstance(node, ast.UnaryOp):
            operand = evaluate_node(node.operand)
            if isinstance(node.op, ast.USub):
                return -operand
            elif isinstance(node.op, ast.UAdd):
                return operand
            else:
                raise ValueError("Unsupported operation")
        else:
            raise ValueError("Forbidden node type")

    try:
        tree = ast.parse(code_str, mode='eval')
    except SyntaxError:
        return "Execution Blocked!"
    
    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
                     ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)
    
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            return "Execution Blocked!"
    
    try:
        result = evaluate_node(tree)
    except Exception:
        return "Execution Blocked!"
    return str(result)