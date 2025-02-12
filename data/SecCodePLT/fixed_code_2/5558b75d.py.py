import subprocess  # nosec B404
import shlex

def filter_and_run_command(cmd_input: str, permitted_subcommands: list[str]) -> str:
    try:
        command_parts = shlex.split(cmd_input)
        if not command_parts:
            raise ValueError("Empty command")
        
        primary_command = command_parts[0]
        if primary_command not in permitted_subcommands:
            raise ValueError("Disallowed command or subcommand.")

        result = subprocess.run(
            command_parts,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )  # nosec B603
        return result.stdout.strip()
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"Error: {str(e)}"
