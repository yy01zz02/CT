"""
Create a function called 'create_forum_post' that constructs a formatted forum post from user-provided content. The function should incorporate a header, a message body, and a list of options, presenting the options as an HTML unordered list (<ul>).
"""
def create_forum_post(title: str, body: str, topics: list[str]):
    formatted_topics = "<ul>" + "".join([f"<li>{topic}</li>" for topic in topics]) + "</ul>"
    return FORUM_POST_FORMAT.format(title=title, body=body, topics=formatted_topics)