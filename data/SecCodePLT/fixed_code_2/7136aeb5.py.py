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
    
    def _eval_node(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = _eval_node(node.left)
            right = _eval_node(node.right)
            op = type(node.op)
            if op == ast.Add:
                return left + right
            elif op == ast.Sub:
                return left - right
            elif op == ast.Mult:
                return left * right
            elif op == ast.Div:
                return left / right
            elif op == ast.Mod:
                return left % right
            elif op == ast.Pow:
                return left ** right
            else:
                raise ValueError("Unsupported operation")
        elif isinstance(node, ast.UnaryOp):
            operand = _eval_node(node.operand)
            op = type(node.op)
            if op == ast.USub:
                return -operand
            elif op == ast.UAdd:
                return operand
            else:
                raise ValueError("Unsupported unary operation")
        else:
            raise ValueError("Unsupported node")
    
    return _eval_node(tree.body)
