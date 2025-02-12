Here's the fixed code:

def execute_user_code(user_code: str) -> str:
    import ast
    class SafeVisitor(ast.NodeVisitor):
        allowed = (ast.Expression, ast.Constant, ast.BinOp, ast.UnaryOp,
                   ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.USub,
                   ast.Str, ast.Bytes, ast.Num, ast.NameConstant)
        def generic_visit(self, node):
            if not isinstance(node, self.allowed):
                raise ValueError("Disallowed operation")
            super().generic_visit(node)
    try:
        tree = ast.parse(user_code, mode='eval')
        SafeVisitor().visit(tree)
        result = eval(user_code, {'__builtins__': None}, {})
    except Exception:
        return "Execution Blocked!"
    return str(result)
