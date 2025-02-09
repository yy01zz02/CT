      input_arg: the input_arg field of an OpDef
                 (e.g. self._definition.signature.input_arg)
      output_arg: the output_arg field of an OpDef
                 (e.g. self._definition.signature.output_arg)
      node_def: the node_def field of a FunctionDef
                (e.g. self._definition.node_def)

    Returns:
      The unique string for this input
    """
    hasher = hashlib.sha1()

    def update_num(n):
      hasher.update(compat.as_bytes("%x" % n))

    def update_str(s):
      update_num(len(s))
      hasher.update(compat.as_bytes(s))

    def update_strs(slist):