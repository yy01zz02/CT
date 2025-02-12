from typing import List

def generate_greeting_command(user_name: str) -> List[str]:
    return ["Hello", user_name]

def execute_command(command: List[str]) -> str:
    return " ".join(command)
