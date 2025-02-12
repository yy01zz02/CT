def call_system_command(sys_command, params):
    try:
        full_cmd = [sys_command] + params
        output = subprocess.check_output(full_cmd, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Command execution failed: {e}")
    except Exception as e:
        raise ValueError(f"Error executing command: {str(e)}")
