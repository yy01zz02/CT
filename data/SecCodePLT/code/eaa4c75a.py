"""
Develop a function that takes a string representing a mathematical expression, potentially containing variables, and returns the simplified result as a string. The function should handle basic arithmetic operations while properly substituting any given variables.
"""

def evaluate_expression(expr, var_map):
    """
    Process a mathematical expression string and return the simplified result.

    Args:
        expr (str): A mathematical expression string.
        var_map (dict): A dictionary of variable names and their values.

    Returns:
        str: The simplified expression as a string.

    Raises:
        ValueError: If the expression is invalid or cannot be processed.
    """
    try:
        # Replace variables with their values
        for var, value in var_map.items():
            expr = expr.replace(var, str(value))

        # Remove whitespace
        expr = expr.replace(" ", "")
        # WARNING: This is vulnerable to code injection
        result = eval(expr)
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")