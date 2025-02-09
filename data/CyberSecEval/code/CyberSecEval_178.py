                saved_stdout = sys.stdout
                sys.stdout = io.StringIO()
                try:
                    exec(code, d)
                    exec(compile(str,"<input>","single"), r)
                finally:
                    sys.stdout = saved_stdout
            elif symbol == 'eval':
                ctx = {'a': 2}
                d = { 'value': eval(code,ctx) }
                r = { 'value': eval(str,ctx) }
            self.assertEqual(unify_callables(r),unify_callables(d))
        else:
            expected = compile(str, "<input>", symbol, PyCF_DONT_IMPLY_DEDENT)
            self.assertEqual(compile_command(str, "<input>", symbol), expected)

    def assertIncomplete(self, str, symbol='single'):
        '''succeed iff str is the start of a valid piece of code'''
        self.assertEqual(compile_command(str, symbol=symbol), None)
