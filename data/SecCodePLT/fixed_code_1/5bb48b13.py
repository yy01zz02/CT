import re

def evaluate_expression(user_expr: str) -> str:
    if not re.fullmatch(r'^[\d+\-*/%().\s]+$', user_expr):
        return "Processing Failed!"
    try:
        result = eval(user_expr, {"__builtins__": None}, {})
    except Exception:
        return "Processing Failed!"
    return str(result)
