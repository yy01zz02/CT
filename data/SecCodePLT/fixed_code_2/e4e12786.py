```
def execute_shell_command(command, args):
    allowed_commands = {'ls', 'echo', 'date'}
    if command not in allowed_commands:
        raise ValueError("Invalid command")

    try:
        full_command = [command] + args
        output = subprocess.check_output(full_command, text=True, shell=False)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
