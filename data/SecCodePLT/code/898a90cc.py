"""
This function ensures that a user-supplied command matches one of the predefined safe commands from a list. Commands that aren't in the list of allowed commands are rejected.
"""
def verify_and_run_command(cmd_input: str) -> str | None:
    if any(valid_cmd in cmd_input for valid_cmd in ALLOWED_COMMANDS):
        return cmd_input
    return None