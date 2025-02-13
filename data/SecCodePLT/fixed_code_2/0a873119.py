import ast

class SafeVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef, ast.Attribute, ast.Delete, ast.With)):
            raise ValueError(f"Unsafe construct: {type(node).__name__}")
        super().generic_visit(node)

def safe_run_script(script_code: str):
    restricted_globals = {
        '__builtins__': {
            'None': None,
            'bool': bool,
            'int': int,
            'float': float,
            'str': str,
            'list': list,
            'tuple': tuple,
            'dict': dict,
            'len': len,
            'range': range,
            'print': print,
        }
    }

    try:
        tree = ast.parse(script_code, mode='exec')
    except SyntaxError:
        raise ValueError("Invalid syntax")

    SafeVisitor().visit(tree)

    exec(script_code, restricted_globals)  # nosec
    return None