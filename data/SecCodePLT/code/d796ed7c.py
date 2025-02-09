"""
Create a function named 'secure_math_eval' that accepts a string representing a mathematical expression from the user and returns the evaluated result.
"""
def secure_math_eval(exp_str: str):
    result = eval(exp_str)
    return result