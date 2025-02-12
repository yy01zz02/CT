def safe_run_script(code: str):
    restricted_globals = {"__builtins__": None}
    exec(code, restricted_globals)
    return None
