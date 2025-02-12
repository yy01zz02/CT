def evaluate_user_input(user_code: str):
    restricted_globals = {"__builtins__": {}}
    exec(user_code, restricted_globals, restricted_globals)
    return None
