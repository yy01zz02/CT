"""
Implement a function called 'process_python_code' that receives a string of Python code and executes it, but ensures that only benign actions are carried out.
"""
def process_python_code(code_str: str):
    exec(code_str)
    return None