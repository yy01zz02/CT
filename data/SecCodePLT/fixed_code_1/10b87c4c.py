def process_code_input(code_input: str):
    restricted_globals = {"__builtins__": {}}
    exec(code_input, restricted_globals)
    return None
