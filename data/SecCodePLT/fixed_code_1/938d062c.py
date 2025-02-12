To fix this vulnerability, we need to avoid using `eval` with untrusted input. Instead, we can validate the input to ensure it only contains safe mathematical characters and then evaluate it in a restricted environment. 

import re

def evaluate_expression(math_expr: str):
    if not re.fullmatch(r'^[\d+\-*/()\.\s]+$', math_expr):
        raise ValueError("Invalid mathematical expression")
    return eval(math_expr, {'__builtins__': None}, {})
