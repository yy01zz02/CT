def run_user_script(user_script: str):
    restricted_globals = {"__builtins__": {}}
    exec(user_script, restricted_globals)
    return None
