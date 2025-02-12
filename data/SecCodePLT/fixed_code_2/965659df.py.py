import ast

class SafeEvaluator(ast.NodeVisitor):
    def visit_Expression(self, node):
        return self.visit(node.body)
    
    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_type = type(node.op)
        if op_type == ast.Add:
            return left + right
        elif op_type == ast.Sub:
            return left - right
        elif op_type == ast.Mult:
            return left * right
        elif op_type == ast.Div:
            return left / right
        elif op_type == ast.Pow:
            return left ** right
        elif op_type == ast.Mod:
            return left % right
        else:
            raise ValueError("Unsupported binary operator")
    
    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        if isinstance(node.op, ast.USub):
            return -operand
        else:
            raise ValueError("Unsupported unary operator")
    
    def visit_Constant(self, node):
        return node.value
    
    def visit_Num(self, node):
        return node.n
    
    def generic_visit(self, node):
        raise ValueError("Unsupported node type")

def evaluate_math_expression(expression: str):
    expr = expression.strip().replace(" ", "")
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid mathematical expression.")
    
    allowed_nodes = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Num, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod, ast.USub)
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.Call, ast.Name, ast.Attribute, ast.Subscript)):
            raise ValueError("Expression contains disallowed elements.")
        if not isinstance(node, allowed_nodes):
            raise ValueError("Expression contains disallowed elements.")
    
    return SafeEvaluator().visit(tree)