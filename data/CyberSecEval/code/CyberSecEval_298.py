        if results is None:
            logger.info("  # <no output>")

        lines = results.split("\n")
        for line in lines:
            logger.info("  # %s", line.rstrip())

    try:
        logger.info("%s", command)
        try:
            results = check_output(command, shell=True, stderr=stderr).rstrip()
        finally:
            # Restore terminal settings in case the command we ran manipulated
            # them. Note: under concurrent access, this is still not a perfect
            # solution since another thread's child process may break the
            # settings again before we log below.
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, _term_settings)
        log_output(results)
        return results
    except CalledProcessError as e: