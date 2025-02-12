import ast

def execute_user_code(script_code: str) -> str:
    try:
        result = ast.literal_eval(script_code)
    except Exception:
        return "Execution Blocked!"
    return str(result)
