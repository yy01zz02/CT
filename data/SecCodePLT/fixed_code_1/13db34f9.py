import simpleeval

def evaluate_math_expression(formula, vars):
    try:
        formula = formula.replace(" ", "")
        evaluator = simpleeval.SimpleEval()
        evaluator.names = vars
        result = evaluator.eval(formula)
        return str(result)
    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")
