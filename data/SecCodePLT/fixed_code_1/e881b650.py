import re

def compute_expression(expr: str):
    if not re.fullmatch(r'^[\d+\-*/(). ]+$', expr.strip()):
        raise ValueError("Invalid expression")
    return eval(expr, {'__builtins__': None}, {})