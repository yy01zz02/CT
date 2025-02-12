def convert_md_to_pdf(input_md_path: str, output_pdf_path: str):
    """Converts a markdown file to a PDF using pandoc."""
    import os
    import subprocess  # nosec: B404
    import shlex
    from logging import logger

    logger.info("Converting markdown file to PDF...")
    input_md_path = os.path.abspath(input_md_path)
    output_pdf_path = os.path.abspath(output_pdf_path)

    if not os.path.exists(input_md_path):
        logger.error("Markdown file not found: %s", input_md_path)
        raise FileNotFoundError(f"Markdown file not found: {input_md_path}")
    if not os.path.isfile(input_md_path):
        logger.error("Invalid file: %s", input_md_path)
        raise ValueError("Invalid file")
    if not input_md_path.endswith('.md'):
        logger.error("Invalid file type: %s", input_md_path)
        raise ValueError("Invalid file type")

    command = ['pandoc', '--', input_md_path, '-o', output_pdf_path]
    logger.info("Running command: %s", shlex.join(command))
    result = subprocess.run(command, shell=False)  # nosec: B603
    exit_code = result.returncode

    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)
