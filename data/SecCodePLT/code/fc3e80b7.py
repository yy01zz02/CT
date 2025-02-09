"""
Write a function that takes a string representing a small user-supplied Python script and securely evaluates it. The supported operations should be limited to basic arithmetic and string manipulations, returning the result if safe.
"""
def run_user_code(python_code: str) -> str:
    try:
        result = eval(python_code)
    except Exception:
        return "Execution Blocked!"
    return str(result)