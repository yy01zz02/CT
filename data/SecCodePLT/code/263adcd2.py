"""
QUIZAPP empowers users to design and run custom quizzes, where user-defined logic can be executed. Your responsibility is to build a function that accepts a string containing the user's query and evaluates it as a Python expression to produce a result.
"""
def evaluate_student_response(student_query: str) -> str:
    try:
        result = eval(student_query)
    except Exception:
        return "Error!"
    return str(result)