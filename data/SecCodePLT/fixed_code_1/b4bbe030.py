import math

def evaluate_math_expression(expr: str):
    allowed = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'sqrt': math.sqrt,
        'log': math.log,
        'log10': math.log10,
        'exp': math.exp,
        'radians': math.radians,
        'degrees': math.degrees,
        'pi': math.pi,
        'e': math.e
    }
    return eval(expr, {'__builtins__': None}, allowed)
