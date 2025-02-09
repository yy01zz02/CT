        except Exception, e:
            print e

    def sendNotification(self, message, start_time):
        try:
            end_time = datetime.datetime.now()
            diff_time_in_delta = end_time - start_time
            diff_time_in_mins = divmod(diff_time_in_delta.days * 86400 + diff_time_in_delta.seconds, 60)
            diff_time_msg = ' (Set ' + str(diff_time_in_mins[0]) + ' minutes ' + str(diff_time_in_mins[1]) + ' seconds ago)'
            if self.platform == 'Linux':
                os.system('notify-send "'+self.title+'" "'+message+'\r'+diff_time_msg+'"')
            elif self.platform == 'Windows':
                self.toaster.show_toast(self.title, message+'\n'+str(diff_time_msg), duration=300)
        except Exception, e:
            print e

def main():
    try:
        counter_flag = True
        notify = Notify()