def run_python_snippet(snippet_string: str):
    restricted_globals = {"__builtins__": {}}
    exec(snippet_string, restricted_globals, restricted_globals)
    return None
