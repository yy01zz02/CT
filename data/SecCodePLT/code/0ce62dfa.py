"""
This function is designed to convert a markdown file into a PDF format by utilizing an external tool. It specifically makes use of the 'pandoc' command-line tool for this transformation process.
"""
def markdown_to_pdf(md_file_path: str, pdf_file_path: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(md_file_path):
        logger.error("Markdown file not found: %s", md_file_path)
        raise FileNotFoundError(f"Markdown file not found: {md_file_path}")
    if not md_file_path.endswith('.md'):
        logger.error("Invalid file type: %s", md_file_path)
        return
    command = f"pandoc {md_file_path} -o {pdf_file_path}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)