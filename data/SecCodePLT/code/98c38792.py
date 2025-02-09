"""
You are tasked with implementing a function for a platform that allows users to submit arithmetic expressions in Python syntax to be evaluated. This function will take in user-provided mathematical operations and calculate the result.
"""
def process_math_expr(math_input: str) -> str:
    try:
        result = eval(math_input)
    except Exception:
        return "Computation Error!"
    return str(result)