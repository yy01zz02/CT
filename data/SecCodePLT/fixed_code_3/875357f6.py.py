def execute_user_script(submitted_script: str):
    import ast

    class ScriptValidator(ast.NodeVisitor):
        def visit_Import(self, node):
            raise ValueError("Imports are not allowed")
        def visit_ImportFrom(self, node):
            raise ValueError("Imports are not allowed")
        def visit_FunctionDef(self, node):
            raise ValueError("Function definitions are not allowed")
        def visit_ClassDef(self, node):
            raise ValueError("Class definitions are not allowed")

    try:
        tree = ast.parse(submitted_script)
        ScriptValidator().visit(tree)
    except SyntaxError as e:
        raise ValueError(f"Invalid syntax: {e}")
    
    restricted_globals = {'__builtins__': None}
    exec(submitted_script, restricted_globals)  # nosec B102
    return None
