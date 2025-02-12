def compute_expression(expression_input: str):
    import re
    import ast

    cleaned_input = re.sub(r'\s+', '', expression_input)
    if not re.fullmatch(r'^[\d+\-*/().%^]+$', cleaned_input):
        raise ValueError("Invalid expression")
    
    class SafeEvaluator(ast.NodeVisitor):
        def visit_BinOp(self, node):
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
        
        def visit_UnaryOp(self, node):
            operand = self.visit(node.operand)
            if isinstance(node.op, ast.USub):
                return -operand
            else:
                raise ValueError("Unsupported unary operator")
        
        def visit_Constant(self, node):
            return node.value
        
        def generic_visit(self, node):
            raise ValueError("Unsupported node type")
    
    try:
        tree = ast.parse(cleaned_input, mode='eval')
        evaluator = SafeEvaluator()
        return evaluator.visit(tree.body)
    except:
        raise ValueError("Invalid expression")