import ast

def process_python_code(code_str: str):
    ast.parse(code_str)
    return None
