"""
This function is designed to check if a user-issued command exists within a predefined set of safe commands. If the command is valid, it can be executed; invalid commands are dismissed.
"""
def check_and_run_command(command_input: str) -> str | None:
    if any(valid_command in command_input for valid_command in ALLOWED_COMMANDS):
        return command_input
    return None