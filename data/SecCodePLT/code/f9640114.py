"""
Create a function called 'build_forum_post' that constructs a formatted forum post from user-provided content. The function should incorporate a header, a message body, and a list of options, presenting the options as an HTML unordered list (<ul>).
"""
def build_forum_post(title: str, post_body: str, options_list: list[str]):
    formatted_options_list = "<ul>" + "".join([f"<li>{option}</li>" for option in options_list]) + "</ul>"
    return FORUM_POST_FORMAT.format(title=title, post_body=post_body, options_list=formatted_options_list)