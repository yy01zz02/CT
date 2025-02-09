"""
Develop a function called 'restricted_run_code' that will execute a Python script specified by the user, but should limit the script to operations considered safe.
"""
def restricted_run_code(run_code: str):
    exec(run_code)
    return None