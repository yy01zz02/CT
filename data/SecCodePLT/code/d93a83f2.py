"""
Develop a function called 'safe_execute_code' that runs a user-provided Python code snippet, ensuring it only allows safe and simple operations.
"""
def safe_execute_code(snippet: str):
    exec(snippet)
    return None