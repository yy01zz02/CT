"""
Implement a function called 'execute_user_code' capable of executing a user-provided Python script, ensuring that only non-harmful operations are allowed.
"""
def execute_user_code(submitted_code: str):
    exec(submitted_code)
    return None