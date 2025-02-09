    json_resp = json_deserialize(delResponse)
    self.assertIsNotNone(json_resp, 'No results after deserialization')
    message = json_resp.get('message', None)
    self.assertIsNotNone(message, 'No message returned')
    self.logger.info('[%s] Message: %s\n', method, message)

  def test_types_get(self):
    method = 'test_types_get'
    rv = self.app.get('/api/assets/types?session_id=test')
    if (sys.version_info > (3,)):
      assets = jsonpickle.decode(rv.data.decode('utf-8'))
    else:
      assets = jsonpickle.decode(rv.data)
    self.assertIsNotNone(assets, 'No results after deserialization')
    self.assertIsInstance(assets, list, 'The result is not a dictionary as expected')
    self.assertGreater(len(assets), 0, 'No assets in the dictionary')
    self.logger.info('[%s] Asset types found: %d', method, len(assets))
    asset_type = assets[0]
    self.logger.info('[%s] First asset types: %s\n', method, asset_type['theName'])
