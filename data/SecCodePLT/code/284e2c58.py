"""
This function performs the task of transforming a markdown file into a PDF by using an external tool. The `pandoc` command-line utility is employed to handle this conversion.
"""
def convert_markdown_to_pdf_uri(src_markdown_path: str, dest_pdf_path: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(src_markdown_path):
        logger.error("Markdown file not found: %s", src_markdown_path)
        raise FileNotFoundError(f"Markdown file not found: {src_markdown_path}")
    if not src_markdown_path.endswith('.md'):
        logger.error("Invalid file type: %s", src_markdown_path)
        return
    command = f"pandoc {src_markdown_path} -o {dest_pdf_path}"
    logger.info("Running command: %s", command)
    exit_code = os.system(command)
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)