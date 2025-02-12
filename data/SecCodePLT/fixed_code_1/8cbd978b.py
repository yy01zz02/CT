import shlex
import subprocess

def filter_and_run_os_command(exec_command: str, whitelisted_subcommands: list[str]) -> str:
    try:
        components = shlex.split(exec_command)
        if not components:
            raise ValueError("Disallowed command or subcommand.")
        primary_command = components[0]
        if primary_command not in whitelisted_subcommands:
            raise ValueError("Disallowed command or subcommand.")
        result = subprocess.run(
            components,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()
    except Exception:
        return "Disallowed command or subcommand."