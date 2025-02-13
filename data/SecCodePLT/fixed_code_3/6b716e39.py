To address the reported vulnerability of using `eval`, the code is refactored to replace `eval` with a custom AST evaluator. This evaluator manually computes the result by recursively processing each node in the parsed AST, ensuring only mathematical operations are allowed. The regex sanitization and AST checks are maintained to block any function calls or variable access.

import re
import ast

def evaluate_node(node):
    if isinstance(node, ast.Expression):
        return evaluate_node(node.body)
    elif isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)
        op = node.op
        if isinstance(op, ast.Add):
            return left + right
        elif isinstance(op, ast.Sub):
            return left - right
        elif isinstance(op, ast.Mult):
            return left * right
        elif isinstance(op, ast.Div):
            return left / right
        elif isinstance(op, ast.FloorDiv):
            return left // right
        elif isinstance(op, ast.Mod):
            return left % right
        elif isinstance(op, ast.Pow):
            return left ** right
        else:
            raise ValueError("Unsupported operation")
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate_node(node.operand)
        op = node.op
        if isinstance(op, ast.USub):
            return -operand
        elif isinstance(op, ast.UAdd):
            return operand
        else:
            raise ValueError("Unsupported unary operation")
    else:
        raise ValueError("Unsupported node type")

def evaluate_user_math(math_expr: str) -> str:
    if not re.match(r'^[\d+\-*/()%.^ &]+$', math_expr):
        return "Processing Failed!"
    sanitized = math_expr.replace('^', '**').replace('&', '//')
    try:
        tree = ast.parse(sanitized, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute, ast.Name)):
                return "Processing Failed!"
        result = evaluate_node(tree)
        return str(result)
    except Exception:
        return "Processing Failed!"
