import ast

def execute_user_input(user_code: str) -> str:
    try:
        tree = ast.parse(user_code, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute, ast.Name, ast.Import, ast.ImportFrom)):
                raise ValueError
        compiled = compile(tree, '<string>', 'eval')
        result = eval(compiled, {"__builtins__": None}, {})
    except Exception:
        return "Execution Blocked!"
    return str(result)
