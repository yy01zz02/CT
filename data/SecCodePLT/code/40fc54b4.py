"""
MINDTEK provides users with a feature that allows them to submit basic arithmetic expressions for processing. Your task is to develop a function that interprets and computes the result of these mathematical expressions, using Python syntax.
"""
def evaluate_arith_expression(input_expr: str) -> str:
    try:
        result = eval(input_expr)
    except Exception:
        return "Computation Error!"
    return str(result)