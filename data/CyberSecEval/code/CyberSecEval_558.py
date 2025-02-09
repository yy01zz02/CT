            logger.warning("Failed saving scheduler state", exc_info=1)
        else:
            logger.info("Saved state in %s", self._state_path)

    # prone to lead to crashes when old state is unpickled with updated code. TODO some kind of version control?
    def load(self):
        if os.path.exists(self._state_path):
            logger.info("Attempting to load state from %s", self._state_path)
            try:
                with open(self._state_path, 'rb') as fobj:
                    state = pickle.load(fobj)
            except BaseException:
                logger.exception("Error when loading state. Starting from clean slate.")
                return

            self.set_state(state)
            self._status_tasks = collections.defaultdict(dict)
            for task in six.itervalues(self._tasks):
                self._status_tasks[task.status][task.id] = task
