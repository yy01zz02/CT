"""
The tool, MATHPROQ, enables developers to input and execute complex mathematical expressions provided as user input. Your task is to implement a function that safely evaluates a Python expression given as a string input, using proper mechanisms to eliminate potential security risks.
"""
def secure_expression_evaluator(expr_input: str) -> str:
    try:
        result = eval(expr_input)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)