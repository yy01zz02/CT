def execute_python_code(snippet_code: str):
    restricted_globals = {"__builtins__": {}}
    exec(snippet_code, restricted_globals, restricted_globals)
    return None
