import shlex
import subprocess

def restricted_command_executor(user_command: str, whitelist_commands: list[str]) -> str:
    try:
        command_parts = shlex.split(user_command)
        base_command = command_parts[0]
        if base_command not in whitelist_commands:
            raise ValueError("Disallowed command or subcommand.")
        
        proc = subprocess.run(
            command_parts,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = proc.stdout + proc.stderr
        return output.strip()
    except Exception as e:
        return "Disallowed command or subcommand."
