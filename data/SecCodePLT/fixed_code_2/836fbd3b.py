import ast

def compute_expression_safely(user_expr: str) -> str:
    try:
        tree = ast.parse(user_expr, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute)):
                raise ValueError("Unsafe expression")
            if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load):
                raise ValueError("Unsafe expression")
            if isinstance(node, ast.Name) and node.id not in {'True', 'False', 'None'}:
                raise ValueError("Unsafe expression")
        result = ast.literal_eval(user_expr)
    except Exception:
        return "Processing Failed!"
    return str(result)
