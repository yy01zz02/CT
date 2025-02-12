def evaluate_expression_safely(expression: str) -> str:
    import ast
    
    class SafeVisitor(ast.NodeVisitor):
        def generic_visit(self, node):
            allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant,
                       ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd)
            if not isinstance(node, allowed):
                raise ValueError("Unsafe node detected")
            super().generic_visit(node)
    
    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError:
        return "Unsafe Code Detected!"
    
    visitor = SafeVisitor()
    try:
        visitor.visit(tree)
    except ValueError:
        return "Unsafe Code Detected!"
    
    try:
        result = eval(expression, {'__builtins__': None}, {})
    except Exception:
        return "Unsafe Code Detected!"
    
    return str(result)