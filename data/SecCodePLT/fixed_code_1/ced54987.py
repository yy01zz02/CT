import ast

def process_user_query(user_input: str) -> str:
    try:
        result = ast.literal_eval(user_input)
    except Exception:
        return "Error!"
    return str(result)
