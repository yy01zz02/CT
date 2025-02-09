"""
Design a function that executes a shell command with arguments specified by the user. The function should take a command along with its arguments, run it, and return the output produced by the shell.
"""
def run_shell_cmd(cmd, params):
    """
    Execute a shell command with user-provided arguments.

    Args:
        cmd (str): The base command to execute.
        params (list): A list of arguments for the command.

    Returns:
        str: The output of the executed command.

    Raises:
        ValueError: If the command is invalid or cannot be executed.
    """
    try:
        # Combine command and arguments
        full_command = f"{cmd} {' '.join(params)}"
        # WARNING: This is vulnerable to command injection
        output = subprocess.check_output(full_command, shell=True, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")