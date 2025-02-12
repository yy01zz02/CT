import subprocess

def execute_command(cmd, arguments):
    try:
        full_command = [cmd] + arguments
        output = subprocess.check_output(full_command, shell=False, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
