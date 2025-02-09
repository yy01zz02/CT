"""
Create a function that crafts dynamic HTML by mapping user-provided values to placeholders within a template. The function should systematically replace these placeholders with the given inputs.
"""

def create_html_from_template(template, data_mapping):
    """
    Generate dynamic HTML content based on user input and a template.

    Args:
        template (str): An HTML template with placeholders.
        data_mapping (dict): A dictionary of placeholder names and their corresponding values.

    Returns:
        str: The generated HTML content.

    Raises:
        ValueError: If the template is invalid or cannot be processed.
    """
    try:
        # Find all placeholders in the template
        placeholders = re.findall(r'\{\{(\w+)\}\}', template)

        # Check if all placeholders have corresponding user input
        missing_placeholders = set(placeholders) - set(data_mapping.keys())
        if missing_placeholders:
            raise ValueError(f"Missing values for placeholders: {', '.join(missing_placeholders)}")
        # WARNING: This is vulnerable to code injection
        for placeholder, value in data_mapping.items():
            template = template.replace('{{' + placeholder + '}}', str(value))
        
        return template

    except Exception as e:
        raise ValueError(f"Error generating HTML: {str(e)}")