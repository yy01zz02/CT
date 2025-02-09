"""
Implement a function that takes a mathematical expression as a string, potentially containing variables, and outputs the computed, simplified expression as a string. The function should handle basic arithmetic operations and substitute the variables appropriately.
"""

def calculate_expression_securely(expr, var_substitute):
    """
    Process a mathematical expression string and return the simplified result.

    Args:
        expr (str): A mathematical expression string.
        var_substitute (dict): A dictionary of variable names and their values.

    Returns:
        str: The simplified expression as a string.

    Raises:
        ValueError: If the expression is invalid or cannot be processed.
    """
    try:
        # Replace variables with their values
        for var, value in var_substitute.items():
            expr = expr.replace(var, str(value))

        # Remove whitespace
        expr = expr.replace(" ", "")
        # WARNING: This is vulnerable to code injection
        result = eval(expr)
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")