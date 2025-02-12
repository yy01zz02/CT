import subprocess  # nosec
import os
import logging

logger = logging.getLogger(__name__)

def md_to_pdf_converter(markdown_file: str, pdf_output: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(markdown_file):
        logger.error("Markdown file not found: %s", markdown_file)
        raise FileNotFoundError(f"Markdown file not found: {markdown_file}")
    if not markdown_file.endswith('.md'):
        logger.error("Invalid file type: %s", markdown_file)
        raise ValueError("Input file must be a Markdown file with .md extension")
    if not pdf_output.endswith('.pdf'):
        logger.error("Invalid output file type: %s", pdf_output)
        raise ValueError("Output file must have a .pdf extension")
    command = ["pandoc", markdown_file, "-o", pdf_output]
    logger.info("Running command: %s", " ".join(command))
    result = subprocess.run(command, capture_output=True, text=True)  # nosec
    if result.returncode == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; pandoc exited with code %d. Error: %s", result.returncode, result.stderr)
        raise RuntimeError(f"Pandoc conversion failed: {result.stderr}")