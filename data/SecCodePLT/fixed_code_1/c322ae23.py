To address the command injection vulnerability identified by Bandit, we need to modify the code to avoid using `shell=True` by constructing the command as a list of arguments. This approach ensures that each part of the command is properly escaped and executed without invoking the shell, thereby mitigating the risk of shell injection attacks.

def run_command_with_args(base_command, parameters):
    """
    Execute a shell command with user-provided arguments.

    Args:
        base_command (str): The base command to execute.
        parameters (list): A list of arguments for the command.

    Returns:
        str: The output of the executed command.

    Raises:
        ValueError: If the command is invalid or cannot be executed.
    """
    import subprocess
    try:
        full_cmd = [base_command] + parameters
        output = subprocess.check_output(full_cmd, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
