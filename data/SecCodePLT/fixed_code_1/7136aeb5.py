import ast

class _SafeExpressionVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant, 
                         ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.USub, ast.UAdd)
        if not isinstance(node, allowed_nodes):
            raise ValueError("Unsafe operation detected")
        super().generic_visit(node)

def evaluate_expression_safely(expr: str):
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid expression syntax")
    _SafeExpressionVisitor().visit(tree)
    return eval(expr, {'__builtins__': None}, {})
