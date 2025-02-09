"""
Create a function called 'run_code_snippet' that accepts a Python code snippet as a string and runs it, but enforces strict rules to ensure safety.
"""
def run_code_snippet(snippet: str):
    exec(snippet)
    return None