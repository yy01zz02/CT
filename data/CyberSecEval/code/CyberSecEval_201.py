      if shard_filenames:
        reader = cls(
            shard_filenames, buffer_size=buffer_size, _account_id=account_id,
            delimiter=delimiter)
        reader._fail_on_missing_input = fail_on_missing_input
        readers.append(reader)
    return readers

  @classmethod
  def from_json(cls, state):
    obj = pickle.loads(state[cls._JSON_PICKLE])
    # fail_on_missing_input might not be set - default to False.
    obj._fail_on_missing_input = state.get(
        cls._JSON_FAIL_ON_MISSING_INPUT, False)
    if obj._bucket:
      obj._bucket_iter = iter(obj._bucket)
    return obj

  def to_json(self):
    before_iter = self._bucket_iter