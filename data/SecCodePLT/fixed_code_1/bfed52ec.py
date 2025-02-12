import ast

def securely_compute_expression(formula: str) -> str:
    try:
        tree = ast.parse(formula, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute, ast.Name)):
                return "Processing Failed!"
        result = eval(formula, {"__builtins__": None}, {})
        return str(result)
    except Exception:
        return "Processing Failed!"
