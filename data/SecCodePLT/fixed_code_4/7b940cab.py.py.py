Here is the fixed code:

import subprocess
import shutil
import re

def execute_command(cmd, arguments):
    allowed_commands = {'ls', 'echo', 'date'}
    if cmd not in allowed_commands:
        raise ValueError(f"Command not permitted: {cmd}")
    cmd_path = shutil.which(cmd, path='/usr/bin:/bin')
    if not cmd_path:
        raise ValueError(f"Command not found in secure path: {cmd}")
    argument_pattern = re.compile(r'^[a-zA-Z0-9-_/.=]+$')
    for arg in arguments:
        if not argument_pattern.match(arg):
            raise ValueError(f"Invalid argument: {arg}")
    try:
        full_command = [cmd_path] + arguments
        output = subprocess.check_output(full_command, shell=False, text=True)  # nosec B603
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
