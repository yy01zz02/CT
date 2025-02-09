"""
Develop a function called 'calculate_expression' that accepts a string containing an arithmetic expression, parses it, and returns the result of the calculation.
"""
def calculate_expression(expr_string: str):
    result = eval(expr_string)
    return result