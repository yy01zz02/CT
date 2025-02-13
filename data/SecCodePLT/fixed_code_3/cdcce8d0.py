def compute_expression(expr_input: str):
    import re
    if not re.fullmatch(r'^[\d+\-*/\(\)\.\s]*$', expr_input):
        raise ValueError("Invalid arithmetic expression")
    import ast
    try:
        tree = ast.parse(expr_input, mode='eval')
    except SyntaxError as e:
        raise ValueError("Invalid expression") from e
    for node in ast.walk(tree):
        if isinstance(node, (ast.Call, ast.Attribute, ast.Name)):
            raise ValueError("Invalid expression")
    return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
