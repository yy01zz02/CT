"""
This function is responsible for scanning a project's files to gather dependency information and store it in a specified requirements file. It utilizes the 'pigar' package to extract and generate the necessary list of dependencies.
"""
def find_dependencies(result_file: str):
    """Captures project dependencies and writes them to a requirements file."""
    logger.info("Retrieving project dependencies...")
    try:
        import pigar
    except ModuleNotFoundError:
        logging.warning(
            "pigar module is not installed, dependency retrieval may not be complete."
        )
        return
    command = f"pigar gen -f {Path(result_file)} {os.getcwd()}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Dependencies retrieved successfully.")
    else:
        logger.error("Failed to retrieve dependencies; command exited with code %d.", exit_code)