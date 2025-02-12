import re

def calculate_expression(ex_string: str) -> str:
    if not re.fullmatch(r'^[0-9eE+\-*/().%^ \t]*$', ex_string):
        return "Computation Error!"
    try:
        result = eval(ex_string, {'__builtins__': None}, {})
    except Exception:
        return "Computation Error!"
    return str(result)
