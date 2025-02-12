import ast
import operator

def perform_safe_math(expression: str):
    allowed_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.BinOp: ast.BinOp
    }
    tree = ast.parse(expression, mode='eval')
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Expression, ast.Constant, ast.UnaryOp, ast.BinOp, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)):
            raise ValueError("Unsupported operation")
    return eval(compile(tree, filename="<string>", mode="eval"), {'__builtins__': None}, allowed_ops)
