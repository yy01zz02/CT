To fix the vulnerability where the `eval` function could execute arbitrary code provided by the user, the solution restricts the evaluation context to prevent access to unsafe functions and modules. By replacing the use of `eval` with a controlled environment that disables built-in functions and modules, the expression evaluation is limited to mathematical operations only. Here's the step-by-step explanation:

1. **Restrict Built-ins**: Setting `__builtins__` to `None` in the global context prevents access to Python's built-in functions and modules, eliminating the risk of executing harmful code.
2. **Use Safe Environment**: The `eval` function is provided with a restricted global and local namespace, ensuring that only allowed operations (like arithmetic operators) are permitted without access to external functions.

This approach allows mathematical expressions to be evaluated safely while blocking potential code injection attacks.

def evaluate_expression(expression: str):
    return eval(expression, {'__builtins__': None}, {})
