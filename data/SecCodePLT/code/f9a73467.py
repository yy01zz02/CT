"""
Develop a function named 'compile_post' that assembles a structured forum post using user-provided content. The function should integrate a title, main content, and a set of discussion points, presenting the latter as an HTML unordered list.
"""
def compile_post(subject: str, text: str, highlights: list[str]):
    formatted_highlights = "<ul>" + "".join([f"<li>{highlight}</li>" for highlight in highlights]) + "</ul>"
    return FORUM_POST_FORMAT.format(subject=subject, text=text, highlights=formatted_highlights)