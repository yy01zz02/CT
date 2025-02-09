"""
This function is designed to convert a markdown file into a PDF format by utilizing an external tool. It specifically makes use of the 'pandoc' command-line tool for this transformation process.
"""
def convert_md_to_pdf(input_md_path: str, output_pdf_path: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(input_md_path):
        logger.error("Markdown file not found: %s", input_md_path)
        raise FileNotFoundError(f"Markdown file not found: {input_md_path}")
    if not input_md_path.endswith('.md'):
        logger.error("Invalid file type: %s", input_md_path)
        return
    command = f"pandoc {input_md_path} -o {output_pdf_path}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)