                  dtype=[('a', int), ('b', float)])
        a_pickled = pickle.loads(a.dumps())
        assert_equal(a_pickled._mask, a._mask)
        assert_equal(a_pickled, a)

    def test_pickling_keepalignment(self):
        # Tests pickling w/ F_CONTIGUOUS arrays
        a = arange(10)
        a.shape = (-1, 2)
        b = a.T
        test = pickle.loads(pickle.dumps(b))
        assert_equal(test, b)

    def test_single_element_subscript(self):
        # Tests single element subscripts of Maskedarrays.
        a = array([1, 3, 2])
        b = array([1, 3, 2], mask=[1, 0, 1])
        assert_equal(a[0].shape, ())
        assert_equal(b[0].shape, ())
        assert_equal(b[1].shape, ())