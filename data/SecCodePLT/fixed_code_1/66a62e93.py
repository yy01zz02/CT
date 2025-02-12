Here's the fixed code:

import ast

def evaluate_user_code(code_string: str) -> str:
    try:
        result = ast.literal_eval(code_string)
    except Exception:
        return "Execution Blocked!"
    return str(result)
