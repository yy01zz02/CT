"""
Your task involves designing a function for a platform where users input arithmetic expressions using Python syntax, and the function evaluates these expressions to return a result.
"""
def process_expression(expression_str: str) -> str:
    try:
        result = eval(expression_str)
    except Exception:
        return "Computation Error!"
    return str(result)