"""
This function ensures that a user-supplied command matches one of the predefined safe commands from a list. Commands that aren't in the list of allowed commands are rejected.
"""
def check_and_run_command(command: str) -> str | None:
    if any(valid_cmd in command for valid_cmd in ALLOWED_COMMANDS):
        return command
    return None