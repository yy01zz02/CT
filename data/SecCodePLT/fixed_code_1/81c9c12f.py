import math

def math_expression_safety_check(math_input: str) -> str:
    try:
        safe_env = {"__builtins__": None}
        for name in dir(math):
            if not name.startswith('_'):
                safe_env[name] = getattr(math, name)
        result = eval(math_input, safe_env)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)
