def simplify_math_expr(math_expr, var_values):
    import ast

    class SafeEvaluator(ast.NodeVisitor):
        allowed_nodes = (ast.Expression, ast.BinOp, ast.Num, ast.UnaryOp, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)

        def generic_visit(self, node):
            if not isinstance(node, self.allowed_nodes):
                raise ValueError(f"Disallowed node type: {type(node).__name__}")
            super().generic_visit(node)

    def evaluate_expr(node):
        if isinstance(node, ast.Expression):
            return evaluate_expr(node.body)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = evaluate_expr(node.left)
            right = evaluate_expr(node.right)
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
                raise ValueError(f"Unsupported operator: {type(op).__name__}")
        elif isinstance(node, ast.UnaryOp):
            operand = evaluate_expr(node.operand)
            op = node.op
            if isinstance(op, ast.USub):
                return -operand
            elif isinstance(op, ast.UAdd):
                return +operand
            else:
                raise ValueError(f"Unsupported unary operator: {type(op).__name__}")
        else:
            raise ValueError(f"Unsupported node type: {type(node).__name__}")

    try:
        for var, value in var_values.items():
            math_expr = math_expr.replace(var, str(value))
        math_expr = math_expr.replace(" ", "")
        parsed_expr = ast.parse(math_expr, mode='eval')
        SafeEvaluator().visit(parsed_expr)
        result = evaluate_expr(parsed_expr)
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")