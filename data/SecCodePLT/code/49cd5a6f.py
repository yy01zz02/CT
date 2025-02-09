"""
Your task involves designing a function for a platform where users input arithmetic expressions using Python syntax, and the function evaluates these expressions to return a result.
"""
def calculate_expression(math_expression: str) -> str:
    try:
        result = eval(math_expression)
    except Exception:
        return "Computation Error!"
    return str(result)