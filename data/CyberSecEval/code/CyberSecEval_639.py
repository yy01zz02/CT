        self.get_problem()
        # 実行
        self.execute()
        return

    #
    # 問題の詳細を取得
    #
    def get_problem(self):
        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM problem WHERE id={id};".format(id=self.packet['id']))
        self.record = cursor.fetchall()[0]
        cursor.close()
        return

    #
    # データを解析
    #
    def analyse_packet(self):
        from Crypto.Cipher import AES