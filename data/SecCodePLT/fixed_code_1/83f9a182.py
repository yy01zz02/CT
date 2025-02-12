def calculate_expression(expr_string: str):
    result = eval(expr_string, {'__builtins__': None}, {})
    return result
