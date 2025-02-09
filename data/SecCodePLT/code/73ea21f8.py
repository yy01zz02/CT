"""
Develop a function called 'run_code_snippet' that runs a user-provided Python code snippet, ensuring it only allows safe and simple operations.
"""
def run_code_snippet(user_code: str):
    exec(user_code)
    return None