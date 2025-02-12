import re

def process_expression(expression_str: str) -> str:
    allowed_pattern = re.compile(r'^[\d+\-*/%().\s]+$')
    if not allowed_pattern.match(expression_str):
        return "Computation Error!"
    try:
        result = eval(expression_str, {"__builtins__": None}, {})
    except Exception:
        return "Computation Error!"
    return str(result)
