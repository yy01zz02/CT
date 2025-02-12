import subprocess
import shlex

def generate_greeting_command(user_name: str) -> str:
    return base_command.format(user_name=user_name)

def execute_command(command: str) -> str:
    return subprocess.run(shlex.split(command), capture_output=True, text=True)
