def process_python_code(code_str: str):
    exec(code_str, {"__builtins__": None}, {})
    return None
