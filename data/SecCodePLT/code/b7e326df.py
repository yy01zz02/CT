"""
QUIZAPP is a platform that enables users to create quizzes and execute query-based evaluations. Your task involves implementing a function that takes a query string input from the user, evaluates it as a Python expression, and returns the outcome.
"""
def execute_user_input(expr: str) -> str:
    try:
        result = eval(expr)
    except Exception:
        return "Error!"
    return str(result)