import ast

def calculate_from_input(user_input: str):
    allowed_chars = set("0123456789+-*/(). eE")
    if not all(c in allowed_chars for c in user_input):
        raise ValueError("Invalid input")
    return ast.literal_eval(user_input)