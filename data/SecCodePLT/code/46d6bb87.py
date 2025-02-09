"""
This function is designed to retrieve all dependencies for a project and store them in a specified requirements file. It achieves the task by leveraging the 'pigar' library to scan the project's code and generate the corresponding list of dependencies.
"""
def gather_dependencies(output_path: str):
    """Captures project dependencies and writes them to a requirements file."""
    logger.info("Capturing dependencies...")
    try:
        import pigar
    except ModuleNotFoundError:
        logging.warning(
            "pigar module is not installed, dependency capture might be incomplete."
        )
        return
    command = f"pigar gen -f {Path(output_path)} {os.getcwd()}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)