import ast
import re

def compute_expression_result(math_expr, values):
    try:
        # Safely replace variables with numeric values
        for key, value in values.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Non-numeric value for variable {key}")
            pattern = r'\b{0}\b'.format(re.escape(key))
            math_expr = re.sub(pattern, str(value), math_expr)
        
        math_expr = math_expr.replace(" ", "")
        
        # Validate expression using AST
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
        
        # Evaluate with restricted environment
        result = eval(math_expr, {'__builtins__': None}, {})
        return str(int(result)) if isinstance(result, float) and result.is_integer() else str(result)
    
    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")