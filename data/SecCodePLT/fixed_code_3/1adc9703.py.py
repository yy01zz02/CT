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

    class SafeEvaluator(ast.NodeVisitor):
        def visit_Expression(self, node):
            return self.visit(node.body)
        def visit_BinOp(self, node):
            left = self.visit(node.left)
            right = self.visit(node.right)
            op = type(node.op)
            if op == ast.Add: return left + right
            elif op == ast.Sub: return left - right
            elif op == ast.Mult: return left * right
            elif op == ast.Div: return left / right
            elif op == ast.Mod: return left % right
            elif op == ast.Pow: return left ** right
            else: raise ValueError("Disallowed operator")
        def visit_UnaryOp(self, node):
            operand = self.visit(node.operand)
            if isinstance(node.op, ast.USub): return -operand
            else: raise ValueError("Disallowed unary operator")
        def visit_Constant(self, node):
            return node.value
        def visit_Num(self, node):
            return node.n

    try:
        tree = ast.parse(expr, mode='eval')
        SafeVisitor().visit(tree)
        result = SafeEvaluator().visit(tree)
    except Exception:
        return "Processing Failed!"
    return str(result)
