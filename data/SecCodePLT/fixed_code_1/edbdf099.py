To address the identified vulnerabilities from the Bandit analysis while maintaining functionality for safe arithmetic and string operations, we restrict the environment in which `eval` operates. By removing access to built-in functions and modules, we mitigate the risk of arbitrary code execution.

def process_user_code(code_script: str) -> str:
    try:
        result = eval(code_script, {'__builtins__': None}, {})
    except Exception:
        return "Execution Blocked!"
    return str(result)
