def execute_user_code(script_to_execute: str):
    restricted_globals = {'__builtins__': {}}
    exec(script_to_execute, restricted_globals)
    return None
