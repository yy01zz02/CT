        with self.raises(space, "ArgumentError", "marshal data too short"):
            space.execute("Marshal.load('')")

    def test_parameters(self, space):
        with self.raises(space, "TypeError", "instance of IO needed"):
            space.execute("Marshal.load(4)")

    def test_io(self, space, tmpdir):
        f = tmpdir.join("testfile")

        w_res = space.execute("""
        Marshal.dump('hallo', File.new('%s', 'wb'))
        file = File.open('%s', 'rb')
        return Marshal.load(file.read)
        """ % (f, f))
        assert space.str_w(w_res) == "hallo"

        w_res = space.execute("""
        Marshal.dump('hallo', File.new('%s', 'wb'))
        file = File.open('%s', 'rb')