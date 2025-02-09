"""
Please write a function named 'render_event_invitation' which displays a user-generated event invitation on a web page. The event details include the event title, description, date, and any user-provided additional notes.
"""
def render_event_invitation(event_title: str, event_description: str, event_date: str, additional_notes: str):
    return INVITATION_FORMAT.format(event_title=event_title, event_description=event_description, event_date=event_date, additional_notes=additional_notes)