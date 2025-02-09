"""
The purpose of this function is to analyze and collect the dependencies of a project, writing them to a specified requirements file. It achieves this by utilizing the 'pigar' package to look up and generate the list.
"""
def fetch_project_dependencies(dep_file_path: str):
    """Captures project dependencies and writes them to a requirements file."""
    logger.info("Capturing dependencies...")
    try:
        import pigar
    except ModuleNotFoundError:
        logging.warning(
            "pigar module is not installed, dependency capture might be incomplete."
        )
        return
    command = f"pigar gen -f {Path(dep_file_path)} {os.getcwd()}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)