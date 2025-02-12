import re

def evaluate_user_math(math_expr: str) -> str:
    if not re.match(r'^[\d+\-*/()%.^ &]+$', math_expr):
        return "Processing Failed!"
    try:
        sanitized = math_expr.replace('^', '**').replace('&', '//')
        result = eval(sanitized, {"__builtins__": None}, {})
        return str(result)
    except Exception:
        return "Processing Failed!"
