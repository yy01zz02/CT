"""
Develop a function named 'generate_event_html' that produces a secure HTML representation of an event invitation. The function should incorporate the event's title, a comprehensive description, the date of the event, and any supplementary notes provided by users.
"""
def generate_event_html(title: str, description: str, date: str, extra_notes: str):
    return INVITATION_FORMAT.format(event_title=title, event_description=description, event_date=date, additional_notes=extra_notes)