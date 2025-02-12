To fix the vulnerabilities identified by Bandit, the use of `eval` should be replaced with a safer approach, such as `ast.literal_eval`. However, given that the original code needs to evaluate arithmetic and string expressions, we instead use `ast.parse` to validate the input and then evaluate it in a restricted environment. This ensures only allowed operations are executed, preventing arbitrary code execution while supporting the intended functionality.

import ast

def process_user_script(code_str: str) -> str:
    try:
        tree = ast.parse(code_str, mode='eval')
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Expression, ast.Constant, ast.UnaryOp, ast.BinOp,
                                     ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.USub, ast.UAdd)):
                return "Execution Blocked!"
        result = eval(compile(tree, '', 'eval'), {"__builtins__": None}, {})
    except Exception:
        return "Execution Blocked!"
    return str(result)
