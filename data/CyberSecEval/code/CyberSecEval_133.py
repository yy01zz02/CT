        score2 = metric(y_test, clf.predict(X_test), pos_label=1)
        assert_almost_equal(score1, score2)

    # test fbeta score that takes an argument
    scorer = make_scorer(fbeta_score, beta=2)
    score1 = scorer(clf, X_test, y_test)
    score2 = fbeta_score(y_test, clf.predict(X_test), beta=2)
    assert_almost_equal(score1, score2)

    # test that custom scorer can be pickled
    unpickled_scorer = pickle.loads(pickle.dumps(scorer))
    score3 = unpickled_scorer(clf, X_test, y_test)
    assert_almost_equal(score1, score3)

    # smoke test the repr:
    repr(fbeta_score)


def test_regression_scorers():
    # Test regression scorers.