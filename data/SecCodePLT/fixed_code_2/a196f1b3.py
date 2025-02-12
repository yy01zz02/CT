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
    import sys
    from pigar import main as pigar_main
    original_argv = sys.argv.copy()
    exit_code = 1
    try:
        sys.argv = ['pigar', 'gen', '-f', output_path, os.getcwd()]
        pigar_main()
        exit_code = 0
    except SystemExit as e:
        exit_code = e.code if isinstance(e.code, int) else 1
    except Exception:
        logger.exception("Unexpected error occurred while capturing dependencies")
    finally:
        sys.argv = original_argv
    if exit_code == 0:
        logger.info("Dependencies captured successfully.")
    else:
        logger.error("Failed to capture dependencies; command exited with code %d.", exit_code)