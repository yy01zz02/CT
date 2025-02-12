def run_python_snippet(python_snippet: str):
    import ast

    class CodeValidator(ast.NodeVisitor):
        def visit_Import(self, node):
            raise ValueError("Imports are not allowed.")
        def visit_ImportFrom(self, node):
            raise ValueError("Imports are not allowed.")
        def visit_FunctionDef(self, node):
            raise ValueError("Function definitions are not allowed.")
        def visit_ClassDef(self, node):
            raise ValueError("Class definitions are not allowed.")
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name) and node.func.id in ['eval', 'exec', 'open', '__import__']:
                raise ValueError(f"Call to {node.func.id} is not allowed.")

    try:
        tree = ast.parse(python_snippet)
    except SyntaxError:
        raise ValueError("Invalid Python syntax.")

    validator = CodeValidator()
    validator.visit(tree)

    allowed_builtins = {'abs': abs, 'max': max, 'min': min, 'sum': sum, 'len': len, 'print': print}
    restricted_globals = {'__builtins__': allowed_builtins}

    exec(python_snippet, restricted_globals)  # nosec B102
    return None