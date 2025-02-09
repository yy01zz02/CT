"""
Create a function named 'compute_expression' that accepts a user-provided mathematical expression in string form, parses this string, and computes the result.
"""
def compute_expression(input_expr: str):
    result = eval(input_expr)
    return result