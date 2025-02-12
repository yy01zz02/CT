import ast

def evaluate_expression(expression: str):
    try:
        return ast.literal_eval(expression)
    except (SyntaxError, ValueError) as e:
        raise ValueError(f"Invalid expression: {e}") from e
