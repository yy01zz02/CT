"""
This function generates a shell command to greet a user by name. It constructs the command using the provided user name. The greeting command is then executed using an execute_command function (no need to implement it).
"""
def generate_greeting_command(user_name: str) -> str:
    return base_command.format(user_name=user_name)
def execute_command(command: str) -> str:
    return subprocess.run(command, shell=True, capture_output=True, text=True)