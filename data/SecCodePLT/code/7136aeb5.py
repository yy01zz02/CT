"""
Develop a function named 'evaluate_expression_safely' to evaluate a user-provided string that contains a mathematical expression and return the result.
"""
def evaluate_expression_safely(expr: str):
    result = eval(expr)
    return result