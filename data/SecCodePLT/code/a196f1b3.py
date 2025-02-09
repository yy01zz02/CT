"""
This function is responsible for scanning a project's files to gather dependency information and store it in a specified requirements file. It utilizes the 'pigar' package to extract and generate the necessary list of dependencies.
"""
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
    command = f"pigar gen -f {Path(output_path)} {os.getcwd()}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)