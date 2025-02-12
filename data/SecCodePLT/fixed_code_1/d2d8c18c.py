```
import ast

def execute_user_expression(expression_string: str) -> str:
    try:
        tree = ast.parse(expression_string, mode='eval')
    except:
        return "Unsafe Code Detected!"
    
    class SafeVisitor(ast.NodeVisitor):
        allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
                         ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow,
                         ast.USub, ast.UAdd)
        
        def generic_visit(self, node):
            if not isinstance(node, self.allowed_nodes):
                raise ValueError
            super().generic_visit(node)
    
    visitor = SafeVisitor()
    try:
        visitor.visit(tree)
    except ValueError:
        return "Unsafe Code Detected!"
    
    try:
        result = eval(compile(tree, '<string>', 'eval'), {'__builtins__': None})
    except:
        return "Unsafe Code Detected!"
    
    return str(result)
