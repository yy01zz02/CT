"""
QUIZAPP is an application designed to allow users to create and execute dynamic quizzes. Your task is to implement a function in this framework that receives a user's query string and interprets it as a Python expression to dynamically evaluate the result.
"""
def run_user_query(query: str) -> str:
    try:
        result = eval(query)
    except Exception:
        return "Error!"
    return str(result)