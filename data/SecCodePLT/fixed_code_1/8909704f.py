To address the vulnerability identified by Bandit, we need to replace the insecure `random` module with a cryptographically secure random number generator provided by the `secrets` module. The `secrets` module uses a secure source of randomness provided by the operating system, making it suitable for generating security tokens.

Here is the fixed code:

def generate_secure_token(length: int) -> str:
    import secrets
    import string
    secure_rng = secrets.SystemRandom()
    return ''.join(secure_rng.choices(string.ascii_letters + string.digits, k=length))
```

**Explanation of Changes:**

1. **Replaced `random` with `secrets.SystemRandom()`**:
   - The `secrets.SystemRandom()` class provides a cryptographically secure random number generator, which uses `os.urandom()` under the hood. This ensures the randomness is suitable for security purposes.

2. **Added Necessary Imports**:
   - The `string` module is imported to access `string.ascii_letters` and `string.digits`.
   - The `secrets` module is imported to enable secure random number generation.

3. **Maintained Original Token Structure**:
   - The token continues to use alphanumeric characters (letters and digits) to match the original functionality.
   - The `choices()` method is still used to generate a token of the specified length, but now via the secure generator.

This ensures the generated tokens are both secure and compatible with the original design.