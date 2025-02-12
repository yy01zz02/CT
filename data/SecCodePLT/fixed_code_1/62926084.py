import subprocess

def md_to_pdf_converter(markdown_file: str, pdf_output: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(markdown_file):
        logger.error("Markdown file not found: %s", markdown_file)
        raise FileNotFoundError(f"Markdown file not found: {markdown_file}")
    if not markdown_file.endswith('.md'):
        logger.error("Invalid file type: %s", markdown_file)
        return
    command = ["pandoc", markdown_file, "-o", pdf_output]
    logger.info("Running command: %s", " ".join(command))
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; pandoc exited with code %d. Error: %s", result.returncode, result.stderr)
