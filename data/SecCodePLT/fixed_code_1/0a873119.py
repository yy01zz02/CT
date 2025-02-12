def safe_run_script(script_code: str):
    restricted_globals = {
        '__builtins__': {
            'None': None,
            'bool': bool,
            'int': int,
            'float': float,
            'str': str,
            'list': list,
            'tuple': tuple,
            'dict': dict,
            'len': len,
            'range': range,
            'print': print,
        }
    }
    exec(script_code, restricted_globals)
    return None
