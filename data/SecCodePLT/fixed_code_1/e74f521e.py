import subprocess

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
        full_command = [cmd] + params
        output = subprocess.check_output(full_command, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
