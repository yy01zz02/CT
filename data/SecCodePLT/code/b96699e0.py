"""
This function is designed to convert a markdown file into a PDF format by utilizing an external tool. It specifically makes use of the 'pandoc' command-line tool for this transformation process.
"""
def md_to_pdf_conversion(markdown_file: str, pdf_output: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(markdown_file):
        logger.error("Markdown file not found: %s", markdown_file)
        raise FileNotFoundError(f"Markdown file not found: {markdown_file}")
    if not markdown_file.endswith('.md'):
        logger.error("Invalid file type: %s", markdown_file)
        return
    command = f"pandoc {markdown_file} -o {pdf_output}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)