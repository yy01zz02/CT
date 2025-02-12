def execute_user_script(submitted_script: str):
    restricted_globals = {'__builtins__': None}
    exec(submitted_script, restricted_globals)
    return None
