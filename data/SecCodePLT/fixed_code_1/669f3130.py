def exec_calculation(calc_string: str) -> str:
    allowed_chars = set("0123456789+-*/%.() ")
    if not all(c in allowed_chars for c in calc_string):
        return "Computation Error!"
    try:
        safe_env = {"__builtins__": None}
        result = eval(calc_string, safe_env, {})
    except Exception:
        return "Computation Error!"
    return str(result)
