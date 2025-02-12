Here is the fixed code:

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
    
    class Evaluator(ast.NodeVisitor):
        def visit(self, node):
            return super().visit(node)
        
        def visit_Expression(self, node):
            return self.visit(node.body)
        
        def visit_Constant(self, node):
            return node.value
        
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
            elif isinstance(op, ast.Pow):
                return left ** right
            elif isinstance(op, ast.Mod):
                return left % right
            else:
                raise ValueError("Unsupported operator")
        
        def visit_UnaryOp(self, node):
            operand = self.visit(node.operand)
            op = node.op
            if isinstance(op, ast.UAdd):
                return +operand
            elif isinstance(op, ast.USub):
                return -operand
            else:
                raise ValueError("Unsupported unary operator")
    
    evaluator = Evaluator()
    return evaluator.visit(tree)
