To fix this code, we need to safely evaluate mathematical expressions by restricting the use of `eval` to a controlled environment. Here's how we can approach and resolve the issues:

### Approach
1. **Problem Analysis**: The current code uses `eval` directly on user input, which can execute arbitrary code and is a security risk. We need a safer way to evaluate mathematical expressions.
2. **Use of Restricted Environment**: Instead of using `eval` without restrictions, we provide a controlled globals dictionary. This restricts access to built-in functions and modules except those explicitly allowed (like the `math` module).
3. **Handling Mathematical Functions**: By importing the `math` module and including it in the allowed globals, users can utilize mathematical functions (e.g., `math.sqrt`) safely.
4. **Exception Handling**: Maintain the existing structure to catch exceptions and return a security message, ensuring unsafe code is detected and handled.

### Solution Code
def evaluate_expression_securely(input_code: str) -> str:
    import math
    restricted_globals = {'__builtins__': None, 'math': math}
    try:
        result = eval(input_code, restricted_globals, {})
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)
```

### Explanation
- **Restricted Environment**: The `restricted_globals` dictionary disables built-ins (`__builtins__`: None) and allows access only to the `math` module.
- **Safe Evaluation**: Expressions are evaluated within the restricted environment, preventing execution of dangerous functions while allowing valid mathematical operations and `math` module functions.
- **Exception Handling**: Any attempt to execute unsafe code results in an exception, which is caught, returning a security warning. This ensures the function remains secure while providing useful mathematical evaluation.