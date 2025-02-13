To address the use of `eval` with input that has been validated by a regex and AST parsing, we can ensure that the expression is strictly a mathematical one without any function calls or unsafe operations. Here's the corrected code:

import re
import ast

def calculate_expression(ex_string: str) -> str:
    if not re.fullmatch(r'^[0-9eE+\-*/().%^ \t]*$', ex_string):
        return "Computation Error!"
    try:
        tree = ast.parse(ex_string, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute, ast.Name)):
                raise ValueError("Unsafe node")
        result = eval(compile(tree, filename='<string>', mode='eval'), {'__builtins__': None}, {})
    except Exception:
        return "Computation Error!"
    return str(result)
