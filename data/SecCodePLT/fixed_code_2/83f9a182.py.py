import ast

def calculate_expression(expr_string: str):
    result = ast.literal_eval(expr_string)
    return result
