To mitigate the security risks associated with using `eval`, the code is modified by restricting the evaluation environment. By removing access to built-in functions and variables, arbitrary code execution is prevented while still allowing the evaluation of basic mathematical expressions.

def compute_expression(input_expr: str):
    result = eval(input_expr, {'__builtins__': None}, {})
    return result
