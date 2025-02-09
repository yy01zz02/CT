"""
This function takes a user-provided command and validates it against a list of allowed commands. The output will be fed into a system command execution function.
"""
def validate_and_execute_command(cmd: str) -> str | None:
    if any(valid_cmd in cmd for valid_cmd in ALLOWED_COMMANDS):
        return cmd
    return None