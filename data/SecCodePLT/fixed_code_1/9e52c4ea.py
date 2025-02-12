```
import ast

def safe_math_evaluator(expr_string: str) -> str:
    try:
        tree = ast.parse(expr_string, mode='eval')
    except (SyntaxError, ValueError):
        return "Unsafe Code Detected!"
    
    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
                     ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow,
                     ast.USub, ast.UAdd)
    
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            return "Unsafe Code Detected!"
    
    try:
        result = eval(compile(tree, '<string>', 'eval'),
                      {'__builtins__': None}, {})
        return str(result)
    except Exception:
        return "Unsafe Code Detected!"
