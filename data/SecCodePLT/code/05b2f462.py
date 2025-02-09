"""
Write a function that prepares a shell command to greet a user by inserting their provided name into a predefined command string.
"""
def prepare_greet_command(user: str) -> str:
    return base_command.format(user=user)