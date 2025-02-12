import subprocess
import shutil

def execute_command(cmd, arguments):
    allowed_commands = {'ls', 'echo', 'date'}
    if cmd not in allowed_commands:
        raise ValueError(f"Command not permitted: {cmd}")
    cmd_path = shutil.which(cmd, path='/usr/bin:/bin')
    if not cmd_path:
        raise ValueError(f"Command not found in secure path: {cmd}")
    try:
        full_command = [cmd_path] + arguments
        output = subprocess.check_output(full_command, shell=False, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
