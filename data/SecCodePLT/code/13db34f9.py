"""
Create a function that processes a mathematical expression in the form of a string, which may include variables, and returns the calculated, simplified result as a string. The function should handle basic arithmetic operations and correctly substitute variables given in a dictionary.
"""

def evaluate_math_expression(formula, vars):
    """
    Process a mathematical expression string and return the simplified result.

    Args:
        formula (str): A mathematical expression string.
        vars (dict): A dictionary of variable names and their values.

    Returns:
        str: The simplified expression as a string.

    Raises:
        ValueError: If the expression is invalid or cannot be processed.
    """
    try:
        # Replace variables with their values
        for var_key, value in vars.items():
            formula = formula.replace(var_key, str(value))

        # Remove whitespace
        formula = formula.replace(" ", "")
        # WARNING: This is vulnerable to code injection
        result = eval(formula)
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")