import ast

def calculate_expression_securely(expr, var_substitute):
    try:
        for var, value in var_substitute.items():
            expr = expr.replace(var, str(value))
        expr = expr.replace(" ", "")
        
        allowed_nodes = (
            ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num,
            ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod,
            ast.Pow, ast.USub, ast.UAdd
        )
        tree = ast.parse(expr, mode='eval')
        for node in ast.walk(tree):
            if not isinstance(node, allowed_nodes):
                raise ValueError(f"Disallowed node {type(node).__name__}")

        def evaluate_node(node):
            if isinstance(node, ast.Expression):
                return evaluate_node(node.body)
            elif isinstance(node, ast.Num):
                return node.n
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
                elif isinstance(op, ast.Mod):
                    return left % right
                elif isinstance(op, ast.Pow):
                    return left ** right
                else:
                    raise ValueError("Unsupported BinOp")
            elif isinstance(node, ast.UnaryOp):
                operand = evaluate_node(node.operand)
                op = node.op
                if isinstance(op, ast.USub):
                    return -operand
                elif isinstance(op, ast.UAdd):
                    return +operand
                else:
                    raise ValueError("Unsupported UnaryOp")
            else:
                raise ValueError("Unsupported node type")

        result = evaluate_node(tree)
        return str(result)
    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")