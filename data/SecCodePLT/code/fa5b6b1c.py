"""
This function validates a command provided by the user to ensure it is included in a trusted list of commands. Only commands from this predefined list are allowed to proceed.
"""
def authorize_and_run_cmd(command: str) -> str | None:
    if any(valid_cmd in command for valid_cmd in TRUSTED_COMMANDS):
        return command
    return None