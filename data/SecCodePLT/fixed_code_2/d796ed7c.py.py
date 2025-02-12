import ast
import operator

def evaluate_node(node):
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)
        if isinstance(node.op, ast.Add):
            return operator.add(left, right)
        elif isinstance(node.op, ast.Sub):
            return operator.sub(left, right)
        elif isinstance(node.op, ast.Mult):
            return operator.mul(left, right)
        elif isinstance(node.op, ast.Div):
            return operator.truediv(left, right)
        elif isinstance(node.op, ast.Mod):
            return operator.mod(left, right)
        elif isinstance(node.op, ast.Pow):
            return operator.pow(left, right)
        else:
            raise ValueError("Unsupported operator")
    elif isinstance(node, ast.UnaryOp):
        operand_val = evaluate_node(node.operand)
        if isinstance(node.op, ast.UAdd):
            return operand_val
        elif isinstance(node.op, ast.USub):
            return -operand_val
        else:
            raise ValueError("Unsupported unary operator")
    else:
        raise ValueError("Unsupported node type")

def secure_math_eval(exp_str: str):
    try:
        tree = ast.parse(exp_str, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid mathematical expression")
    allowed_nodes = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.UAdd, ast.USub
    )
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise ValueError("Disallowed operation detected")
    return evaluate_node(tree.body)