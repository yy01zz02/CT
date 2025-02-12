import ast

def evaluate_expression(expr: str) -> str:
    try:
        result = ast.literal_eval(expr)
    except Exception:
        return "Error!"
    return str(result)
