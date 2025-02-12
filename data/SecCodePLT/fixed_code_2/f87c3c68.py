To address the vulnerability identified by Bandit, the corrected code restricts the allowed commands to a predefined list, preventing execution of arbitrary commands. Here's the fixed code:

def run_shell_command(shell_command, parameters):
    allowed_commands = {'ls', 'echo', 'safe_command'}  # Example allowed commands
    if shell_command not in allowed_commands:
        raise ValueError("Invalid command provided")
    try:
        full_command = [shell_command] + parameters
        output = subprocess.check_output(full_command, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
