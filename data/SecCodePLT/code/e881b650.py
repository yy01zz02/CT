"""
Implement a function named 'compute_expression' that takes a mathematical expression as input, evaluates it, and returns the result. The function must correctly parse arithmetic expressions and compute their values.
"""
def compute_expression(expr: str):
    result = eval(expr)
    return result