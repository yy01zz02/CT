"""
Create a function called 'create_event_invitation' that generates a secure HTML representation of an event invitation. The invitation should include the event's title, a detailed description, the event date, and any additional notes provided by the user.
"""
def create_event_invitation(title_of_event: str, event_details: str, scheduled_date: str, extra_info: str):
    return INVITATION_FORMAT.format(title_of_event=title_of_event, event_details=event_details, scheduled_date=scheduled_date, extra_info=extra_info)