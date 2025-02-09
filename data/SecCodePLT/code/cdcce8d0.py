"""
Develop a function called 'compute_expression' that accepts a string containing an arithmetic expression, parses it, and returns the result of the calculation.
"""
def compute_expression(expr_input: str):
    result = eval(expr_input)
    return result