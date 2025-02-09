        if self.return_value == None:
            if (line not in self.storage_blacklist) and self.command_not_blank(line):
                self.store_to_script(line)
                print "Stored!"

    def default(self, line):
        """
        This is the default method that is called if the shell command is not
        a specific shell command (a do_ method_)
        """
        cmd_file = os.popen(line)
        output = cmd_file.read()
        self.return_value = cmd_file.close()
        if self.return_value != None:
            if self.alert_type == 'text':
                self.send_text(line)
            if self.alert_type == 'call':
                self.send_call()
        if self.command_not_blank(line):
            print output