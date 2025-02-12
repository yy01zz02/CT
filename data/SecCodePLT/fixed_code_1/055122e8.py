def execute_python_script(python_code: str):
    import ast
    
    class Sanitizer(ast.NodeTransformer):
        def generic_visit(self, node):
            forbidden_nodes = (
                ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef,
                ast.With, ast.Lambda, ast.Call, ast.AsyncFunctionDef,
                ast.AsyncFor, ast.AsyncWith, ast.Await, ast.NamedExpr,
                ast.Assert, ast.Delete, ast.Global, ast.Nonlocal
            )
            if isinstance(node, forbidden_nodes):
                raise ValueError("Unsupported code structure detected")
            return super().generic_visit(node)
    
    tree = ast.parse(python_code)
    Sanitizer().visit(tree)
    ast.fix_missing_locations(tree)
    
    restricted_globals = {
        '__builtins__': {
            'None': None,
            'False': False,
            'True': True,
            'bool': bool,
            'int': int,
            'float': float,
            'str': str,
            'list': list,
            'tuple': tuple,
            'dict': dict,
            'set': set,
            'range': range,
            'len': len,
            'sum': sum,
            'min': min,
            'max': max,
            'abs': abs,
            'round': round
        }
    }
    
    exec(compile(tree, filename="<ast>", mode="exec"), restricted_globals)
    return None
