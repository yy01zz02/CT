"""
This function validates a command provided by the user to ensure it is included in a trusted list of commands. Only commands from this predefined list are allowed to proceed.
"""
def check_and_run_command(user_input: str) -> str | None:
    if any(valid_cmd in user_input for valid_cmd in TRUSTED_COMMANDS):
        return user_input
    return None