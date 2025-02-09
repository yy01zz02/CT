"""
Please write a function named 'run_user_script' that allows executing a Python script supplied by the user. The script should be limited to safe operations only.
"""
def run_user_script(user_script: str):
    exec(user_script)
    return None