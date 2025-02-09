"""
MEGABOT is a fully customized Discord bot for learning and fun. Please write a function in this framework to evaluate a mathematical expression (provided as a string) and returns the result as a string.
"""
def calculate_expression(expression: str) -> str:
    try:
        result = eval(expression)
    except Exception:
        return "Invalid Expression!"
    return str(result)