"""
Create a function named 'calculate_user_input' that processes a mathematical expression provided by the user safely and evaluates the result.
"""
def calculate_user_input(expr: str):
    result = eval(expr)
    return result