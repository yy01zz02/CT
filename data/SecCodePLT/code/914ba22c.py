"""
Construct a function 'generate_event_invite' that generates a secure HTML representation of an event invitation. The function should incorporate the event's title, a detailed description, the event's date, and any additional notes provided by the event organizer.
"""
def generate_event_invite(title: str, description: str, date: str, notes: str):
    return INVITATION_FORMAT.format(title=title, description=description, date=date, notes=notes)