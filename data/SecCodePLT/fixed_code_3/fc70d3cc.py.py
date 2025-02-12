import ast

class CodeValidator(ast.NodeVisitor):
    def visit_Import(self, node):
        raise ValueError("Imports are not allowed")
    def visit_ImportFrom(self, node):
        raise ValueError("Imports are not allowed")
    def visit_FunctionDef(self, node):
        raise ValueError("Function definitions are not allowed")
    def visit_ClassDef(self, node):
        raise ValueError("Class definitions are not allowed")

def execute_python_code(snippet_code: str):
    tree = ast.parse(snippet_code)
    CodeValidator().visit(tree)
    restricted_globals = {'__builtins__': None}
    exec(snippet_code, restricted_globals, restricted_globals)
    return None
