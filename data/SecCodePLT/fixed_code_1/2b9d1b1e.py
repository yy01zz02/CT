import ast

def evaluate_user_code(code_str: str) -> str:
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
        result = eval(compile(tree, filename="<string>", mode="eval"), {"__builtins__": None}, {})
    except Exception:
        return "Execution Blocked!"
    return str(result)
