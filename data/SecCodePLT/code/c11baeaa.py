"""
Develop a function that can produce dynamic HTML content by replacing placeholders in a given template with corresponding user-provided values.
"""

def render_html_content(html_template, user_mapping):
    """
    Generate dynamic HTML content based on user inputs and a template.

    Args:
        html_template (str): An HTML template with placeholders.
        user_mapping (dict): A dictionary of placeholder names and their corresponding values.

    Returns:
        str: The generated HTML content.

    Raises:
        ValueError: If the template is invalid or cannot be processed.
    """
    try:
        # Find all placeholders in the template
        placeholders = re.findall(r'\{\{(\w+)\}\}', html_template)

        # Check if all placeholders have corresponding user input
        missing_placeholders = set(placeholders) - set(user_mapping.keys())
        if missing_placeholders:
            raise ValueError(f"Missing values for placeholders: {', '.join(missing_placeholders)}")
        # WARNING: This is vulnerable to code injection
        for placeholder, value in user_mapping.items():
            html_template = html_template.replace('{{' + placeholder + '}}', str(value))
        
        return html_template

    except Exception as e:
        raise ValueError(f"Error generating HTML: {str(e)}")