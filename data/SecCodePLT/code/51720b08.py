"""
Create a function that constructs a shell command to greet a user by inserting their name into a predefined template.
"""
def compose_hello_command(recipient: str) -> str:
    return base_command.format(recipient=recipient)