        first_log_time = None

        from droidbot.state_monitor import StateMonitor
        state_monitor = StateMonitor()
        state_monitor.start()

        while self.enabled:
            try:
                if self.output_dir and (time.time() - self.lastScreenshot) >=5:
                    # Take screenshots every 5 seconds.
                    os.system("adb shell screencap -p | sed 's/\r$//' > %s" % os.path.join(self.output_dir, "screen") \
                              + "_$(date +%Y-%m-%d_%H%M%S).png")
                    self.lastScreenshot = time.time()

                logcatInput = self.adb.stdout.readline()
                if not logcatInput:
                    raise LostADBException("We have lost the connection with ADB.")

                from droidbot import utils
                log_data = utils.parse_log(logcatInput)