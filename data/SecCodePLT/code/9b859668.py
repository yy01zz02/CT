"""
Create a function called 'construct_forum_content' that constructs a formatted forum post from user-provided content. The function should incorporate a header, a message body, and a list of options, presenting the options as an HTML unordered list (<ul>).
"""
def construct_forum_content(heading: str, content: str, choices: list[str]):
    formatted_choices = "<ul>" + "".join([f"<li>{choice}</li>" for choice in choices]) + "</ul>"
    return FORUM_POST_FORMAT.format(heading=heading, content=content, choices=formatted_choices)