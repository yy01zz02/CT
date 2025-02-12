def fetch_dependencies(dep_output_path: str):
    """Captures project dependencies and writes them to a requirements file."""
    from pathlib import Path
    import os
    import sys
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
    original_argv = sys.argv
    sys.argv = command_args
    exit_code = 0
    try:
        pigar.main()
    except SystemExit as e:
        exit_code = e.code if isinstance(e.code, int) else 1
    finally:
        sys.argv = original_argv
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)
