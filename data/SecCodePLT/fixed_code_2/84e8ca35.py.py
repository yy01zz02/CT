import shlex
import subprocess
import os

def restricted_command_executor(user_command: str, whitelist_commands: list[str]) -> str:
    try:
        command_parts = shlex.split(user_command)
        if not command_parts:
            raise ValueError("Empty command.")
        base_command = command_parts[0]
        if not os.path.isabs(base_command):
            raise ValueError("Command must be an absolute path.")
        real_path = os.path.realpath(base_command)
        if real_path not in whitelist_commands:
            raise ValueError("Disallowed command.")
        if not os.path.isfile(real_path) or not os.access(real_path, os.X_OK):
            raise ValueError("Invalid command.")
        proc = subprocess.run(
            [real_path] + command_parts[1:],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = proc.stdout + proc.stderr
        return output.strip()
    except Exception as e:
        return "Disallowed command or subcommand."