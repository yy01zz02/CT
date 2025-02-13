def gather_dependencies(output_file: str):
    """Captures project dependencies and writes them to a requirements file."""
    logger.info("Capturing project dependencies...")
    try:
        import pigar
    except ModuleNotFoundError:
        logging.warning(
            "pigar module is not installed, dependency capture might be incomplete."
        )
        return
    args = ['pigar', 'gen', '-f', str(Path(output_file)), os.getcwd()]
    logger.info("Running command: %s", ' '.join(args))
    exit_code = subprocess.run(args, shell=False).returncode
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)
