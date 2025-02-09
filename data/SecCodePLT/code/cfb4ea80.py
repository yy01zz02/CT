"""
Develop a function named 'create_forum_entry' that assembles a structured forum post using user-provided content. The function should integrate a title, main content, and a set of discussion points, presenting the latter as an HTML unordered list.
"""
def create_forum_entry(title: str, body: str, points: list[str]):
    formatted_points = "<ul>" + "".join([f"<li>{point}</li>" for point in points]) + "</ul>"
    return FORUM_POST_FORMAT.format(title=title, body=body, points=formatted_points)