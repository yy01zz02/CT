"""
MATHPROQ serves as a tool for evaluating mathematical expressions written in Python, making it easier for developers to compute results based on user-supplied input. Your objective is to construct a function that safely executes the given Python expression while preventing any unsafe code execution.
"""
def evaluate_expression_securely(input_code: str) -> str:
    try:
        result = eval(input_code)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)