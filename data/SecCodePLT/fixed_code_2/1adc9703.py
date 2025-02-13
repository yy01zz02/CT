def process_user_expression(expr: str) -> str:
    import ast

    class SafeVisitor(ast.NodeVisitor):
        def __init__(self):
            self.allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num,
                            ast.Constant, ast.Add, ast.Sub, ast.Mult, ast.Div,
                            ast.Mod, ast.Pow, ast.USub)
        def generic_visit(self, node):
            if not isinstance(node, self.allowed):
                raise ValueError("Disallowed node")
            super().generic_visit(node)

    try:
        tree = ast.parse(expr, mode='eval')
        SafeVisitor().visit(tree)
        result = eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
    except Exception:
        return "Processing Failed!"
    return str(result)
