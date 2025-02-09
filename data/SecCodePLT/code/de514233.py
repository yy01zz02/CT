"""
Implement a function called 'show_blog_post' that displays a user-submitted blog post on a webpage. The function should take the blog post's title and content as inputs.
"""
def show_blog_post(headline: str, text: str):
    return BLOG_FORMAT.format(headline=headline, text=text)