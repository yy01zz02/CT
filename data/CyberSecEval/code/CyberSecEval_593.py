        def get_Login_input(self, parent):
            var = dbConnect()
            dbconn = mysql.connect(host=var.host, user=var.user, password=var.password, db=var.db)
            cur = dbconn.cursor()  # Cursor object - required to execute all queries

            cur.execute("SELECT username FROM playerinfo WHERE username = '%s' AND password = '%s'" % (entry_user.get(), entry_pass.get()))

            rows = cur.fetchall()

            if rows:
                cur.execute("SELECT firstname, lastname, username FROM playerinfo WHERE username = '%s' AND password = '%s'" % (entry_user.get(), entry_pass.get()))
                for namerow in cur.fetchall():  # print all the first cell
                    fn = namerow[0] #store firstname
                    ln = namerow[1] #store lastname
                    user = namerow[2]

                self.destroy()
                parent.destroy()
                go_to_HomePage(user)
                '''top = Toplevel(self)