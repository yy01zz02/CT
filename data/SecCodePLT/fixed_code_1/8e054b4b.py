import re

def calculate_expression(expression: str) -> str:
    if not re.fullmatch(r'^[\d+\-*/().^ \s]+$', expression):
        return "Invalid Expression!"
    try:
        result = eval(expression, {'__builtins__': None}, {})
    except Exception:
        return "Invalid Expression!"
    return str(result)
