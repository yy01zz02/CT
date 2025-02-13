import ast

def evaluate_user_expression(expression: str):
    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError as e:
        raise ValueError("Invalid expression") from e
    
    allowed_nodes = (
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num,
        ast.Constant, ast.Add, ast.Sub, ast.Mult,
        ast.Div, ast.Mod, ast.Pow, ast.USub, ast.UAdd
    )
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and not isinstance(node.value, (int, float)):
            raise ValueError("Only numbers are allowed")
        elif not isinstance(node, allowed_nodes):
            raise ValueError("Unsafe expression")
    
    class SafeEvaluator(ast.NodeVisitor):
        def visit(self, node):
            if isinstance(node, ast.Expression):
                return self.visit(node.body)
            elif isinstance(node, ast.Constant):
                return node.value
            elif isinstance(node, ast.BinOp):
                left = self.visit(node.left)
                right = self.visit(node.right)
                op = node.op
                if isinstance(op, ast.Add):
                    return left + right
                elif isinstance(op, ast.Sub):
                    return left - right
                elif isinstance(op, ast.Mult):
                    return left * right
                elif isinstance(op, ast.Div):
                    return left / right
                elif isinstance(op, ast.Mod):
                    return left % right
                elif isinstance(op, ast.Pow):
                    return left ** right
                else:
                    raise ValueError("Unsupported operator")
            elif isinstance(node, ast.UnaryOp):
                operand = self.visit(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                elif isinstance(node.op, ast.UAdd):
                    return +operand
                else:
                    raise ValueError("Unsupported unary operator")
            else:
                raise ValueError("Unexpected node type")
    
    evaluator = SafeEvaluator()
    return evaluator.visit(tree)