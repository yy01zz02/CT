def capture_dependencies(requirements_path: str):
    """Captures project dependencies and writes them to a requirements file."""
    logger.info("Capturing dependencies...")
    try:
        import pigar
    except ModuleNotFoundError:
        logging.warning(
            "pigar module is not installed, dependency capture might be incomplete."
        )
        return
    command_args = ['pigar', 'gen', '-f', str(Path(requirements_path)), os.getcwd()]
    logger.info("Running command: %s", ' '.join(command_args))
    exit_code = subprocess.run(command_args).returncode
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)
