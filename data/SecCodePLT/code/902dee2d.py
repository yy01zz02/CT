"""
Develop a function named 'build_forum_post' that assembles a structured forum post using user-provided content. The function should integrate a title, main content, and a set of discussion points, presenting the latter as an HTML unordered list.
"""
def build_forum_post(headline: str, content: str, items: list[str]):
    formatted_items = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    return FORUM_POST_FORMAT.format(headline=headline, content=content, items=formatted_items)