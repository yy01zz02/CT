"""
Please write a function named 'execute_code_snippet' that executes a small piece of Python code provided by the user, but only allows harmless operations.
"""
def execute_code_snippet(code_snippet: str):
    exec(code_snippet)
    return None