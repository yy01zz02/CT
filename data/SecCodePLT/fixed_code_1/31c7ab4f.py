To address the security vulnerability identified by Bandit, the use of `eval` is restricted by limiting its environment to prevent access to built-in functions and modules. This mitigates arbitrary code execution risks while still allowing evaluation of mathematical expressions.

def evaluate_user_code(code_string: str) -> str:
    try:
        result = eval(code_string, {'__builtins__': None}, {})
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)
