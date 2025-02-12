def extract_dependencies(output_path: str):
    """Captures project dependencies and writes them to a requirements file."""
    logger.info("Capturing project dependencies...")
    try:
        import pigar
    except ModuleNotFoundError:
        logging.warning(
            "pigar module is not installed, dependency capture might be incomplete."
        )
        return
    from subprocess import run
    command = ['pigar', 'gen', '-f', output_path, os.getcwd()]
    logger.info("Running command: %s", ' '.join(command))
    exit_code = run(command).returncode
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)
