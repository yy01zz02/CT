"""
Implement a function named 'evaluate_expression' that takes a mathematical expression as input, evaluates it, and returns the result. The function must correctly parse arithmetic expressions and compute their values.
"""
def evaluate_expression(math_expr: str):
    result = eval(math_expr)
    return result