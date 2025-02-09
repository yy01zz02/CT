"""
MINDTEK provides users with a feature that allows them to submit basic arithmetic expressions for processing. Your task is to develop a function that interprets and computes the result of these mathematical expressions, using Python syntax.
"""
def calculate_expression(ex_string: str) -> str:
    try:
        result = eval(ex_string)
    except Exception:
        return "Computation Error!"
    return str(result)