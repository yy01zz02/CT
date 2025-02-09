        else:
            columns = {info.name for info in self.get_table_description(cursor, table_name)}
            constraints.update(self._parse_table_constraints(table_schema, columns))

        # Get the index info
        cursor.execute("PRAGMA index_list(%s)" % self.connection.ops.quote_name(table_name))
        for row in cursor.fetchall():
            # SQLite 3.8.9+ has 5 columns, however older versions only give 3
            # columns. Discard last 2 columns if there.
            number, index, unique = row[:3]
            cursor.execute(
                "SELECT sql FROM sqlite_master "
                "WHERE type='index' AND name=%s" % self.connection.ops.quote_name(index)
            )
            # There's at most one row.
            sql, = cursor.fetchone() or (None,)
            # Inline constraints are already detected in
            # _parse_table_constraints(). The reasons to avoid fetching inline
            # constraints from `PRAGMA index_list` are:
            # - Inline constraints can have a different name and information