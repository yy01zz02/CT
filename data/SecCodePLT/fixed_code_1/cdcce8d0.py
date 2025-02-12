def compute_expression(expr_input: str):
    import re
    if not re.fullmatch(r'^[\d+\-*/\(\)\.\s]*$', expr_input):
        raise ValueError("Invalid arithmetic expression")
    return eval(expr_input)