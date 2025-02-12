import ast

def calculate_expression_securely(expr, var_substitute):
    try:
        for var, value in var_substitute.items():
            expr = expr.replace(var, str(value))
        expr = expr.replace(" ", "")
        
        allowed_nodes = (
            ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num,
            ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod,
            ast.Pow, ast.USub, ast.UAdd
        )
        tree = ast.parse(expr, mode='eval')
        for node in ast.walk(tree):
            if not isinstance(node, allowed_nodes):
                raise ValueError(f"Disallowed node {type(node).__name__}")

        result = eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
        return str(result)
    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")