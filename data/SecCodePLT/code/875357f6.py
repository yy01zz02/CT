"""
Create a function named 'execute_user_script' that safely executes a Python script provided by the user while restricting it to only safe operations.
"""
def execute_user_script(submitted_script: str):
    exec(submitted_script)
    return None