import ast

def run_code_snippet(user_code: str):
    tree = ast.parse(user_code, mode='exec')
    
    class SafetyVisitor(ast.NodeVisitor):
        def visit_Import(self, node):
            raise ValueError("Imports are not allowed.")
        def visit_ImportFrom(self, node):
            raise ValueError("Imports are not allowed.")
        def visit_Call(self, node):
            raise ValueError("Function calls are not allowed.")
        def visit_FunctionDef(self, node):
            raise ValueError("Function definitions are not allowed.")
        def visit_ClassDef(self, node):
            raise ValueError("Class definitions are not allowed.")
        def visit_For(self, node):
            raise ValueError("Loops are not allowed.")
        def visit_While(self, node):
            raise ValueError("Loops are not allowed.")
        def visit_Attribute(self, node):
            raise ValueError("Attribute access is not allowed.")

    visitor = SafetyVisitor()
    visitor.visit(tree)
    
    restricted_globals = {'__builtins__': {}}
    exec(user_code, restricted_globals)  # nosec B102
    return None