    )
    categories = ParentalManyToManyField(EventCategory, blank=True)

    search_fields = [
        index.SearchField('get_audience_display'),
        index.SearchField('location'),
        index.SearchField('body'),
        index.FilterField('url_path'),
    ]

    password_required_template = 'tests/event_page_password_required.html'
    base_form_class = EventPageForm


EventPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date_from'),
    FieldPanel('date_to'),
    FieldPanel('time_from'),
    FieldPanel('time_to'),