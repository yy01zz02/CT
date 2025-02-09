"""
Develop a function called 'execute_user_code' that will execute a Python script specified by the user, but should limit the script to operations considered safe.
"""
def execute_user_code(script_to_execute: str):
    exec(script_to_execute)
    return None