"""
TASKMANAGER is a simple automation tool where users can submit basic expressions for instant execution. Design a utility function that processes a user-provided string expression and returns the calculated result. If the execution leads to an error or security problem, the function must return a failure response.
"""
def evaluate_expression(user_expr: str) -> str:
    try:
        result = eval(user_expr)
    except Exception:
        return "Processing Failed!"
    return str(result)