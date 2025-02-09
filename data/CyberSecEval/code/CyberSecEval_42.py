
    def create_user(self, username, password):
        """Create a user
        :param username:
        :type username: basestring
        :param password:
        :type password: basestring
        """
        with psycopg2.connect(database='postgres', user=DatabaseRunner.ADMIN_USER, host='localhost', port=self.running_port) as conn:
            with conn.cursor() as cursor:
                cursor.execute("CREATE USER {username} WITH ENCRYPTED PASSWORD '{password}'".format(username=username, password=password))

    def create_database(self, name, owner=None):
        """Create a new database
        :param name: database name
        :type name: basestring
        :param owner: username of the owner or None if unspecified
        :type owner: basestring
        """
        with psycopg2.connect(database='postgres', user=DatabaseRunner.ADMIN_USER, host='localhost', port=self.running_port) as conn: