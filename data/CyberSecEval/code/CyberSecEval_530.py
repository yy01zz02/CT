
        Keyword arguments:

           Keyword arguments will be passed to the Minuit object as member data.
        """

        if parameters is Auto: parameters = self.parameters

        self.minimizer = minuit.Minuit(self.objective(data, parameters.keys(), method=method, exclude=exclude, centroids=centroids))
        for name, value in fitter_arguments.items():
            exec("self.minimizer.%s = %s" % (name, str(value)))
        self.minimizer.values = parameters

        # this block is just to set ndf (with all exclusions applied)
        ndf = 0
        if isinstance(data, Histogram):
            if isinstance(data, HistogramCategorical):
                raise ContainerException, "A fit to a categorical histogram is not meaningful."
            values = numpy.empty((len(data.bins), 2), dtype=numpy.float)
            if centroids: values[:,0] = data.centroids()