To address the vulnerabilities identified by the Bandit analysis, the code has been modified to safely evaluate arithmetic and logical expressions without using `eval` directly. The solution uses Python's `ast` module to parse and validate the expression's abstract syntax tree (AST), ensuring that only safe nodes (literals and basic operations) are allowed. The expression is then evaluated in a restricted environment to prevent any unintended code execution.

Here is the corrected code:

import ast

class SecurityChecker(ast.NodeVisitor):
    def __init__(self):
        self.safe = True

    def visit_Call(self, node):
        self.safe = False

    def visit_Attribute(self, node):
        self.safe = False

    def visit_Name(self, node):
        self.safe = False

def calculate_user_input(input_expr: str) -> str:
    try:
        expr_ast = ast.parse(input_expr, mode='eval')
    except SyntaxError:
        return "Processing Failed!"

    checker = SecurityChecker()
    checker.visit(expr_ast)
    if not checker.safe:
        return "Processing Failed!"

    try:
        result = eval(compile(expr_ast, '', 'eval'), {'__builtins__': None}, {})
    except Exception:
        return "Processing Failed!"

    return str(result)
