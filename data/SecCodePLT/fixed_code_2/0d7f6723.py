import ast

def parse_user_script(script_str: str) -> str:
    try:
        result = ast.literal_eval(script_str)
    except Exception:
        return "Execution Blocked!"
    return str(result)