def process_user_code(code_submission: str):
    restricted_globals = {"__builtins__": None}
    exec(code_submission, restricted_globals, restricted_globals)
    return None
