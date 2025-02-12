def evaluate_code_string(code_string: str):
    import ast

    class SecurityVisitor(ast.NodeVisitor):
        def visit_Import(self, node):
            raise ValueError("Imports are not allowed")
        
        def visit_ImportFrom(self, node):
            raise ValueError("Imports are not allowed")
        
        def visit_FunctionDef(self, node):
            raise ValueError("Function definitions are not allowed")
        
        def visit_ClassDef(self, node):
            raise ValueError("Class definitions are not allowed")
        
        def visit_Call(self, node):
            if isinstance(node.func, ast.Name) and node.func.id in {'exec', 'eval', 'open', 'globals', 'locals'}:
                raise ValueError(f"Disallowed function call: {node.func.id}")
            self.generic_visit(node)

    parsed = ast.parse(code_string)
    SecurityVisitor().visit(parsed)
    
    restricted_globals = {'__builtins__': {}}
    exec(code_string, restricted_globals, restricted_globals)
    return None
