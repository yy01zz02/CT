def simplify_math_expr(math_expr, var_values):
    import ast

    class SafeEvaluator(ast.NodeVisitor):
        allowed_nodes = (ast.Expression, ast.BinOp, ast.Num, ast.UnaryOp, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd)

        def generic_visit(self, node):
            if not isinstance(node, self.allowed_nodes):
                raise ValueError(f"Disallowed node type: {type(node).__name__}")
            super().generic_visit(node)

    try:
        for var, value in var_values.items():
            math_expr = math_expr.replace(var, str(value))
        math_expr = math_expr.replace(" ", "")
        parsed_expr = ast.parse(math_expr, mode='eval')
        SafeEvaluator().visit(parsed_expr)
        result = eval(compile(parsed_expr, '<string>', 'eval'), {'__builtins__': None}, {})
        return str(result)

    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")
