  def HasFailed(self):
    execution_failed = self.test.DidFail(self.output)
    if self.test.IsNegative():
      return not execution_failed
    else:
      return execution_failed


def KillProcessWithID(pid):
  if utils.IsWindows():
    os.popen('taskkill /T /F /PID %d' % pid)
  else:
    os.kill(pid, signal.SIGTERM)


MAX_SLEEP_TIME = 0.1
INITIAL_SLEEP_TIME = 0.0001
SLEEP_TIME_FACTOR = 1.25

SEM_INVALID_VALUE = -1