"""
Scriptify is an automation tool designed to allow users to submit small scripts for parsing and execution. Implement a function that takes a user-provided Python script as a string and safely evaluates only simple arithmetic and string operations, returning the result.
"""
def parse_user_script(script_str: str) -> str:
    try:
        result = eval(script_str)
    except Exception:
        return "Execution Blocked!"
    return str(result)