To address the security vulnerability caused by using `eval`, we replace it with `ast.literal_eval`, which safely evaluates Python literals. This restricts the input to literals (like numbers, lists, dicts) and prevents arbitrary code execution. If the user input is a mathematical expression, it will now correctly return a failure, enhancing security.

import ast

def execute_user_input(user_input: str) -> str:
    try:
        result = ast.literal_eval(user_input)
    except Exception:
        return "Processing Failed!"
    return str(result)
