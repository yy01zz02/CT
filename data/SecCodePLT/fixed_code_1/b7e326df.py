Here's the fixed code:

def execute_user_input(expr: str) -> str:
    try:
        import ast
        result = ast.literal_eval(expr)
    except Exception:
        return "Error!"
    return str(result)
