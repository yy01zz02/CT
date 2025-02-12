import ast

def evaluate_expression(node):
    if isinstance(node, ast.Expression):
        return evaluate_expression(node.body)
    if isinstance(node, (ast.Constant, ast.Num, ast.Str)):
        return getattr(node, 'value', getattr(node, 'n', getattr(node, 's', None)))
    elif isinstance(node, ast.BinOp):
        left = evaluate_expression(node.left)
        right = evaluate_expression(node.right)
        op_type = type(node.op)
        if op_type == ast.Add:
            return left + right
        elif op_type == ast.Sub:
            return left - right
        elif op_type == ast.Mult:
            return left * right
        elif op_type == ast.Div:
            return left / right
        elif op_type == ast.Mod:
            return left % right
        elif op_type == ast.Pow:
            return left ** right
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate_expression(node.operand)
        op_type = type(node.op)
        if op_type == ast.USub:
            return -operand
        elif op_type == ast.UAdd:
            return operand
    raise ValueError("Unsupported operation")

def run_user_script(script_input: str) -> str:
    try:
        tree = ast.parse(script_input, mode='eval')
    except SyntaxError:
        return "Execution Blocked!"
    
    allowed_nodes = {
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Num, ast.Str,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.USub, ast.UAdd
    }
    
    for node in ast.walk(tree):
        if type(node) not in allowed_nodes:
            return "Execution Blocked!"
    
    try:
        result = evaluate_expression(tree)
    except:
        return "Execution Blocked!"
    
    return str(result)