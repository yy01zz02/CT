def execute_user_code(submitted_code: str):
    safe_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "bool": bool,
            "int": int,
            "float": float,
            "str": str,
            "list": list,
            "dict": dict,
            "tuple": tuple,
            "set": set,
            "len": len,
            "sum": sum,
            "min": min,
            "max": max,
            "abs": abs,
            "round": round,
            "__import__": __import__  # Override to allow imports
        }
    }

    def safe_import(name, *args, **kwargs):
        allowed_modules = ["math"]
        if name in allowed_modules:
            return __import__(name, *args, **kwargs)
        raise ImportError(f"Import of {name} is not allowed")

    safe_globals["__builtins__"]["__import__"] = safe_import

    exec(submitted_code, safe_globals)
    return None
