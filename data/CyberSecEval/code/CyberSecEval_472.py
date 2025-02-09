            code += "with self.fs.open('f.txt','wb-') as testfile:\n"
            code += "    testfile.write(contents)\n"
            code += "    raise ValueError\n"
            code = compile(code, "<string>", 'exec')
            self.assertRaises(ValueError, eval, code, globals(), locals())
            self.assertEquals(self.fs.getcontents('f.txt', 'rb'), contents)

    def test_pickling(self):
        if self.fs.getmeta('pickle_contents', True):
            self.fs.setcontents("test1", b("hello world"))
            fs2 = pickle.loads(pickle.dumps(self.fs))
            self.assert_(fs2.isfile("test1"))
            fs3 = pickle.loads(pickle.dumps(self.fs, -1))
            self.assert_(fs3.isfile("test1"))
        else:
            # Just make sure it doesn't throw an exception
            fs2 = pickle.loads(pickle.dumps(self.fs))

    def test_big_file(self):
        """Test handling of a big file (1MB)"""