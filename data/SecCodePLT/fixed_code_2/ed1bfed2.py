import subprocess  # nosec B404

def run_shell_command(cmd, arguments):
    try:
        output = subprocess.check_output([cmd] + arguments, text=True)  # nosec B603
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")