  from devil.android import device_utils
  from devil.android import forwarder

  sys.path.insert(0, os.path.join(chrome_paths.GetSrc(), 'build', 'android'))
  import devil_chromium

ANDROID_TEST_HTTP_PORT = 2311
ANDROID_TEST_HTTPS_PORT = 2411

_EXPECTATIONS = {}
exec(compile(open(os.path.join(_THIS_DIR, 'test_expectations'), "rb").read(), \
  os.path.join(_THIS_DIR, 'test_expectations'), 'exec'), _EXPECTATIONS)


class BaseTestEnvironment(object):
  """Manages the environment java tests require to run."""

  def __init__(self, chrome_version='HEAD'):
    """Initializes a desktop test environment.
