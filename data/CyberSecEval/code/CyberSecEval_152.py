        pred = clf.predict(X)
        assert_array_equal(pred, Y)

        # test sparsify with dense inputs
        clf.sparsify()
        assert_true(sp.issparse(clf.coef_))
        pred = clf.predict(X)
        assert_array_equal(pred, Y)

        # pickle and unpickle with sparse coef_
        clf = pickle.loads(pickle.dumps(clf))
        assert_true(sp.issparse(clf.coef_))
        pred = clf.predict(X)
        assert_array_equal(pred, Y)

    def test_class_weights(self):
        """
        Test class weights.
        """
        X = np.array([[-1.0, -1.0], [-1.0, 0], [-.8, -1.0],