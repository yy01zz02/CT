            self._error(code=404,s3code='NSB')
            return

        self.set_header('Date', '"%s"' % datetime.datetime.utcnow())
        self.finish()
        
    
class ObjectHandler(BaseRequestHandler):
    
    def _object_md5(self,bucket_object):
        object_md5 = hashlib.md5()
        object_md5.update(bucket_object)
        return object_md5.hexdigest()
    
    def _get_bucket_object(self,**kwargs):
        if '_id' in kwargs.keys():
            object_id = kwargs['_id']
            object_field = '_id'
        if 'object_name' in kwargs.keys():
            object_id = kwargs['object_name']