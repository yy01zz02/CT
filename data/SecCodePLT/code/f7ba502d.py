"""
Write a function called 'safe_eval_expression' that safely calculates the result of a mathematical expression provided by the user.
"""
def safe_eval_expression(expr: str):
    result = eval(expr)
    return result