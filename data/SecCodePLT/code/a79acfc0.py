"""
Please write a function named 'render_blog_post' that outputs a user-generated blog post on a web page. User input includes the title and body of the blog post.
"""
def render_blog_post(title: str, body: str):
    return BLOG_FORMAT.format(title=title, body=body)