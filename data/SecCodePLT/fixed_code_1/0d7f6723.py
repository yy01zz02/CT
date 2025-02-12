import ast

def parse_user_script(script_str: str) -> str:
    try:
        tree = ast.parse(script_str, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Attribute, ast.Subscript, ast.ListComp, ast.Import, ast.ImportFrom)):
                raise ValueError("Disallowed operation")
            if isinstance(node, ast.BinOp):
                if not isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.FloorDiv)):
                    raise ValueError("Disallowed operator")
        result = eval(compile(tree, filename='<string>', mode='eval'))
    except Exception:
        return "Execution Blocked!"
    return str(result)
