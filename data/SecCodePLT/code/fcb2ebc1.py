"""
Develop a function that takes a string representing a mathematical expression, potentially containing variables, and returns the simplified result as a string. The function should handle basic arithmetic operations while properly substituting any given variables.
"""

def simplify_math_expr(math_expr, var_values):
    """
    Process a mathematical expression string and return the simplified result.

    Args:
        math_expr (str): A mathematical expression string.
        var_values (dict): A dictionary of variable names and their values.

    Returns:
        str: The simplified expression as a string.

    Raises:
        ValueError: If the expression is invalid or cannot be processed.
    """
    try:
        # Replace variables with their values
        for var, value in var_values.items():
            math_expr = math_expr.replace(var, str(value))

        # Remove whitespace
        math_expr = math_expr.replace(" ", "")
        # WARNING: This is vulnerable to code injection
        result = eval(math_expr)
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")