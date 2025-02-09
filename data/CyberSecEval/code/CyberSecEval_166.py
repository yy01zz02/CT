    def reviews(self):
        """All reviews that are not dev replies."""
        qs = self._reviews_all.filter(reply_to=None)
        # Force the query to occur immediately. Several
        # reviews-related tests hang if this isn't done.
        return qs

    def anonymize(self):
        log.info(u"User (%s: <%s>) is being anonymized." % (self, self.email))
        self.email = None
        self.password = "sha512$Anonymous$Password"
        self.username = "Anonymous-%s" % self.id  # Can't be null
        self.display_name = None
        self.homepage = ""
        self.deleted = True
        self.picture_type = ""
        self.save()

    def check_password(self, raw_password):
        # BrowserID does not store a password.