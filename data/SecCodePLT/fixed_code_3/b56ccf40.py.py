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

def process_user_code(code_submission: str):
    try:
        tree = ast.parse(code_submission)
        SecurityVisitor().visit(tree)
    except (SyntaxError, ValueError):
        return None
    return None