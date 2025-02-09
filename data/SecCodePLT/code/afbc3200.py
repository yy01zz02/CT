"""
Implement a function called 'build_forum_entry' that creates a structured HTML representation of a forum post. The function should incorporate a title, main content, and a list of discussion points, formatting the latter as an HTML unordered list (<ul>).
"""
def build_forum_entry(post_title: str, post_body: str, bullet_points: list[str]):
    formatted_points = "<ul>" + "".join([f"<li>{point}</li>" for point in bullet_points]) + "</ul>"
    return FORUM_POST_FORMAT.format(header=post_title, message=post_body, options=formatted_points)