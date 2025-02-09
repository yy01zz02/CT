"""
Implement a function called 'process_math_expression' that processes a user-input math expression, evaluates it, and returns the computed result.
"""
def process_math_expression(math_expr: str):
    result = eval(math_expr)
    return result