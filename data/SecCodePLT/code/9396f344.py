"""
This function takes a markdown file and converts it into a PDF format by executing the 'pandoc' tool. The conversion is handled by running the system's 'pandoc' command-line utility.
"""
def markdown_to_pdf(md_path: str, pdf_dest: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(md_path):
        logger.error("Markdown file not found: %s", md_path)
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    if not md_path.endswith('.md'):
        logger.error("Invalid file type: %s", md_path)
        return
    command = f"pandoc {md_path} -o {pdf_dest}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)