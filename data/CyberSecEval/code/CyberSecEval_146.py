from coinbase.model import Order
from coinbase.model import Transaction
from coinbase.model import Transfer


# Hide all warning output.
warnings.showwarning = lambda *a, **k: None

# Dummy API key values for use in tests
api_key = 'fakeapikey'
api_secret = 'fakeapisecret'
client_id = 'fakeid'
client_secret = 'fakesecret'
access_token = 'fakeaccesstoken'
refresh_token = 'fakerefreshtoken'


class TestAccount(unittest2.TestCase):
  @hp.activate
  def test_delete(self):