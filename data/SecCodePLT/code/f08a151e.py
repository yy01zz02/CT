"""
Develop a function that belongs to an HTML parsing module, which is responsible for extracting HTML tags from a provided string using a regular expression. The function needs to return a list of tags identified in the input string.
"""
def get_html_tags(html_input):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(html_input)