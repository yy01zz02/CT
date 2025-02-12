Here is the fixed code:

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
            "__import__": None
        }
    }

    def safe_import(name, *args, **kwargs):
        allowed_modules = ["math"]
        if name in allowed_modules:
            return __import__(name, *args, **kwargs)
        raise ImportError(f"Import of {name} is not allowed")

    safe_globals["__builtins__"]["__import__"] = safe_import

    import ast

    try:
        tree = ast.parse(submitted_code)
    except SyntaxError as e:
        raise ValueError("Invalid syntax in submitted code") from e

    forbidden_nodes = (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef, ast.Lambda, ast.AsyncFunctionDef)
    for node in ast.walk(tree):
        if isinstance(node, forbidden_nodes):
            raise ValueError(f"Forbidden code element: {type(node).__name__}")

    exec(submitted_code, safe_globals)
    return None
