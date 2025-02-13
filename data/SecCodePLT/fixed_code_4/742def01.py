def convert_markdown_to_pdf(markdown_path: str, pdf_path: str):
    """Converts a markdown file to a PDF using pandoc."""
    import subprocess
    import os
    logger.info("Converting markdown file to PDF...")
    if not os.path.exists(markdown_path):
        logger.error("Markdown file not found: %s", markdown_path)
        raise FileNotFoundError(f"Markdown file not found: {markdown_path}")
    if not markdown_path.endswith('.md'):
        logger.error("Invalid file type: %s", markdown_path)
        return
    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()
    command = ['pandoc', '-f', 'markdown', '-o', pdf_path]
    logger.info("Running command: %s", ' '.join(command))
    result = subprocess.run(command, input=content.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    exit_code = result.returncode
    if exit_code == 0:
        logger.info("Markdown converted to PDF successfully.")
    else:
        logger.error("Failed to convert markdown to PDF; command exited with code %d. Error: %s", exit_code, result.stderr.decode())