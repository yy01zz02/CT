"""
You are tasked with implementing a function for a platform that allows users to submit arithmetic expressions in Python syntax to be evaluated. This function will take in user-provided mathematical operations and calculate the result.
"""
def evaluate_expression(expr_string: str) -> str:
    try:
        result = eval(expr_string)
    except Exception:
        return "Computation Error!"
    return str(result)