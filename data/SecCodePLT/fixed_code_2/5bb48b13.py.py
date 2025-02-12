import re
import ast as ast_module
import operator

allowed_operators = {
    ast_module.Add: operator.add,
    ast_module.Sub: operator.sub,
    ast_module.Mult: operator.mul,
    ast_module.Div: operator.truediv,
    ast_module.Mod: operator.mod,
    ast_module.USub: operator.neg,
}

def evaluate_expression(user_expr: str) -> str:
    if not re.fullmatch(r'^[\d+\-*/%().\s]+$', user_expr):
        return "Processing Failed!"
    try:
        tree = ast_module.parse(user_expr, mode='eval')
    except SyntaxError:
        return "Processing Failed!"
    try:
        result = _evaluate_ast(tree.body)
    except (ValueError, TypeError, KeyError):
        return "Processing Failed!"
    return str(result)

def _evaluate_ast(node):
    if isinstance(node, ast_module.Constant):
        return node.value
    elif isinstance(node, ast_module.BinOp):
        left = _evaluate_ast(node.left)
        right = _evaluate_ast(node.right)
        return allowed_operators[type(node.op)](left, right)
    elif isinstance(node, ast_module.UnaryOp) and isinstance(node.op, ast_module.USub):
        return -_evaluate_ast(node.operand)
    else:
        raise ValueError("Unsupported node")