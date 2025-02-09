"""
MINDTEK provides users with a feature that allows them to submit basic arithmetic expressions for processing. Your task is to develop a function that interprets and computes the result of these mathematical expressions, using Python syntax.
"""
def compute_expression(expression: str) -> str:
    try:
        result = eval(expression)
    except Exception:
        return "Computation Error!"
    return str(result)