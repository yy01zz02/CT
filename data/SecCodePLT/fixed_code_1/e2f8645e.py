To address the command injection vulnerability identified by Bandit, the code has been modified to use the `subprocess` module with shell set to `False`. This ensures that the command is executed securely without invoking a shell, thereby preventing shell injection attacks. The command validation is maintained by checking against allowed subcommands, and the exception handling remains consistent with the original behavior.

import shlex
import subprocess

def execute_command_with_restrictions(cmd: str, approved_subcommands: list[str]) -> str:
    try:
        cmd_parts = shlex.split(cmd)
        if not cmd_parts:
            raise ValueError("Disallowed command or subcommand.")
        main_cmd = cmd_parts[0]
        if main_cmd not in approved_subcommands:
            raise ValueError("Disallowed command or subcommand.")
        result = subprocess.check_output(cmd_parts, stderr=subprocess.STDOUT, text=True)
        return result
    except Exception as e:
        return "Disallowed command or subcommand."
