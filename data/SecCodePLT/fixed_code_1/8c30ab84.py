def compute_expression(expression_input: str):
    import re
    cleaned_input = re.sub(r'\s+', '', expression_input)
    if not re.fullmatch(r'^[\d+\-*/().%^]+$', cleaned_input):
        raise ValueError("Invalid expression")
    return eval(cleaned_input, {"__builtins__": None}, {})