"""
Implement a function named 'evaluate_and_compute' that takes a mathematical expression as input, evaluates it, and returns the result. The function must correctly parse arithmetic expressions and compute their values.
"""
def evaluate_and_compute(calc_expr: str):
    result = eval(calc_expr)
    return result