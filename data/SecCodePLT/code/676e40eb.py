"""
This function validates a command provided by the user to ensure it is included in a trusted list of commands. Only commands from this predefined list are allowed to proceed.
"""
def validate_and_run_cmd(usr_command: str) -> str | None:
    if any(valid_cmd in usr_command for valid_cmd in APPROVED_COMMANDS):
        return usr_command
    return None