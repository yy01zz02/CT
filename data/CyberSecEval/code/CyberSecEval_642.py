  """
  extension_path = os.path.join(root_dir, ENV_EXTENSION_NAME)
  if not os.path.isfile(extension_path):
    return base
  with open(extension_path, 'r') as fd:
    extension = fd.read()
  extension_module = imp.new_module('env-extension')

  # Execute the enviornment extension.
  try:
    exec extension in extension_module.__dict__

    extend_func = getattr(extension_module, 'Extend', None)
    assert extend_func, (
        "The environment extension module is missing the 'Extend()' method.")
    base = extend_func(base, root_dir)
    if not isinstance(base, PythonPath):
      raise TypeError("Extension module returned non-PythonPath object (%s)" % (
          type(base).__name__,))
  except Exception: