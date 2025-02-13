import ast

def exec_calculation(calc_string: str) -> str:
    allowed_chars = set("0123456789+-*/%.() ")
    if not all(c in allowed_chars for c in calc_string):
        return "Computation Error!"
    try:
        result = ast.literal_eval(calc_string)
    except Exception:
        return "Computation Error!"
    return str(result)