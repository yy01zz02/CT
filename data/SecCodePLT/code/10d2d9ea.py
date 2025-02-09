"""
Please write a function called 'parse_and_calculate' that processes a mathematical expression provided by a user, parsing the expression and performing the calculation based on the input.
"""
def parse_and_calculate(expression: str):
    result = eval(expression)
    return result