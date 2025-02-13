def log_project_dependencies(dependency_file_path: str):
    """Captures project dependencies and writes them to a requirements file."""
    import subprocess  # nosec B404
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
    args = ['pigar', 'gen', '-f', str(Path(dependency_file_path)), os.getcwd()]
    logger.info("Running command: %s", ' '.join(args))
    result = subprocess.run(args, shell=False)  # nosec B603
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)