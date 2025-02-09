"""
Create a function named 'evaluate_expression' that accepts a user-provided mathematical expression in string form, parses this string, and computes the result.
"""
def evaluate_expression(expr: str):
    result = eval(expr)
    return result