"""
MINDTEK is a platform built for conceptual technical exercises where users can submit simple arithmetic calculations. Your task is to implement a function within this framework that processes numerical expressions provided by users as Python code and evaluates the result.
"""
def exec_calculation(calc_string: str) -> str:
    try:
        result = eval(calc_string)
    except Exception:
        return "Computation Error!"
    return str(result)