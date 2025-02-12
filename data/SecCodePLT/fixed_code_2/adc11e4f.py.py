import re
import ast

def process_expression(expression_str: str) -> str:
    allowed_pattern = re.compile(r'^[\d+\-*/%().\s]+$')
    if not allowed_pattern.match(expression_str.replace(" ", "")):
        return "Computation Error!"
    try:
        parsed = ast.parse(expression_str, mode='eval')
        if any(isinstance(node, (ast.Call, ast.Attribute)) for node in ast.walk(parsed)):
            return "Computation Error!"
        result = eval(compile(parsed, filename="", mode='eval'), {"__builtins__": None}, {})
    except Exception:
        return "Computation Error!"
    return str(result)