
    self.assertAllEqual(self.evaluate(x), 2)

  def test_converted_call_exec_generated_code(self):

    temp_mod = imp.new_module('test_module')
    dynamic_code = """
      def foo(x):
        return x + 1
    """
    exec(textwrap.dedent(dynamic_code), temp_mod.__dict__)  # pylint:disable=exec-used
    opts = converter.ConversionOptions(optional_features=None)

    x = api.converted_call(temp_mod.foo, opts, (1,), {})

    self.assertAllEqual(x, 2)

  def test_converted_call_namedtuple(self):

    opts = converter.ConversionOptions(recursive=True)