import re
import ast

def process_expression(expression_str: str) -> str:
    allowed_pattern = re.compile(r'^[\d+\-*/%().\s]+$')
    if not allowed_pattern.match(expression_str.replace(" ", "")):
        return "Computation Error!"
    try:
        parsed = ast.parse(expression_str, mode='eval')
        if any(isinstance(node, (ast.Call, ast.Attribute)) for node in ast.walk(parsed)):
            return "Computation Error!"
        
        def evaluate_node(node):
            if isinstance(node, ast.Constant):
                return node.value
            elif isinstance(node, ast.BinOp):
                left = evaluate_node(node.left)
                right = evaluate_node(node.right)
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
                else:
                    raise ValueError()
            elif isinstance(node, ast.UnaryOp):
                operand = evaluate_node(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                elif isinstance(node.op, ast.UAdd):
                    return operand
                else:
                    raise ValueError()
            else:
                raise ValueError()
        
        result = evaluate_node(parsed.body)
    except Exception:
        return "Computation Error!"
    return str(result)
