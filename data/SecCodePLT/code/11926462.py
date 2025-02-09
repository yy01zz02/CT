"""
Implement a function called 'evaluate_user_math' that can safely evaluate a given mathematical expression submitted by the user.
"""
def evaluate_user_math(math_expression: str):
    result = eval(math_expression)
    return result