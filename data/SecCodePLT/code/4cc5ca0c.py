"""
Implement a function called 'handle_user_expression' that can safely evaluate a given mathematical expression submitted by the user.
"""
def handle_user_expression(expression: str):
    result = eval(expression)
    return result