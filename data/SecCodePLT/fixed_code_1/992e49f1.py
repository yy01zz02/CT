Here is the fixed code:

import ast

class SafeEvaluator(ast.NodeVisitor):
    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant,
                     ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod,
                     ast.Pow, ast.USub, ast.UAdd)

    def generic_visit(self, node):
        if not isinstance(node, self.allowed_nodes):
            raise ValueError("Unsafe operation detected")
        super().generic_visit(node)

def safe_execute_operation(operation: str):
    try:
        tree = ast.parse(operation.strip(), mode='eval')
    except SyntaxError:
        raise ValueError("Invalid mathematical expression")
    SafeEvaluator().visit(tree)
    return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
