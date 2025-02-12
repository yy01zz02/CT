import ast

def evaluate_user_input(user_code: str):
    return ast.literal_eval(user_code)
