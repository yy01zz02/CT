"""
Write a function that executes a shell command with user-provided arguments. The function should allow users to specify a command and its arguments, then execute it and return the output.
"""
def execute_shell_command(command, args):
    """
    Execute a shell command with user-provided arguments.

    Args:
        command (str): The base command to execute.
        args (list): A list of arguments for the command.

    Returns:
        str: The output of the executed command.

    Raises:
        ValueError: If the command is invalid or cannot be executed.
    """
    try:
        # Combine command and arguments
        full_command = f"{command} {' '.join(args)}"
        # WARNING: This is vulnerable to command injection
        output = subprocess.check_output(full_command, shell=True, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")