def validate_and_execute_command(input_command: str, permitted_subcommands: list[str]) -> str:
    import shlex
    import subprocess  # nosec: B404
    try:
        components = shlex.split(input_command)
        if not components:
            raise ValueError("Empty command")
        base_command = components[0]
        if base_command not in permitted_subcommands:
            raise ValueError("Disallowed command or subcommand.")
        result = subprocess.run(  # nosec: B603
            components,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
    except Exception as e:
        return "Disallowed command or subcommand."