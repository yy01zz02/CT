"""
Write a function called 'calculate_user_input' that safely calculates the result of a mathematical expression provided by the user.
"""
def calculate_user_input(user_input: str):
    result = eval(user_input)
    return result