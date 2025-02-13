import re
import ast

def evaluate_user_math(math_expr: str) -> str:
    if not re.match(r'^[\d+\-*/()%.^ &]+$', math_expr):
        return "Processing Failed!"
    sanitized = math_expr.replace('^', '**').replace('&', '//')
    try:
        tree = ast.parse(sanitized, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute, ast.Name)):
                return "Processing Failed!"
        result = eval(compile(tree, '', 'eval'), {"__builtins__": None}, {})
        return str(result)
    except Exception:
        return "Processing Failed!"
