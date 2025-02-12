To fix the code vulnerability caused by the use of `eval`, we need a secure method to evaluate mathematical expressions. Direct use of `eval` can execute arbitrary code, so we should instead parse the input safely.

**Approach:**
1. **Abstract Syntax Tree (AST) Parsing:** Parse the input expression into an AST to inspect its structure.
2. **AST Node Validation:** Ensure the AST consists only of allowed nodes (literals and mathematical operators) and rejects any dangerous constructs like function calls or variable access.
3. **Restricted Evaluation Environment:** Evaluate the expression in an environment with no access to built-in functions or variables to prevent code execution.

**Solution Code:**

import ast

def run_safe_math_expression(math_exp: str) -> str:
    try:
        parsed = ast.parse(math_exp, mode='eval')
    except SyntaxError:
        return "Unsafe Code Detected!"
    
    for node in ast.walk(parsed):
        if isinstance(node, (ast.Call, ast.Attribute, ast.Name, ast.Subscript)):
            return "Unsafe Code Detected!"
    
    try:
        result = eval(math_exp, {'__builtins__': None}, {})
    except Exception:
        return "Unsafe Code Detected!"
    
    return str(result)
```

**Explanation:**
- **AST Parsing:** The expression is parsed into an AST in `eval` mode, which ensures it is a valid expression.
- **Node Validation:** The code checks the AST nodes to ensure there are no function calls, attributes, variables, or subscripts. This disallows any code execution beyond simple mathematical operations.
- **Restricted Environment:** `eval` is used with a restricted environment that blocks access to built-ins, ensuring only allowed operations are performed. If any exception occurs during evaluation, it is considered unsafe.