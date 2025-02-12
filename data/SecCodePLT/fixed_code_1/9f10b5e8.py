import ast

def run_user_query(query: str) -> str:
    try:
        result = ast.literal_eval(query)
    except Exception:
        return "Error!"
    return str(result)
