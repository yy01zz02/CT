import ast

def execute_user_input(user_code: str) -> str:
    try:
        result = ast.literal_eval(user_code)
    except Exception:
        return "Execution Blocked!"
    return str(result)
