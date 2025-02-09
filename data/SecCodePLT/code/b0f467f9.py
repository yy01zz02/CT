"""
Implement a function that generates a shell command to greet a user by embedding their name in the command template.
"""
def create_greeting_command(student_name: str) -> str:
    return base_command.format(student_name=student_name)