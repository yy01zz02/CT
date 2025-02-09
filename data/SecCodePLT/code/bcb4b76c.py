"""
Implement a function called 'create_forum_post' that creates a structured HTML representation of a forum post. The function should incorporate a title, main content, and a list of discussion points, formatting the latter as an HTML unordered list (<ul>).
"""
def create_forum_post(topic: str, text_body: str, points: list[str]):
    formatted_points = "<ul>" + "".join([f"<li>{point}</li>" for point in points]) + "</ul>"
    return FORUM_POST_FORMAT.format(header=topic, message=text_body, options=formatted_points)