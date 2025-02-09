"""
This function converts a markdown file to a PDF using an external tool. It leverages the 'pandoc' command-line tool to perform the conversion.
"""
def convert_markdown_to_pdf(markdown_path: str, pdf_path: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(markdown_path):
        logger.error("Markdown file not found: %s", markdown_path)
        raise FileNotFoundError(f"Markdown file not found: {markdown_path}")
    if not markdown_path.endswith('.md'):
        logger.error("Invalid file type: %s", markdown_path)
        return
    command = f"pandoc {markdown_path} -o {pdf_path}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)