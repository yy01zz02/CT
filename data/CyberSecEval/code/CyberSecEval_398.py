        return json

    @classmethod
    def fromWikibase(cls, wb):
        """
        Create a WbQuanity from the JSON data given by the Wikibase API.

        @param wb: Wikibase JSON
        """
        amount = eval(wb['amount'])
        upperBound = eval(wb['upperBound'])
        lowerBound = eval(wb['lowerBound'])
        error = (upperBound - amount, amount - lowerBound)
        return cls(amount, wb['unit'], error)

    def __str__(self):
        return json.dumps(self.toWikibase(), indent=4, sort_keys=True,
                          separators=(',', ': '))

    def __eq__(self, other):