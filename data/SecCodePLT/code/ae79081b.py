"""
Construct a function 'prepare_event_details' that generates a secure HTML representation of an event invitation. The function should incorporate the event's title, a detailed description, the event's date, and any additional notes provided by the event organizer.
"""
def prepare_event_details(headline: str, summary: str, scheduled_date: str, additional_info: str):
    return INVITATION_FORMAT.format(headline=headline, summary=summary, scheduled_date=scheduled_date, additional_info=additional_info)