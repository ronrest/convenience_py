
# ==============================================================================
#                                                                         ARGMAX
# ==============================================================================
def argmax(a):
    """ Given a list `a`, it returns the index of the max value. """
    return max(range(len(a)), key=lambda i: a[i])

