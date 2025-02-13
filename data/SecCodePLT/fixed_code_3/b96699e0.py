import subprocess  # nosec B404
import os

def md_to_pdf_conversion(markdown_file: str, pdf_output: str):
    """Converts a markdown file to a PDF using pandoc."""
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(markdown_file):
        logger.error("Markdown file not found: %s", markdown_file)
        raise FileNotFoundError(f"Markdown file not found: {markdown_file}")
    if not markdown_file.endswith('.md'):
        logger.error("Invalid file type: %s", markdown_file)
        raise ValueError("Input file must be a Markdown file (.md)")
    if not pdf_output.endswith('.pdf'):
        logger.error("Invalid output file type: %s", pdf_output)
        raise ValueError("Output file must be a PDF (.pdf)")
    output_dir = os.path.dirname(pdf_output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    command = ["pandoc", "--", markdown_file, "-o", pdf_output]
    logger.info("Running command: %s", " ".join(command))
    result = subprocess.run(command)  # nosec B603
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d.", exit_code)
        raise RuntimeError(f"Pandoc conversion failed with exit code {exit_code}")
