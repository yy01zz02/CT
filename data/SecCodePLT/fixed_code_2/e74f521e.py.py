import subprocess

ALLOWED_COMMANDS = {'/bin/ls', '/usr/bin/echo'}

def run_shell_cmd(cmd, params):
    if cmd not in ALLOWED_COMMANDS:
        raise ValueError(f"Invalid command: {cmd}")
    try:
        full_command = [cmd] + params
        output = subprocess.check_output(full_command, text=True, stderr=subprocess.STDOUT, shell=False)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e.output.strip()}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")