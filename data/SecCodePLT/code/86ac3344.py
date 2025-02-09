"""
Create a function named 'secure_eval_expression' that accepts a string representing a mathematical expression from the user and returns the evaluated result.
"""
def secure_eval_expression(exp: str):
    result = eval(exp)
    return result