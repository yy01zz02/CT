    def add_factory(id, factory):
        JsonObjectFactory.factories[id] = factory

    @staticmethod
    def create(id, data):
        for key in data:
            if key in KEYWORDS:
                new_key = key + "_"
                data[new_key] = data.pop(key)
        if id not in JsonObjectFactory.factories:
            JsonObjectFactory.add_factory(id, eval(id))
        return JsonObjectFactory.factories[id].factory(data)


class JsonObject(object):

    """ This is the base class for all HP SDN Client data types."""

    def __str__(self):
        return self.to_json_string()