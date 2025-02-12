import ast

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
        compiled = compile(tree, filename='<string>', mode='eval')
        result = eval(compiled, {'__builtins__': None}, {})
    except Exception:
        return "Execution Blocked!"
    
    return str(result)
