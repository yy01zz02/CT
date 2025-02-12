import ast

def safe_eval_expression(expr: str):
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError as e:
        raise ValueError(f"Invalid expression") from None
    
    allowed_nodes = (
        ast.Expression, ast.BinOp, ast.UnaryOp,
        ast.Constant, ast.Add, ast.Sub, ast.Mult,
        ast.Div, ast.Pow, ast.Mod, ast.USub, ast.UAdd
    )
    
    class Checker(ast.NodeVisitor):
        def generic_visit(self, node):
            if not isinstance(node, allowed_nodes):
                raise ValueError("Unsafe expression")
            super().generic_visit(node)
    
    Checker().visit(tree)
    
    return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
