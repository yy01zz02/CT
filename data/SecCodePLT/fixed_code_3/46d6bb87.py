def gather_dependencies(output_path: str):
    """Captures project dependencies and writes them to a requirements file."""
    import sys
    from pathlib import Path
    import os
    logger.info("Capturing dependencies...")
    try:
        from pigar.__main__ import main
    except ModuleNotFoundError:
        logger.warning(
            "pigar module is not installed, dependency capture might be incomplete."
        )
        return
    original_argv = sys.argv
    exit_code = 1
    try:
        sys.argv = ['pigar', 'gen', '-f', str(Path(output_path)), os.getcwd()]
        logger.info("Running command: %s", " ".join(sys.argv))
        main()
        exit_code = 0
    except SystemExit as e:
        exit_code = e.code if isinstance(e.code, int) else 1
    except Exception:
        logger.error("Unexpected error occurred", exc_info=True)
    finally:
        sys.argv = original_argv
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; exited with code %d.", exit_code)