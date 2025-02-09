        """Create a new database
        :param name: database name
        :type name: basestring
        :param owner: username of the owner or None if unspecified
        :type owner: basestring
        """
        with psycopg2.connect(database='postgres', user=DatabaseRunner.ADMIN_USER, host='localhost', port=self.running_port) as conn:
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with conn.cursor() as cursor:
                sql = 'CREATE DATABASE {name} ' + ('WITH OWNER {owner}' if owner else '')
                cursor.execute(sql.format(name=name, owner=owner))

    def shutdown(self):
        """
        Shutdown postgres and remove the data directory
        """
        # stop pg
        try:
            logger.debug('Killing postgres on port {port}'.format(port=self.running_port))
            self.proc.kill()