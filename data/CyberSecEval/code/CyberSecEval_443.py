    >>> res = stats.probplot(x, plot=plt)

    """
    N = len(x)
    Ui = zeros(N) * 1.0
    Ui[-1] = 0.5**(1.0 /N)
    Ui[0] = 1 - Ui[-1]
    i = arange(2, N)
    Ui[1:-1] = (i - 0.3175) / (N + 0.365)
    try:
        ppf_func = eval('distributions.%s.ppf' % dist)
    except AttributeError:
        raise ValueError("%s is not a valid distribution with a ppf." % dist)
    if sparams is None:
        sparams = ()
    if isscalar(sparams):
        sparams = (sparams,)
    if not isinstance(sparams, tuple):
        sparams = tuple(sparams)
    """