import os
import subprocess  # nosec B404
import logging

logger = logging.getLogger(__name__)

def markdown_to_pdf_conversion(md_file_path: str, pdf_file_output: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(md_file_path):
        logger.error("Markdown file not found: %s", md_file_path)
        raise FileNotFoundError(f"Markdown file not found: {md_file_path}")
    if not os.path.isfile(md_file_path):
        logger.error("Not a file: %s", md_file_path)
        raise ValueError("Input path is not a file")
    if not md_file_path.endswith('.md'):
        logger.error("Invalid file type: %s", md_file_path)
        raise ValueError("Invalid file type")
    command = ["pandoc", "--", md_file_path, "-o", pdf_file_output]
    logger.info("Running command: %s", " ".join(command))
    result = subprocess.run(command, check=False)  # nosec B603
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)
        raise RuntimeError(f"Conversion failed with exit code {exit_code}")