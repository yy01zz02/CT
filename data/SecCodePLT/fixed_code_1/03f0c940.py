import ast

def execute_quiz_query(quiz_query: str) -> str:
    try:
        result = ast.literal_eval(quiz_query)
    except Exception:
        return "Error!"
    return str(result)
