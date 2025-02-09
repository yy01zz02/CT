      postResponse = rv.data
    self.logger.debug('[%s] Response data: %s', method, postResponse)
    json_resp = jsonpickle.decode(postResponse)
    self.assertIsNotNone(json_resp, 'No results after deserialization')
    ackMsg = json_resp.get('message', None)
    self.assertEqual(ackMsg,'Test asset type created')

    rv = self.app.delete('/api/assets/types/name/%s?session_id=test' % quote(self.prepare_new_asset_type().theName))
    delResponse = rv.data.decode('utf-8')
    self.assertIsNotNone(delResponse, 'No response')
    json_resp = jsonpickle.decode(delResponse)
    self.assertIsInstance(json_resp, dict, 'The response cannot be converted to a dictionary')
    message = json_resp.get('message', None)
    self.assertIsNotNone(message, 'No message in response')
    self.assertEqual(message,'Test asset type deleted')

  def test_types_put(self):
    method = 'test_types_put'
    url = '/api/assets/types'
    self.logger.info('[%s] URL: %s', method, url)