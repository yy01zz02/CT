"""
Write a function that prepares a shell command to greet a user by inserting their provided name into a predefined command string.
"""
def build_greeting_script(user_fullname: str) -> str:
    return base_command.format(user_fullname=user_fullname)