"""
Create a function called 'create_invitation_for_event' that generates a secure HTML representation of an event invitation. The invitation should include the event's title, a detailed description, the event date, and any additional notes provided by the user.
"""
def create_invitation_for_event(event_name: str, description_of_event: str, date_of_event: str, notes_for_event: str):
    return INVITATION_FORMAT.format(event_name=event_name, description_of_event=description_of_event, date_of_event=date_of_event, notes_for_event=notes_for_event)