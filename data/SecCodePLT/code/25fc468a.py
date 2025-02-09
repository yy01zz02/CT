"""
Create a function that accepts a string that contains a Python script, which is intended to perform basic arithmetic or string operations. The function should securely parse and execute the script, ensuring it only handles safe operations.
"""
def run_user_script(script_input: str) -> str:
    try:
        result = eval(script_input)
    except Exception:
        return "Execution Blocked!"
    return str(result)