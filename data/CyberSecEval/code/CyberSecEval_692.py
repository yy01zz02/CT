    message = json_resp.get('message', None)
    self.assertIsNotNone(message, 'No message in response')
    self.logger.info('[%s] Message: %s', method, message)
    self.assertEqual(message,'Edited test asset type updated')

    rv = self.app.get('/api/assets/types/name/%s?session_id=test' % quote(type_to_update.theName))
    if (sys.version_info > (3,)):
      getResponse = rv.data.decode('utf-8')
    else:
      getResponse = rv.data
    upd_asset_type = jsonpickle.decode(getResponse)
    self.assertIsNotNone(upd_asset_type, 'Unable to decode JSON data')
    self.logger.debug('[%s] Response data: %s', method, getResponse)
    self.logger.info('[%s] Asset type: %s\n', method, upd_asset_type['theName'])

    rv = self.app.delete('/api/assets/types/name/%s?session_id=test' % quote(type_to_update.theName))

  def prepare_new_asset_type(self):
    new_type = ValueType(
                 valueTypeId=-1,