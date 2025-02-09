            placeholder = placeholder % self.get_expression_column(value)

        return placeholder

    def _get_postgis_func(self, func):
        """
        Helper routine for calling PostGIS functions and returning their result.
        """
        # Close out the connection.  See #9437.
        with self.connection.temporary_connection() as cursor:
            cursor.execute('SELECT %s()' % func)
            return cursor.fetchone()[0]

    def postgis_geos_version(self):
        "Returns the version of the GEOS library used with PostGIS."
        return self._get_postgis_func('postgis_geos_version')

    def postgis_lib_version(self):
        "Returns the version number of the PostGIS library used with PostgreSQL."
        return self._get_postgis_func('postgis_lib_version')