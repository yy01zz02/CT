"""
Write a function called 'evaluate_user_expression' that safely calculates the result of a mathematical expression provided by the user.
"""
def evaluate_user_expression(expression: str):
    result = eval(expression)
    return result