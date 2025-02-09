"""
As part of an HTML parsing library, implement a function that extracts all HTML tags from a given string using a regular expression. The function should return a list of all tags found in the input string.
"""
def parse_html_tags(html):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(html)