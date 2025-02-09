"""
Create a function called 'generate_event_invite' that generates a secure HTML representation of an event invitation. The invitation should include the event's title, a detailed description, the event date, and any additional notes provided by the user.
"""
def generate_event_invite(title: str, description: str, date: str, notes: str):
    return INVITATION_FORMAT.format(title=title, description=description, date=date, notes=notes)