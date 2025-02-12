import ast

def process_user_query(query: str):
    try:
        parsed = ast.parse(query, mode='eval')
        for node in ast.walk(parsed):
            if not isinstance(node, (ast.Expression, ast.Constant, ast.UnaryOp, ast.BinOp, ast.operator, ast.unaryop)):
                raise ValueError("Invalid expression")
        result = eval(compile(parsed, filename="<string>", mode="eval"), {"__builtins__": None}, {})
    except (SyntaxError, ValueError, TypeError):
        raise ValueError("Invalid mathematical expression")
    return result
