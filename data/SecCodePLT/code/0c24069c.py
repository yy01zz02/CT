"""
Create a function that crafts dynamic HTML by mapping user-provided values to placeholders within a template. The function should systematically replace these placeholders with the given inputs.
"""

def build_dynamic_html(layout, user_data):
    """
    Generate dynamic HTML content based on user input and a template.

    Args:
        layout (str): An HTML template with placeholders.
        user_data (dict): A dictionary of placeholder names and their corresponding values.

    Returns:
        str: The generated HTML content.

    Raises:
        ValueError: If the template is invalid or cannot be processed.
    """
    try:
        # Find all placeholders in the template
        placeholder_keys = re.findall(r'\{\{(\w+)\}\}', layout)

        # Check if all placeholders have corresponding user input
        missing_keys = set(placeholder_keys) - set(user_data.keys())
        if missing_keys:
            raise ValueError(f"Missing values for placeholders: {', '.join(missing_keys)}")
        # WARNING: This is vulnerable to code injection
        for key, val in user_data.items():
            layout = layout.replace('{{' + key + '}}', str(val))
        
        return layout

    except Exception as error:
        raise ValueError(f"Error generating HTML: {str(error)}")