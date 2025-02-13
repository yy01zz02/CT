import ast
import re

def compute_expression_result(math_expr, values):
    try:
        for key, value in values.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Non-numeric value for variable {key}")
            pattern = r'\b{0}\b'.format(re.escape(key))
            math_expr = re.sub(pattern, str(value), math_expr)
        
        math_expr = math_expr.replace(" ", "")
        
        tree = ast.parse(math_expr, mode='eval')
        
        class SafeValidator(ast.NodeVisitor):
            allowed = (ast.Expression, ast.UnaryOp, ast.BinOp, ast.Constant,
                       ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow,
                       ast.USub, ast.UAdd)
            def generic_visit(self, node):
                if not isinstance(node, self.allowed):
                    raise ValueError(f"Unsafe operation detected: {type(node).__name__}")
                super().generic_visit(node)
        
        SafeValidator().visit(tree)
        
        class Evaluator(ast.NodeVisitor):
            def visit_Constant(self, node):
                return node.value
            def visit_UnaryOp(self, node):
                operand = self.visit(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                elif isinstance(node.op, ast.UAdd):
                    return +operand
                else:
                    raise ValueError("Invalid unary operator")
            def visit_BinOp(self, node):
                left = self.visit(node.left)
                right = self.visit(node.right)
                if isinstance(node.op, ast.Add):
                    return left + right
                elif isinstance(node.op, ast.Sub):
                    return left - right
                elif isinstance(node.op, ast.Mult):
                    return left * right
                elif isinstance(node.op, ast.Div):
                    return left / right
                elif isinstance(node.op, ast.Mod):
                    return left % right
                elif isinstance(node.op, ast.Pow):
                    return left ** right
                else:
                    raise ValueError("Invalid binary operator")
            def visit_Expression(self, node):
                return self.visit(node.body)
        
        evaluator = Evaluator()
        result = evaluator.visit(tree)
        
        return str(int(result)) if isinstance(result, float) and result.is_integer() else str(result)
    
    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")