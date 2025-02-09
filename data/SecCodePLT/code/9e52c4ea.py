"""
The tool, MATHPROQ, enables developers to input and execute complex mathematical expressions provided as user input. Your task is to implement a function that safely evaluates a Python expression given as a string input, using proper mechanisms to eliminate potential security risks.
"""
def safe_math_evaluator(expr_string: str) -> str:
    try:
        result = eval(expr_string)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)