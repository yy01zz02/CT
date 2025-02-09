        1. Stop playback of the current book if one is playing
        2. Start playing
        """

        while True:
            if self.player.is_playing():
                self.on_playing()
            elif self.player.finished_book():
                # when at the end of a book, delete its progress from the db
                # so we can listen to it again
                self.db_cursor.execute(
                    'DELETE FROM progress WHERE book_id = %d' % self.player.book.book_id)
                self.db_conn.commit()
                self.player.book.reset()

            rfid_card = self.rfid_reader.read()

            if not rfid_card:
                continue
    