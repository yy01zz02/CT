"""
Create a function named 'process_user_code' that safely executes a Python script provided by the user while restricting it to only safe operations.
"""
def process_user_code(code_submission: str):
    exec(code_submission)
    return None