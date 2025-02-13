def execute_command(base_command, parameters):
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
    try:
        full_command = [base_command] + parameters
        output = subprocess.check_output(full_command, text=True, shell=False)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")