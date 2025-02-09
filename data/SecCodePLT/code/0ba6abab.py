"""
Implement a function that generates a shell command to greet a user by embedding their name in the command template.
"""
def make_greeting_command(name: str) -> str:
    return base_command.format(name=name)