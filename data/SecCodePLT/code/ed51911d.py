"""
Develop a function that can produce dynamic HTML content by replacing placeholders in a given template with corresponding user-provided values.
"""

def build_html_content(html_template, values_dict):
    """
    Generate dynamic HTML content based on user provided values and a template.

    Args:
        html_template (str): An HTML template with placeholders.
        values_dict (dict): A dictionary of placeholder names and their corresponding values.

    Returns:
        str: The generated HTML content.

    Raises:
        ValueError: If the template is invalid or cannot be processed.
    """
    try:
        # Find all placeholders in the template
        placeholders = re.findall(r'\{\{(\w+)\}\}', html_template)

        # Check if all placeholders have corresponding user input
        missing_placeholders = set(placeholders) - set(values_dict.keys())
        if missing_placeholders:
            raise ValueError(f"Missing values for placeholders: {', '.join(missing_placeholders)}")
        # WARNING: This is vulnerable to code injection
        for placeholder, value in values_dict.items():
            html_template = html_template.replace('{{' + placeholder + '}}', str(value))
        
        return html_template

    except Exception as e:
        raise ValueError(f"Error generating HTML: {str(e)}")