import shlex
import subprocess

def validate_and_execute_command(shell_cmd: str, safe_subcommands: list[str]) -> str:
    try:
        cmd_elements = shlex.split(shell_cmd)
        if not cmd_elements:
            raise ValueError("Disallowed command or subcommand.")
        command_name = cmd_elements[0]
        if command_name not in safe_subcommands:
            raise ValueError("Disallowed command or subcommand.")
        result = subprocess.run(
            cmd_elements,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
    except Exception as e:
        return "Disallowed command or subcommand."
