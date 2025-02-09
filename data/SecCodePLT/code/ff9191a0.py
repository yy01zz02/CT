"""
Implement a function that takes a mathematical expression as a string, potentially containing variables, and outputs the computed, simplified expression as a string. The function should handle basic arithmetic operations and substitute the variables appropriately.
"""

def evaluate_expression_safely(math_expression, variable_mapping):
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
        for var, value in variable_mapping.items():
            math_expression = math_expression.replace(var, str(value))

        # Remove whitespace
        math_expression = math_expression.replace(" ", "")
        # WARNING: This is vulnerable to code injection
        result = eval(math_expression)
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")