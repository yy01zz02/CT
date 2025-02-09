        stop_words = set()
        with open(PATH + "english_stopwords.txt") as stopwords:
            stop_words = set(word.strip().lower() for word in stopwords)

        self.english_words = english_words
        self.stop_words = stop_words

        if not os.path.isfile(PATH + 'categories.pickle'):
            scrape_wikipedia()

        categories = pickle.load(open(PATH + 'categories.pickle', 'rb'))

        # parse the html, turning it into a list of words
        # and removing stop words and non-dictionary words
        # we'll also collect all of the words so that we can make a map of
        # words to numbers

        all_words = set()
        # the category level
        for k, v in categories.iteritems():