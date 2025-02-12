def evaluate_expression(expr_string: str) -> str:
    try:
        result = eval(expr_string, {"__builtins__": None}, {})
    except Exception:
        return "Computation Error!"
    return str(result)
