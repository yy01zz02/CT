To fix the code vulnerability from using `eval`, the solution employs Abstract Syntax Tree (AST) validation to ensure only safe mathematical expressions are evaluated. It restricts operations to basic arithmetic and checks nodes for validity before evaluation.

import ast
import operator

class MathExpressionValidator(ast.NodeVisitor):
    allowed_operators = {
        ast.Add: operator.add, ast.Sub: operator.sub,
        ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Pow: operator.pow, ast.Mod: operator.mod,
        ast.USub: operator.neg
    }

    def visit_BinOp(self, node):
        if type(node.op) not in self.allowed_operators:
            raise ValueError("Disallowed operator")
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryOp(self, node):
        if type(node.op) not in self.allowed_operators:
            raise ValueError("Disallowed unary operator")
        self.visit(node.operand)

    def visit_Constant(self, node):
        if not isinstance(node.value, (int, float)):
            raise ValueError("Invalid constant type")

    def generic_visit(self, node):
        if not isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant)):
            raise ValueError("Disallowed node type")

def secure_math_eval(expr_str: str):
    try:
        tree = ast.parse(expr_str, mode='eval')
    except SyntaxError as e:
        raise ValueError("Invalid syntax") from e

    validator = MathExpressionValidator()
    try:
        validator.visit(tree)
    except ValueError as e:
        raise ValueError("Unsafe expression") from e

    return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
