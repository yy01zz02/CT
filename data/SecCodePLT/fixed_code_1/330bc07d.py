import ast

def process_user_expression(query_expr: str) -> str:
    try:
        result = ast.literal_eval(query_expr)
    except Exception:
        return "Error!"
    return str(result)
