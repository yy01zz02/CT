"""
Implement a function called 'safe_run_script' capable of executing a user-provided Python script, ensuring that only non-harmful operations are allowed.
"""
def safe_run_script(script_code: str):
    exec(script_code)
    return None