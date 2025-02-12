Here's the fixed code:

def run_user_script(user_script: str):
    restricted_globals = {"__builtins__": None}
    allowed_builtins = {"print", "range", "len"}
    restricted_globals["__builtins__"] = {name: __builtins__[name] for name in allowed_builtins}
    exec(user_script, restricted_globals)
    return None
