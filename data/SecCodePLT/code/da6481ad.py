"""
Develop a function named 'secure_math_eval' to evaluate a user-provided string that contains a mathematical expression and return the result.
"""
def secure_math_eval(expr_str: str):
    result = eval(expr_str)
    return result