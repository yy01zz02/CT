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
    }
    tree = ast.parse(expression, mode='eval')
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.Expression, ast.Constant)):
            continue
        if isinstance(node, ast.BinOp) and type(node.op) in allowed_ops:
            continue
        if isinstance(node, ast.UnaryOp) and type(node.op) in allowed_ops:
            continue
        raise ValueError("Unsupported operation")
    
    def _evaluate(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = _evaluate(node.left)
            right = _evaluate(node.right)
            return allowed_ops[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = _evaluate(node.operand)
            return allowed_ops[type(node.op)](operand)
        elif isinstance(node, ast.Expression):
            return _evaluate(node.body)
        else:
            raise ValueError("Unexpected node during evaluation")
    
    return _evaluate(tree)
