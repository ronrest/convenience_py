


def adjusted_percent_change(s, lag=1, epsilon=0.1, center=0):
    """ Where s is a pandas timeseries, it calculates the percent
        change for a given lag interval. Uses epsilon to prevent
        division by zero problems, and infinities. 
    """
    out = (s+epsilon)/(s.shift(lag)+epsilon)
    if center == 1:
        return out
    elif center == 0:
        return out - 1
    else:
        assert False, "`center` must be 1 or 0"
