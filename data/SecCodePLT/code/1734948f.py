"""
This function performs the task of transforming a markdown file into a PDF by using an external tool. The `pandoc` command-line utility is employed to handle this conversion.
"""
def convert_md_to_pdf(md_path: str, output_pdf_path: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(md_path):
        logger.error("Markdown file not found: %s", md_path)
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    if not md_path.endswith('.md'):
        logger.error("Invalid file type: %s", md_path)
        return
    command = f"pandoc {md_path} -o {output_pdf_path}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)