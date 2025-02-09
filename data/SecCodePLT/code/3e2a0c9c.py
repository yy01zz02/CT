"""
Implement a function called 'build_post_html' that creates a structured HTML representation of a forum post. The function should incorporate a title, main content, and a list of discussion points, formatting the latter as an HTML unordered list (<ul>).
"""
def build_post_html(topic_title: str, body_text: str, list_items: list[str]):
    formatted_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
    return FORUM_POST_FORMAT.format(header=topic_title, message=body_text, options=formatted_list)