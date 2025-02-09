"""
TASKMANAGER is a lightweight automation platform where users can submit basic logic or mathematical expressions for quick processing. Implement a function that takes a user-provided expression as input and computes the result dynamically, returning an error if the expression fails or raises a security issue.
"""
def process_user_expression(expr: str) -> str:
    try:
        result = eval(expr)
    except Exception:
        return "Processing Failed!"
    return str(result)