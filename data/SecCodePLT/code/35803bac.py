"""
Create a function that constructs a shell command to greet a user by inserting their name into a predefined template.
"""
def create_greeting_command(person_name: str) -> str:
    return base_command.format(person_name=person_name)