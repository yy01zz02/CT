def convert_md_to_pdf(input_md_path: str, output_pdf_path: str):
    """Converts a markdown file to a PDF using pandoc."""
    import os
    import subprocess
    from logging import logger

    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(input_md_path):
        logger.error("Markdown file not found: %s", input_md_path)
        raise FileNotFoundError(f"Markdown file not found: {input_md_path}")
    if not input_md_path.endswith('.md'):
        logger.error("Invalid file type: %s", input_md_path)
        raise ValueError("Invalid file type")
    command = ['pandoc', '--', input_md_path, '-o', output_pdf_path]
    logger.info("Running command: %s", ' '.join(command))
    result = subprocess.run(command)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)