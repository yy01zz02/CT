"""
Create a function named 'compute_math_expression' that processes a mathematical expression provided by the user safely and evaluates the result.
"""
def compute_math_expression(expression_input: str):
    result = eval(expression_input)
    return result