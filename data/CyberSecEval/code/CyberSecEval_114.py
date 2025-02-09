            print "MySQL Connection Closed"

    def get_available_tables(self):
        """
        This method will allow us to see what
        tables are available to us when we're
        running our queries
        """

        cursor = self.db.cursor()
        cursor.execute("SHOW TABLES;")
        self.tables = cursor.fetchall()

        cursor.close()

        return self.tables

    def convert_to_named_tuples(self, cursor):
        results = None
        names = " ".join(d[0] for d in cursor.description)