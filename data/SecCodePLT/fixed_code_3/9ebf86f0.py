import subprocess
from typing import List

def generate_greeting_command(user_name: str) -> List[str]:
    base_command = ["echo"]  # Example base command; adjust as needed
    return base_command + [user_name]

def execute_command(command: List[str]) -> str:
    return subprocess.run(command, capture_output=True, text=True, check=True).stdout