To fix the vulnerabilities identified by Bandit, the use of `eval` can be made safer by validating the input more rigorously through AST (Abstract Syntax Tree) parsing and restricting allowed operations. This approach ensures only mathematical expressions are evaluated safely.

def calculate_expression(math_expr: str):
    import ast

    sanitized_expr = math_expr.replace(" ", "")

    class SafeEvaluator(ast.NodeVisitor):
        def visit_Expression(self, node):
            self.visit(node.body)
        
        def visit_BinOp(self, node):
            if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
                self.visit(node.left)
                self.visit(node.right)
            else:
                raise ValueError("Invalid operation")
        
        def visit_UnaryOp(self, node):
            if isinstance(node.op, (ast.UAdd, ast.USub)):
                self.visit(node.operand)
            else:
                raise ValueError("Invalid operation")
        
        def visit_Constant(self, node):
            pass
        
        def visit_Num(self, node):
            pass
        
        def generic_visit(self, node):
            raise ValueError(f"Unsupported node: {type(node).__name__}")

    try:
        tree = ast.parse(sanitized_expr, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid mathematical expression")
    
    SafeEvaluator().visit(tree)
    
    return eval(compile(tree, '<string>', 'eval'), {'__builtins__': None}, {})
