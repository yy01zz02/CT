"""
Implement a function called 'run_python_snippet' that receives a string of Python code and executes it, but ensures that only benign actions are carried out.
"""
def run_python_snippet(snippet_string: str):
    exec(snippet_string)
    return None