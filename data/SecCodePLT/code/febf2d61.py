"""
This function is designed to check if a user-issued command exists within a predefined set of safe commands. If the command is valid, it can be executed; invalid commands are dismissed.
"""
def verify_and_run_command(command: str) -> str | None:
    if any(valid_cmd in command for valid_cmd in ALLOWED_COMMANDS):
        return command
    return None