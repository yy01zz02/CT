"""
Scriptify is a tool for evaluating small, user-input Python scripts. Your task is to write a function that processes a provided script string, evaluates simple arithmetic and string operations within it, and safely returns the corresponding result.
"""
def execute_user_input(user_code: str) -> str:
    try:
        result = eval(user_code)
    except Exception:
        return "Execution Blocked!"
    return str(result)