def restricted_run_code(run_code: str):
    exec(run_code, {'__builtins__': None}, {})
    return None
