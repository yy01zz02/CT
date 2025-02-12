import math
from simpleeval import simple_eval

def evaluate_math_expression(expr: str):
    allowed_functions = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'sqrt': math.sqrt,
        'log': math.log,
        'log10': math.log10,
        'exp': math.exp,
        'radians': math.radians,
        'degrees': math.degrees
    }
    allowed_names = {
        'pi': math.pi,
        'e': math.e
    }
    return simple_eval(expr, functions=allowed_functions, names=allowed_names)