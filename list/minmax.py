
# ==============================================================================
#                                                                         ARGMAX
# ==============================================================================
def argmax(a):
    """ Given a list `a`, it returns the index of the max value. """
    return max(range(len(a)), key=lambda i: a[i])


def argmin(a):
    return min(range(len(a)), key=lambda i: a[i])


