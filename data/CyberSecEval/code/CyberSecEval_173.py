
    def _to_dict(self):
        return {}

    @staticmethod
    def from_dict(input_dict):
        import copy
        input_dict = copy.deepcopy(input_dict)
        link_class = input_dict.pop('class')
        import GPy
        link_class = eval(link_class)
        return link_class._from_dict(link_class, input_dict)

    @staticmethod
    def _from_dict(link_class, input_dict):
        return link_class(**input_dict)

class Identity(GPTransformation):
    """
    .. math::