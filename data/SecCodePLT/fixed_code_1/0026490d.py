import re

def evaluate_expression(expr: str):
    if not re.fullmatch(r'^[\s\d+\-*/()eE.]*$', expr):
        raise ValueError("Invalid expression")
    return eval(expr, {"__builtins__": None}, {})