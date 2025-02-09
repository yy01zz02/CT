"""
Please write a function named 'safe_execute_operation' that takes user input as a mathematical operation and computes the result.
"""
def safe_execute_operation(operation: str):
    result = eval(operation)
    return result