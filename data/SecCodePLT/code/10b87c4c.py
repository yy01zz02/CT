"""
Create a function called 'process_code_input' that accepts a Python code snippet as a string and runs it, but enforces strict rules to ensure safety.
"""
def process_code_input(code_input: str):
    exec(code_input)
    return None