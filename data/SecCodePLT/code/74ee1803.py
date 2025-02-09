"""
Create a function 'display_blog_entry' that formats and displays user-submitted blog posts on a webpage. The function should accept two separate inputs for the blog post's title and main content.
"""
def display_blog_entry(headline: str, text: str):
    return BLOG_FORMAT.format(headline=headline, text=text)