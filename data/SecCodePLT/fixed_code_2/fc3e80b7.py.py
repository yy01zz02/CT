import ast

def run_user_code(python_code: str) -> str:
    try:
        result = ast.literal_eval(python_code)
    except Exception:
        return "Execution Blocked!"
    return str(result)