import re
import ast

def calculate_expression(expression: str) -> str:
    if not re.fullmatch(r'^[\d+\-*/().^ \s]+$', expression):
        return "Invalid Expression!"
    try:
        node = ast.parse(expression.strip(), mode='eval')
        result = _evaluate(node.body)
        return str(result)
    except:
        return "Invalid Expression!"

def _evaluate(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        left = _evaluate(node.left)
        right = _evaluate(node.right)
        op = node.op
        if isinstance(op, ast.Add):
            return left + right
        elif isinstance(op, ast.Sub):
            return left - right
        elif isinstance(op, ast.Mult):
            return left * right
        elif isinstance(op, ast.Div):
            return left / right
        elif isinstance(op, ast.Pow):
            return left ** right
        else:
            raise ValueError("Unsupported operator")
    elif isinstance(node, ast.UnaryOp):
        operand = _evaluate(node.operand)
        if isinstance(node.op, ast.USub):
            return -operand
        elif isinstance(node.op, ast.UAdd):
            return operand
        else:
            raise ValueError("Unsupported unary operator")
    else:
        raise ValueError("Unsupported node type")
