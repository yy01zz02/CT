def markdown_to_pdf(md_file_path: str, pdf_file_path: str):
    """Converts a markdown file to a PDF using pandoc."""
    import subprocess
    import shlex
    import os
    
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(md_file_path):
        logger.error("Markdown file not found: %s", md_file_path)
        raise FileNotFoundError(f"Markdown file not found: {md_file_path}")
    if not md_file_path.endswith('.md'):
        logger.error("Invalid file type: %s", md_file_path)
        raise ValueError("Invalid file type")
    command = ['pandoc', '-o', pdf_file_path, '--', md_file_path]
    logger.info("Running command: %s", ' '.join(shlex.quote(arg) for arg in command))
    result = subprocess.run(command, check=False)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)