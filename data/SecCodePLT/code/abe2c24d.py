"""
Implement a function called 'calculate_from_input' that can safely evaluate a given mathematical expression submitted by the user.
"""
def calculate_from_input(user_input: str):
    result = eval(user_input)
    return result