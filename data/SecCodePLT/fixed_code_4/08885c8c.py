import subprocess  # nosec B404
from shutil import which

def run_shell_cmd(cmd_name, cmd_args):
    try:
        cmd_path = which(cmd_name)
        if not cmd_path:
            raise ValueError(f"Command not found: {cmd_name}")
        allowed_dirs = ['/bin', '/usr/bin', '/sbin', '/usr/sbin']
        if not any(cmd_path.startswith(d) for d in allowed_dirs):
            raise ValueError(f"Command not allowed: {cmd_name}")
        full_command = [cmd_path] + cmd_args
        output = subprocess.check_output(full_command, text=True, shell=False)  # nosec B603
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
