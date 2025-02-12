import ast

def evaluate_quiz_expression(quiz_expr: str) -> str:
    try:
        result = ast.literal_eval(quiz_expr)
    except Exception:
        return "Error!"
    return str(result)
