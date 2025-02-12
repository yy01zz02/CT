import ast

def process_user_query(query: str):
    try:
        parsed = ast.parse(query, mode='eval')
        for node in ast.walk(parsed):
            if isinstance(node, ast.BinOp):
                if not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
                    raise ValueError("Invalid operator")
            elif isinstance(node, ast.UnaryOp):
                if not isinstance(node.op, (ast.UAdd, ast.USub)):
                    raise ValueError("Invalid unary operator")
            elif not isinstance(node, (ast.Expression, ast.Constant)):
                raise ValueError("Invalid node")
        result = _evaluate(parsed.body)
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError):
        raise ValueError("Invalid mathematical expression")
    return result

def _evaluate(node):
    if isinstance(node, ast.Constant):
        return node.value
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
        else:
            raise ValueError("Invalid operator")
    elif isinstance(node, ast.UnaryOp):
        operand = _evaluate(node.operand)
        op = node.op
        if isinstance(op, ast.UAdd):
            return +operand
        elif isinstance(op, ast.USub):
            return -operand
        else:
            raise ValueError("Invalid unary operator")
    else:
        raise ValueError("Unsupported node type")
