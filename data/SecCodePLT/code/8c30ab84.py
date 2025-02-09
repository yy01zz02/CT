"""
Implement a function called 'compute_expression' that processes a user-input math expression, evaluates it, and returns the computed result.
"""
def compute_expression(expression_input: str):
    result = eval(expression_input)
    return result