import ast

def evaluate_student_response(student_query: str) -> str:
    try:
        result = ast.literal_eval(student_query)
    except Exception:
        return "Error!"
    return str(result)