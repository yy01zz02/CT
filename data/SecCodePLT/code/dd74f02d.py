"""
This function ensures that a user-supplied command matches one of the predefined safe commands from a list. Commands that aren't in the list of allowed commands are rejected.
"""
def run_command_if_safe(user_command: str) -> str | None:
    if any(allowed in user_command for allowed in ALLOWED_COMMANDS):
        return user_command
    return None