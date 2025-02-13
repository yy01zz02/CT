def calculate_expression(expr_input: str) -> str:
    try:
        import ast
        allowed_chars = set("0123456789+-*/.%() ")
        if not all(c in allowed_chars for c in expr_input.replace(' ', '')):
            return "Computation Error!"
        tree = ast.parse(expr_input, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute, ast.Name, ast.Subscript)):
                return "Computation Error!"

        def evaluate_node(node):
            if isinstance(node, ast.Constant):
                return node.value
            elif isinstance(node, ast.BinOp):
                left = evaluate_node(node.left)
                right = evaluate_node(node.right)
                if isinstance(node.op, ast.Add):
                    return left + right
                elif isinstance(node.op, ast.Sub):
                    return left - right
                elif isinstance(node.op, ast.Mult):
                    return left * right
                elif isinstance(node.op, ast.Div):
                    return left / right
                elif isinstance(node.op, ast.Mod):
                    return left % right
                raise ValueError("Unsupported operator")
            elif isinstance(node, ast.UnaryOp):
                operand = evaluate_node(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                elif isinstance(node.op, ast.UAdd):
                    return operand
                raise ValueError("Unsupported operator")
            else:
                raise ValueError("Invalid node")

        result = evaluate_node(tree.body)
    except Exception:
        return "Computation Error!"
    return str(result)