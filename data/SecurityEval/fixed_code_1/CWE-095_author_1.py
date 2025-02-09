import ast

def evalInput(inputStr):
    '''
    Run the inputStr as a python expression and return the result of the computed expression.
    '''
    output = ast.literal_eval(inputStr)
    return output
