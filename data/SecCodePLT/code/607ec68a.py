"""
Develop a function called 'safe_run_script' that will execute a Python script specified by the user, but should limit the script to operations considered safe.
"""
def safe_run_script(code: str):
    exec(code)
    return None