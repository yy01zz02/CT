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

class SafeEvaluator(ast.NodeVisitor):
    def visit(self, node):
        if isinstance(node, ast.Expression):
            return self.visit(node.body)
        return super().visit(node)
    
    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right
        elif isinstance(node.op, ast.Pow):
            return left ** right
        else:
            raise ValueError("Invalid operator")

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        elif isinstance(node.op, ast.USub):
            return -operand
        else:
            raise ValueError("Invalid unary operator")

    def visit_Num(self, node):
        return node.n

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise ValueError("Disallowed constant type")

def evaluate_expression(expr: str):
    if not re.fullmatch(r'^[\s\d+\-*/()eE.]*$', expr):
        raise ValueError("Invalid expression")
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid syntax")
    SecurityVisitor().visit(tree)
    return SafeEvaluator().visit(tree)