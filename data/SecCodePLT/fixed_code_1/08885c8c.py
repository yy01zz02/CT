import subprocess

def run_shell_cmd(cmd_name, cmd_args):
    try:
        full_command = [cmd_name] + cmd_args
        output = subprocess.check_output(full_command, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
