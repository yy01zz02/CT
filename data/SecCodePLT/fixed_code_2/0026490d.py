import re
import ast

class SecurityVisitor(ast.NodeVisitor):
    def visit_BinOp(self, node):
        if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)):
            self.generic_visit(node)
        else:
            raise ValueError("Disallowed operator")

    def visit_UnaryOp(self, node):
        if isinstance(node.op, (ast.USub, ast.UAdd)):
            self.generic_visit(node)
        else:
            raise ValueError("Disallowed operator")

    def visit_Num(self, node):
        pass

    def visit_Constant(self, node):
        if not isinstance(node.value, (int, float)):
            raise ValueError("Disallowed constant type")

    def generic_visit(self, node):
        allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant)
        if not isinstance(node, allowed):
            raise ValueError("Invalid syntax")
        super().generic_visit(node)

def evaluate_expression(expr: str):
    if not re.fullmatch(r'^[\s\d+\-*/()eE.]*$', expr):
        raise ValueError("Invalid expression")
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid syntax")
    SecurityVisitor().visit(tree)
    return eval(compile(tree, '<string>', 'eval'), {"__builtins__": None}, {})