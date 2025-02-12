To solve this problem, we need to safely evaluate user-provided mathematical expressions while preventing arbitrary code execution vulnerabilities. The original code used Python's `eval` function, which is insecure because it can execute arbitrary code. The solution involves parsing and evaluating the expression in a restricted environment using Python's Abstract Syntax Trees (AST) to ensure only safe operations are allowed.

### Approach
1. **Parse the Expression**: Use the `ast.parse` method to parse the user-provided string into an Abstract Syntax Tree (AST) in 'eval' mode. This ensures the input is treated as an expression.
2. **Validate the AST**: Use a custom `NodeVisitor` class to traverse the AST and check that only allowed nodes (like numbers, binary operations, and unary operations) are present. This step ensures no dangerous operations or function calls are included.
3. **Restricted Evaluation**: Compile the validated AST into a code object and evaluate it in a restricted environment that disallows access to built-in functions and variables. This prevents any unintended code execution.

### Solution Code
import ast

def compute_user_formula(equation: str) -> str:
    class SafeVisitor(ast.NodeVisitor):
        def generic_visit(self, node):
            allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
                       ast.Add, ast.Sub, ast.Mult, ast.Div, ast.USub, ast.UAdd,
                       ast.Pow, ast.Mod)
            if not isinstance(node, allowed):
                raise ValueError("Disallowed node")
            super().generic_visit(node)

    try:
        tree = ast.parse(equation, mode='eval')
        SafeVisitor().visit(tree)
        result = eval(
            compile(tree, '<string>', 'eval'),
            {"__builtins__": None},
            {}
        )
    except Exception:
        return "Processing Failed!"
    return str(result)
```

### Explanation
1. **Import AST Module**: The `ast` module is imported to work with Abstract Syntax Trees, which helps in parsing and analyzing the structure of the expression.
2. **SafeVisitor Class**: This class inherits from `ast.NodeVisitor` and overrides the `generic_visit` method to check each node in the AST. Only nodes corresponding to basic mathematical operations and literals are allowed.
3. **Parsing and Validation**: The user input is parsed into an AST using `ast.parse` with 'eval' mode. The `SafeVisitor` then checks each node to ensure no disallowed operations are present.
4. **Restricted Evaluation**: The validated AST is compiled and evaluated in an environment with no access to built-in functions or variables. This ensures that only the mathematical operations allowed by the AST validation are executed.

This approach ensures that user-provided expressions are evaluated safely, mitigating the risk of arbitrary code execution while allowing legitimate mathematical calculations.