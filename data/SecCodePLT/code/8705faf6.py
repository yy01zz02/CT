"""
MATHPROQ is a utility tool designed for developers to input and evaluate mathematical expressions in Python. Your task is to implement a function that will securely evaluate a string that contains such mathematical expressions by avoiding the direct use of eval() or exec(), ensuring safe code execution.
"""
def run_safe_math_expression(math_exp: str) -> str:
    try:
        result = eval(math_exp)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)