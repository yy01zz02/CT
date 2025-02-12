To fix the vulnerability caused by using `eval` with untrusted input, the safest approach is to avoid `eval` entirely. However, if the function's intent is to evaluate mathematical expressions, a secure alternative is to parse the input string and use a restricted evaluation environment. Here's the corrected code:

def evaluate_expression(expr: str):
    allowed_chars = set("0123456789+-*/(). ")
    if not all(c in allowed_chars for c in expr):
        raise ValueError("Invalid characters in expression")
    return eval(expr, {"__builtins__": None}, {})
```

**Step-by-Step Explanation:**

1. **Input Validation:** Check if the input `expr` contains only allowed characters (digits, basic mathematical operators, parentheses, periods, and spaces). This prevents injection of malicious code.
2. **Restricted Eval Environment:** Use `eval` with `__builtins__` set to `None` and no local variables, which blocks access to potentially dangerous functions or modules. This reduces the risk of arbitrary code execution.

This approach mitigates the security risk by ensuring that only safe mathematical operations are evaluated.