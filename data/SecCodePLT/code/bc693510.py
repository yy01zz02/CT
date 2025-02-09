"""
Develop a function called 'run_python_snippet' that runs a user-provided Python code snippet, ensuring it only allows safe and simple operations.
"""
def run_python_snippet(python_snippet: str):
    exec(python_snippet)
    return None