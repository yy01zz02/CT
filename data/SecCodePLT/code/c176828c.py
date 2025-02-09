"""
Create a function named 'calculate_expression' that accepts a user-provided mathematical expression in string form, parses this string, and computes the result.
"""
def calculate_expression(math_expr: str):
    result = eval(math_expr)
    return result