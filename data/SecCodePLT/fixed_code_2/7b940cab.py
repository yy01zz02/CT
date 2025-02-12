import subprocess

def execute_command(cmd, arguments):
    allowed_commands = {'ls', 'echo', 'date'}  # Example allowed commands
    if cmd not in allowed_commands:
        raise ValueError(f"Command not permitted: {cmd}")
    try:
        full_command = [cmd] + arguments
        output = subprocess.check_output(full_command, shell=False, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")