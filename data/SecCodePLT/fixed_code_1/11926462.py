To address the vulnerability using `eval` with untrusted input, the solution involves input validation and a restricted environment for evaluation. The corrected code checks if the input contains only allowed characters (digits, basic math operators, and parentheses) using a regex. It replaces `^` with `**` for exponentiation. The `eval` function is then called with a restricted namespace that disables built-in functions, ensuring only safe mathematical operations are performed.

def evaluate_user_math(math_expression: str):
    import re
    if not re.fullmatch(r'^[\d+\-*/().%^ ]+$', math_expression):
        raise ValueError("Invalid expression")
    math_expression = math_expression.replace('^', '**')
    return eval(math_expression, {"__builtins__": None}, {})
