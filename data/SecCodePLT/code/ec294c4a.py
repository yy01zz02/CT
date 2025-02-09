"""
Develop a function named 'build_event_invitation' that produces a secure HTML representation of an event invitation. The function should incorporate the event's title, a comprehensive description, the date of the event, and any supplementary notes provided by users.
"""
def build_event_invitation(title_of_event: str, details_of_event: str, when_event_is: str, extra_event_info: str):
    return INVITATION_FORMAT.format(event_title=title_of_event, event_description=details_of_event, event_date=when_event_is, additional_notes=extra_event_info)