import ast
import operator

class SafeEvaluator(ast.NodeVisitor):
    def __init__(self):
        self.ops = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.USub: operator.neg,
            ast.UAdd: operator.pos,
        }
    
    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_type = type(node.op)
        if op_type not in self.ops:
            raise ValueError(f"Unsupported operator: {op_type}")
        return self.ops[op_type](left, right)
    
    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        op_type = type(node.op)
        if op_type not in self.ops:
            raise ValueError(f"Unsupported unary operator: {op_type}")
        return self.ops[op_type](operand)
    
    def visit_Constant(self, node):
        return node.value
    
    def visit_Num(self, node):
        return node.n
    
    def visit_Name(self, node):
        raise ValueError(f"Variable '{node.id}' not substituted")
    
    def generic_visit(self, node):
        raise ValueError(f"Disallowed node type: {type(node).__name__}")

def evaluate_expression(expr, var_map):
    try:
        for var, value in var_map.items():
            expr = expr.replace(var, str(value))
        expr = expr.replace(" ", "")
        tree = ast.parse(expr, mode='eval')
        evaluator = SafeEvaluator()
        result = evaluator.visit(tree.body)
        return str(result)
    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")