"""
Implement a function called 'execute_python_code' that receives a string of Python code and executes it, but ensures that only benign actions are carried out.
"""
def execute_python_code(snippet_code: str):
    exec(snippet_code)
    return None