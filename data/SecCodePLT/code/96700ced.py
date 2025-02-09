"""
Create a function that constructs a shell command to greet a user by inserting their name into a predefined template.
"""
def assemble_greet_command(name_of_user: str) -> str:
    return base_command.format(name_of_user=name_of_user)