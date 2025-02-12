import ast

def evaluate_expression(expression: str):
    try:
        code = compile(expression, '<string>', 'eval')
    except SyntaxError as e:
        raise ValueError(f"Invalid expression syntax: {e}") from e
    if code.co_names:
        raise ValueError("Expression contains disallowed variables or function calls")
    return eval(code, {'__builtins__': None}, {})
