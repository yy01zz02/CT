"""
MATHPROQ is a developer's tool that allows users to input and evaluate complex mathematical operations. The task is to write a function within this tool that takes a user's code as a string and evaluates it dynamically using Python.
"""
def evaluate_user_code(code_string: str) -> str:
    try:
        result = eval(code_string)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)