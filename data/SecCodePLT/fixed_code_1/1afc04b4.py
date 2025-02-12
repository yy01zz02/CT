import shlex
import subprocess
from typing import List

def run_shell_command_with_filters(command: str, allowed_subcommands_list: List[str]) -> str:
    try:
        components = shlex.split(command)
        if not components:
            raise ValueError("Empty command.")
        
        main_command = components[0]
        if main_command not in allowed_subcommands_list:
            raise ValueError("Disallowed command or subcommand.")
        
        result = subprocess.run(
            components,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
    except Exception:
        return "Disallowed command or subcommand."
