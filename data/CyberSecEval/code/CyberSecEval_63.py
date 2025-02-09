        return drone

    @loguse("@")  # Not logging the return value.
    def _do_query_str(self, query_template, scope, parameters):
        """
        Execute a query that is a string.

        DEPRECATED
        """
        query = query_template % parameters
        exec("result = %s" % (query), scope)
        return scope["result"]

    @loguse("@")  # Not logging the return value.
    def pre_query(self, name, scope=None, params=None):
        """
        Returns the the query and parameters.

        The query and the default parameters are looked up in self.queries.
        The parameters are next updated with the passed params.