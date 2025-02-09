        return osm, osr

def ppcc_max(x, brack=(0.0,1.0), dist='tukeylambda'):
    """Returns the shape parameter that maximizes the probability plot
    correlation coefficient for the given data to a one-parameter
    family of distributions.

    See also ppcc_plot
    """
    try:
        ppf_func = eval('distributions.%s.ppf'%dist)
    except AttributeError:
        raise ValueError("%s is not a valid distribution with a ppf." % dist)
    """
    res = inspect.getargspec(ppf_func)
    if not ('loc' == res[0][-2] and 'scale' == res[0][-1] and \
            0.0==res[-1][-2] and 1.0==res[-1][-1]):
        raise ValueError("Function has does not have default location "
              "and scale parameters\n  that are 0.0 and 1.0 respectively.")
    if (1 < len(res[0])-len(res[-1])-1) or \