        return results

    def get_columns_for_table(self, table_name):
        """
        This method will enable us to interact
        with our database to find what columns
        are currently in a specific table
        """

        cursor = self.db.cursor()
        cursor.execute("SHOW COLUMNS FROM `%s`" % table_name)
        self.columns = cursor.fetchall()

        cursor.close()

        return self.columns

    def select(self, table, columns=None, named_tuples=False, **kwargs):
        """
        We'll create our `select` method in order