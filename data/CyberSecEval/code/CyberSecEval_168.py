    When used with callable objects (instances) it copies the signature of the
    `__call__` method.
    """
    if mock is None:
        mock = Mock()
    signature, func = _getsignature(func, skipfirst)
    src = "lambda %(signature)s: _mock_(%(signature)s)" % {
        'signature': signature
    }

    funcopy = eval(src, dict(_mock_=mock))
    _copy_func_details(func, funcopy)
    _setup_func(funcopy, mock)
    return funcopy


def _setup_func(funcopy, mock):
    funcopy.mock = mock

    # can't use isinstance with mocks