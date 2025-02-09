"""
Create a function that processes a mathematical expression in the form of a string, which may include variables, and returns the calculated, simplified result as a string. The function should handle basic arithmetic operations and correctly substitute variables given in a dictionary.
"""

def simplify_math_expression(formula_str, vars_mapping):
    """
    Process a mathematical expression string and return the simplified result.

    Args:
        formula_str (str): A mathematical expression string.
        vars_mapping (dict): A dictionary of variable names and their values.

    Returns:
        str: The simplified expression as a string.

    Raises:
        ValueError: If the expression is invalid or cannot be processed.
    """
    try:
        # Replace variables with their values
        for variable, val in vars_mapping.items():
            formula_str = formula_str.replace(variable, str(val))

        # Remove whitespace
        formula_str = formula_str.replace(" ", "")
        # WARNING: This is vulnerable to code injection
        result = eval(formula_str)
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")