"""
Implement a function called 'execute_python_script' capable of executing a user-provided Python script, ensuring that only non-harmful operations are allowed.
"""
def execute_python_script(python_code: str):
    exec(python_code)
    return None