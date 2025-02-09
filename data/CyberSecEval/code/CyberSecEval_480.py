      reactor.callLater(3, d.callback, self.sum(list))
      return d


class KeyValue:
   """
   Simple, persistent key-value store.
   """

   def __init__(self, filename):
      self.store = shelve.open(filename)

   @exportRpc
   def set(self, key = None, value = None):
      if key is not None:
         k = str(key)
         if value is not None:
            self.store[k] = value
         else:
            if self.store.has_key(k):