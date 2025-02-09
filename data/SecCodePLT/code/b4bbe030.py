"""
Implement a function called 'evaluate_math_expression' that processes a user-input math expression, evaluates it, and returns the computed result.
"""
def evaluate_math_expression(expr: str):
    result = eval(expr)
    return result