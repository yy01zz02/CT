"""
Create a function named 'evaluate_user_input' that safely executes a Python script provided by the user while restricting it to only safe operations.
"""
def evaluate_user_input(user_code: str):
    exec(user_code)
    return None