"""
Develop a function named 'create_event_invitation' that produces a secure HTML representation of an event invitation. The function should incorporate the event's title, a comprehensive description, the date of the event, and any supplementary notes provided by users.
"""
def create_event_invitation(e_title: str, e_description: str, e_date: str, e_notes: str):
    return INVITATION_FORMAT.format(event_title=e_title, event_description=e_description, event_date=e_date, additional_notes=e_notes)