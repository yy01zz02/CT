import ast

class SafeVisitor(ast.NodeVisitor):
    allowed_nodes = {ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Num, 
                     ast.Str, ast.BoolOp, ast.Compare, ast.NameConstant}
    allowed_ops = {ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow,
                   ast.USub, ast.UAdd, ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt,
                   ast.GtE, ast.And, ast.Or}

    def visit_BoolOp(self, node):
        if type(node.op) not in self.allowed_ops:
            raise ValueError("Disallowed operator")
        self.generic_visit(node)

    def visit_Compare(self, node):
        for op in node.ops:
            if type(op) not in self.allowed_ops:
                raise ValueError("Disallowed operator")
        self.generic_visit(node)

    def visit_BinOp(self, node):
        if type(node.op) not in self.allowed_ops:
            raise ValueError("Disallowed operator")
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        if type(node.op) not in self.allowed_ops:
            raise ValueError("Disallowed operator")
        self.generic_visit(node)

    def generic_visit(self, node):
        if type(node) not in self.allowed_nodes:
            raise ValueError("Disallowed node")
        super().generic_visit(node)

def evaluate_expression_safely(input_expr: str) -> str:
    try:
        expr_ast = ast.parse(input_expr, mode='eval')
    except SyntaxError:
        return "Processing Failed!"
    
    visitor = SafeVisitor()
    try:
        visitor.visit(expr_ast)
    except ValueError:
        return "Processing Failed!"
    
    try:
        result = eval(expr_ast.body, {'__builtins__': None}, {})
    except Exception:
        return "Processing Failed!"
    return str(result)
