def fetch_dependencies(dep_output_path: str):
    """Captures project dependencies and writes them to a requirements file."""
    import subprocess
    from pathlib import Path
    import os
    logger.info("Capturing dependencies...")
    try:
        import pigar
    except ModuleNotFoundError:
        logger.warning(
            "pigar module is not installed, dependency capture might be incomplete."
        )
        return
    command_args = [
        'pigar',
        'gen',
        '-f',
        str(Path(dep_output_path)),
        os.getcwd()
    ]
    logger.info("Running command: %s", ' '.join(command_args))
    result = subprocess.run(command_args, check=False)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)
