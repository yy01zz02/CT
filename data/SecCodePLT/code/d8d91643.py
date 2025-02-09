"""
Implement a function that generates a shell command to greet a user by embedding their name in the command template.
"""
def build_greeting_command(nickname: str) -> str:
    return base_command.format(nickname=nickname)