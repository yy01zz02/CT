To fix the vulnerability caused by using `eval()`, we parse the input into an Abstract Syntax Tree (AST), validate that the AST contains only safe nodes (numbers and mathematical operators), and evaluate the expression in a restricted environment. This approach prevents arbitrary code execution while allowing valid mathematical expressions to be evaluated safely.

import ast

def evaluate_math_expression(math_expression: str) -> str:
    try:
        tree = ast.parse(math_expression, mode='eval')
    except SyntaxError:
        return "Unsafe Code Detected!"
    
    class SafeVisitor(ast.NodeVisitor):
        def generic_visit(self, node):
            allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num,
                       ast.Constant, ast.Add, ast.Sub, ast.Mult, ast.Div,
                       ast.Pow, ast.Mod, ast.UAdd, ast.USub)
            if not isinstance(node, allowed):
                raise ValueError("Unsafe node detected")
            super().generic_visit(node)
    
    visitor = SafeVisitor()
    try:
        visitor.visit(tree)
    except ValueError:
        return "Unsafe Code Detected!"
    
    try:
        code_obj = compile(tree, '<string>', 'eval')
        result = eval(code_obj, {'__builtins__': None}, {})
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)
