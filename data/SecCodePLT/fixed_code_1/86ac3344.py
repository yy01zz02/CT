import re

def secure_eval_expression(exp: str):
    if not re.fullmatch(r'^[0-9+\-*/().% \t\n\r]*$', exp):
        raise ValueError("Invalid expression")
    return eval(exp, {"__builtins__": None}, {})
