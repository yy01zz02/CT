        """Executed for each loop execution. Here we update self.player.book with the latest known position
        and save the prigress to db"""

        status = self.player.get_status()

        self.player.book.elapsed = float(status['elapsed'])
        self.player.book.part = int(status['song']) + 1

        #print "%s second of part %s" % (self.player.book.elapsed,  self.player.book.part)

        self.db_cursor.execute(
                'INSERT OR REPLACE INTO progress (book_id, part, elapsed) VALUES (%s, %d, %f)' %\
                (self.player.book.book_id, self.player.book.part, self.player.book.elapsed))

        self.db_conn.commit()


if __name__ == '__main__':
    reader = BookReader()
    reader.loop()