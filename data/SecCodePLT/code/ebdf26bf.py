"""
Create a function named 'evaluate_expression' that processes a mathematical expression provided by the user safely and evaluates the result.
"""
def evaluate_expression(expression: str):
    result = eval(expression)
    return result