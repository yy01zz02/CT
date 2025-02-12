import ast

def process_user_input(user_query: str) -> str:
    try:
        result = ast.literal_eval(user_query)
    except Exception:
        return "Error!"
    return str(result)
