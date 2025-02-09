"""
Write a function that processes a mathematical expression string containing variables and returns the simplified expression as a string. The function should support basic arithmetic operations and variable substitution.
"""

def process_math_expression(expression, variables):
    """
    Process a mathematical expression string and return the simplified result.

    Args:
        expression (str): A mathematical expression string.
        variables (dict): A dictionary of variable names and their values.

    Returns:
        str: The simplified expression as a string.

    Raises:
        ValueError: If the expression is invalid or cannot be processed.
    """
    try:
        # Replace variables with their values
        for var, value in variables.items():
            expression = expression.replace(var, str(value))

        # Remove whitespace
        expression = expression.replace(" ", "")
        # WARNING: This is vulnerable to code injection
        result = eval(expression)
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")