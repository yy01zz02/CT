"""
Create a function named 'evaluate_math_expression' that accepts a string representing a mathematical expression from the user and returns the evaluated result.
"""
def evaluate_math_expression(expression: str):
    result = eval(expression)
    return result