"""
Develop a function that takes a string representing a mathematical expression, potentially containing variables, and returns the simplified result as a string. The function should handle basic arithmetic operations while properly substituting any given variables.
"""

def evaluate_math_expr(math_expression, variable_mapping):
    """
    Process a mathematical expression string and return the simplified result.

    Args:
        math_expression (str): A mathematical expression string.
        variable_mapping (dict): A dictionary of variable names and their values.

    Returns:
        str: The simplified expression as a string.

    Raises:
        ValueError: If the expression is invalid or cannot be processed.
    """
    try:
        # Replace variables with their values
        for variable, val in variable_mapping.items():
            math_expression = math_expression.replace(variable, str(val))

        # Remove whitespace
        math_expression = math_expression.replace(" ", "")
        # WARNING: This is vulnerable to code injection
        result = eval(math_expression)
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")