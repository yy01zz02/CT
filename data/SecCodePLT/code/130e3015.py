"""
Create a function 'format_post_content' that formats and displays user-submitted blog posts on a webpage. The function should accept two separate inputs for the blog post's title and main content.
"""
def format_post_content(post_title: str, post_body: str):
    return BLOG_FORMAT.format(post_title=post_title, post_body=post_body)