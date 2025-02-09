    self.logger.info('[%s] Object to delete: %s', method, new_asset_type_body)
    self.app.post('/api/assets/types', content_type='application/json', data=new_asset_type_body)
    self.logger.info('[%s] URL: %s', method, url)
    rv = self.app.delete(url)
    if (sys.version_info > (3,)):
      delResponse = rv.data.decode('utf-8')
    else:
      delResponse = rv.data
    self.logger.info('[%s] Response data: %s', method, delResponse)
    self.assertIsNotNone(delResponse, 'No response')
    json_resp = jsonpickle.decode(delResponse)
    self.assertIsInstance(json_resp, dict, 'The response cannot be converted to a dictionary')
    message = json_resp.get('message', None)
    self.assertIsNotNone(message, 'No message in response')
    self.assertEqual(message,'Test asset type deleted')

  def test_types_post(self):
    method = 'test_types_post'
    url = '/api/assets/types'
    self.logger.info('[%s] URL: %s', method, url)