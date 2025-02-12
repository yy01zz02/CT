import ast

def compute_expression(query_str: str) -> str:
    try:
        result = ast.literal_eval(query_str)
    except Exception:
        return "Error!"
    return str(result)
