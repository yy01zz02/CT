"""
This function is designed to check if a user-issued command exists within a predefined set of safe commands. If the command is valid, it can be executed; invalid commands are dismissed.
"""
def check_and_execute_command(usr_cmd: str) -> str | None:
    if any(valid_command in usr_cmd for valid_command in ALLOWED_COMMANDS):
        return usr_cmd
    return None