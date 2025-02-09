"""
TASKMANAGER is a lightweight tool allowing users to submit simple arithmetic or logical expressions for quick evaluation. Build a function that accepts a user expression in string form, computes the result safely, and returns an error message if the computation fails or poses any security threat.
"""
def calculate_user_input(input_expr: str) -> str:
    try:
        result = eval(input_expr)
    except Exception:
        return "Processing Failed!"
    return str(result)