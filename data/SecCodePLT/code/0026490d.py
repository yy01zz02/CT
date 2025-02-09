"""
Develop a function called 'evaluate_expression' that accepts a string containing an arithmetic expression, parses it, and returns the result of the calculation.
"""
def evaluate_expression(expr: str):
    result = eval(expr)
    return result