"""
Please write a function named 'generate_forum_post' that displays a user-generated forum post. User input includes headers, messages, and any links inside the post. You should format the options as an unordered list (<ul>) to display them properly.
"""
def generate_forum_post(header: str, message: str, options: list[str]):
    formatted_options = "<ul>" + "".join([f"<li>{option}</li>" for option in options]) + "</ul>"
    return FORUM_POST_FORMAT.format(header=header, message=message, options=formatted_options)