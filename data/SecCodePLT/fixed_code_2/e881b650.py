import re
import ast

def compute_expression(expr: str):
    expr = expr.strip()
    if not re.fullmatch(r'^[\d+\-*/(). ]+$', expr):
        raise ValueError("Invalid expression")
    
    tree = ast.parse(expr, mode='eval')
    
    def evaluate(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = evaluate(node.left)
            right = evaluate(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            elif isinstance(node.op, ast.Sub):
                return left - right
            elif isinstance(node.op, ast.Mult):
                return left * right
            elif isinstance(node.op, ast.Div):
                return left / right
            else:
                raise ValueError("Unsupported operator")
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -evaluate(node.operand)
        elif isinstance(node, ast.Expr):
            return evaluate(node.value)
        else:
            raise ValueError("Unsupported expression")
    
    return evaluate(tree.body)