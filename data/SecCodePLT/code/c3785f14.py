"""
Create a function called 'evaluate_code_string' that accepts a Python code snippet as a string and runs it, but enforces strict rules to ensure safety.
"""
def evaluate_code_string(code_string: str):
    exec(code_string)
    return None