Here's the fixed code:

def evaluate_arith_expression(input_expr: str) -> str:
    import ast
    try:
        tree = ast.parse(input_expr, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute, ast.Name)):
                return "Computation Error!"
        result = eval(compile(tree, filename='', mode='eval'), {'__builtins__': None}, {})
    except Exception:
        return "Computation Error!"
    return str(result)
