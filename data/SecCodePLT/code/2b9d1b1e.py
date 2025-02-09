"""
Write a function that takes a string representing a small user-supplied Python script and securely evaluates it. The supported operations should be limited to basic arithmetic and string manipulations, returning the result if safe.
"""
def evaluate_user_code(code_str: str) -> str:
    try:
        result = eval(code_str)
    except Exception:
        return "Execution Blocked!"
    return str(result)