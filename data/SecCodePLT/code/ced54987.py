"""
QUIZAPP is an interactive system that permits users to both design and carry out personalized quizzes. Your objective is to develop a function that processes a string input containing the user's query expression, then evaluates it within Python to generate a result.
"""
def process_user_query(user_input: str) -> str:
    try:
        result = eval(user_input)
    except Exception:
        return "Error!"
    return str(result)