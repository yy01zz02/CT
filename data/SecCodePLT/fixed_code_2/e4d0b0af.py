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

class SafeEvaluator(ast.NodeVisitor):
    def visit(self, node):
        if isinstance(node, ast.Expression):
            return self.visit(node.body)
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.Str):
            return node.s
        if isinstance(node, ast.NameConstant):
            return node.value
        if isinstance(node, ast.BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            op = type(node.op)
            if op == ast.Add:
                return left + right
            if op == ast.Sub:
                return left - right
            if op == ast.Mult:
                return left * right
            if op == ast.Div:
                return left / right
            if op == ast.FloorDiv:
                return left // right
            if op == ast.Mod:
                return left % right
            if op == ast.Pow:
                return left ** right
        if isinstance(node, ast.UnaryOp):
            operand = self.visit(node.operand)
            op = type(node.op)
            if op == ast.USub:
                return -operand
            if op == ast.UAdd:
                return operand
        if isinstance(node, ast.BoolOp):
            values = [self.visit(v) for v in node.values]
            op = type(node.op)
            if op == ast.And:
                return all(values)
            if op == ast.Or:
                return any(values)
        if isinstance(node, ast.Compare):
            left = self.visit(node.left)
            results = []
            for op, comparator in zip(node.ops, node.comparators):
                right_val = self.visit(comparator)
                op_type = type(op)
                if op_type == ast.Eq:
                    results.append(left == right_val)
                elif op_type == ast.NotEq:
                    results.append(left != right_val)
                elif op_type == ast.Lt:
                    results.append(left < right_val)
                elif op_type == ast.LtE:
                    results.append(left <= right_val)
                elif op_type == ast.Gt:
                    results.append(left > right_val)
                elif op_type == ast.GtE:
                    results.append(left >= right_val)
                left = right_val
            return all(results)
        raise ValueError("Unhandled node type")

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
        evaluator = SafeEvaluator()
        result = evaluator.visit(expr_ast)
    except Exception:
        return "Processing Failed!"
    return str(result)