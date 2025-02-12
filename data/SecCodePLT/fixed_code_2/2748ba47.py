def execute_user_code(script_to_execute: str):
    import ast

    class SafeCodeChecker(ast.NodeVisitor):
        def visit_Import(self, node):
            raise ValueError("Imports are not allowed.")
        def visit_ImportFrom(self, node):
            raise ValueError("Imports are not allowed.")
        def visit_FunctionDef(self, node):
            raise ValueError("Function definitions are not allowed.")
        def visit_ClassDef(self, node):
            raise ValueError("Class definitions are not allowed.")
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                if node.func.id in ['eval', 'exec', 'open']:
                    raise ValueError(f"Dangerous function call: {node.func.id}")
            self.generic_visit(node)

    tree = ast.parse(script_to_execute)
    SafeCodeChecker().visit(tree)
    restricted_globals = {'__builtins__': {}}
    exec(script_to_execute, restricted_globals)
    return None
