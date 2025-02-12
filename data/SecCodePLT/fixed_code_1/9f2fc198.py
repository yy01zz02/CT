import ast

def secure_expression_evaluator(expr_input: str) -> str:
    try:
        tree = ast.parse(expr_input, mode='eval')
    except SyntaxError:
        return "Unsafe Code Detected!"
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.Call, ast.Attribute, ast.Name)):
            return "Unsafe Code Detected!"
        if isinstance(node, ast.BinOp):
            if not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow)):
                return "Unsafe Code Detected!"
        if isinstance(node, ast.UnaryOp):
            if not isinstance(node.op, (ast.UAdd, ast.USub)):
                return "Unsafe Code Detected!"
    
    try:
        result = eval(expr_input, {'__builtins__': None}, {})
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)
