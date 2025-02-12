import ast

def secure_eval_expression(exp: str):
    return ast.literal_eval(exp)
