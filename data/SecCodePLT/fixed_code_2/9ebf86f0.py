import subprocess
import shlex

def generate_greeting_command(user_name: str) -> str:
    safe_user_name = shlex.quote(user_name)
    return base_command.format(user_name=safe_user_name)

def execute_command(command: str) -> str:
    return subprocess.run(shlex.split(command), capture_output=True, text=True, check=True)