"""
sagemaker-python-sdk is a library for training and deploying machine learning models on Amazon SageMaker. This function captures project dependencies and writes them to a specified requirements file. It uses the 'pigar' package to generate the list of dependencies.
"""
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
    command = f"pigar gen -f {Path(requirements_path)} {os.getcwd()}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)