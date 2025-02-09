    type_to_update = self.prepare_new_asset_type()
    type_to_update.theName = 'Edited test asset type'
    json_dict = {'session_id': 'test', 'object': type_to_update}
    upd_type_body = jsonpickle.encode(json_dict)
    rv = self.app.put('/api/assets/types/name/%s?session_id=test' % quote(self.prepare_new_asset_type().theName), data=upd_type_body, content_type='application/json')
    if (sys.version_info > (3,)):
      putResponse = rv.data.decode('utf-8')
    else:
      putResponse = rv.data
    self.assertIsNotNone(rv.data, 'No response')
    json_resp = jsonpickle.decode(putResponse)
    self.assertIsNotNone(json_resp)
    self.assertIsInstance(json_resp, dict)
    message = json_resp.get('message', None)
    self.assertIsNotNone(message, 'No message in response')
    self.logger.info('[%s] Message: %s', method, message)
    self.assertEqual(message,'Edited test asset type updated')

    rv = self.app.get('/api/assets/types/name/%s?session_id=test' % quote(type_to_update.theName))
    if (sys.version_info > (3,)):