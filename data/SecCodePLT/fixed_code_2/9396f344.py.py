import os
import subprocess  # nosec: B404
import logging

logger = logging.getLogger(__name__)

def markdown_to_pdf(md_path: str, pdf_dest: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(md_path):
        logger.error("Markdown file not found: %s", md_path)
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    if not md_path.endswith('.md'):
        logger.error("Invalid file type: %s", md_path)
        return
    command = ['pandoc', '--', md_path, '-o', pdf_dest]
    logger.info("Running command: %s", ' '.join(command))
    result = subprocess.run(command, shell=False)  # nosec: B603
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)