import ast
import operator

def parse_and_calculate(expression: str):
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
    }

    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            op_type = type(node.op)
            if op_type not in allowed_operators:
                raise ValueError(f"Operation {op_type} not allowed")
            return allowed_operators[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            op_type = type(node.op)
            if op_type not in allowed_operators:
                raise ValueError(f"Operation {op_type} not allowed")
            return allowed_operators[op_type](operand)
        else:
            raise ValueError(f"Unsupported node type: {type(node)}")

    try:
        tree = ast.parse(expression, mode='eval')
        result = eval_node(tree.body)
        return result
    except (SyntaxError, ValueError, TypeError) as e:
        raise ValueError("Invalid mathematical expression") from e