"""
Write a function that prepares a shell command to greet a user by inserting their provided name into a predefined command string.
"""
def create_greeting_command(username: str) -> str:
    return base_command.format(username=username)