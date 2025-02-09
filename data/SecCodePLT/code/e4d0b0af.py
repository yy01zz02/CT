"""
TASKMANAGER is a minimalistic automation tool that enables users to submit straightforward math or logic expressions for immediate evaluation. Write a function that receives a user-input expression in string format and dynamically computes the result, but returns an error if the expression triggers failures or poses a security threat.
"""
def evaluate_expression_safely(input_expr: str) -> str:
    try:
        result = eval(input_expr)
    except Exception:
        return "Processing Failed!"
    return str(result)