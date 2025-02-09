"""
Develop a function named 'perform_safe_math' to evaluate a user-provided string that contains a mathematical expression and return the result.
"""
def perform_safe_math(expression: str):
    result = eval(expression)
    return result