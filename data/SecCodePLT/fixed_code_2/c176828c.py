def calculate_expression(math_expr: str):
    import re
    sanitized_expr = math_expr.replace(" ", "")
    if not re.fullmatch(r'^[\d+\-*/().]+$', sanitized_expr):
        raise ValueError("Invalid mathematical expression")
    return eval(sanitized_expr, {'__builtins__': None}, {})