Here is the fixed code:

import ast
import operator

def execute_calculation_string(calc_expr, var_dict):
    try:
        allowed_operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.USub: operator.neg,
            ast.UAdd: operator.pos
        }

        for var, value in var_dict.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Invalid value for variable '{var}'. Must be a number.")
            calc_expr = calc_expr.replace(var, str(value))
        calc_expr = calc_expr.replace(" ", "")

        tree = ast.parse(calc_expr, mode='eval')

        def _check(node):
            if isinstance(node, ast.Expression):
                return _check(node.body)
            elif isinstance(node, ast.Num):
                return True
            elif isinstance(node, ast.BinOp):
                return isinstance(node.op, tuple(allowed_operators.keys())) and _check(node.left) and _check(node.right)
            elif isinstance(node, ast.UnaryOp):
                return isinstance(node.op, (ast.USub, ast.UAdd)) and _check(node.operand)
            else:
                raise ValueError(f"Disallowed operation: {node.__class__.__name__}")

        _check(tree)

        def evaluate_node(node):
            if isinstance(node, ast.Expression):
                return evaluate_node(node.body)
            elif isinstance(node, ast.Num):
                return node.n
            elif isinstance(node, ast.BinOp):
                left = evaluate_node(node.left)
                right = evaluate_node(node.right)
                return allowed_operators[type(node.op)](left, right)
            elif isinstance(node, ast.UnaryOp):
                operand = evaluate_node(node.operand)
                return allowed_operators[type(node.op)](operand)
            else:
                raise ValueError(f"Unsupported node: {type(node)}")

        result = evaluate_node(tree)
        return str(result)
    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")
