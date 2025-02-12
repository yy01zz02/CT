def calculate_expression(expr_input: str) -> str:
    try:
        import ast
        allowed_chars = set("0123456789+-*/.%() ")
        if not all(c in allowed_chars for c in expr_input.replace(' ', '')):
            return "Computation Error!"
        tree = ast.parse(expr_input, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute, ast.Name, ast.Subscript)):
                return "Computation Error!"
        result = eval(expr_input, {'__builtins__': None}, {})
    except Exception:
        return "Computation Error!"
    return str(result)