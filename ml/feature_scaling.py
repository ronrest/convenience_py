import numpy as np

def minmax_scaling(x, min=None, max=None):
    """

    :param x:
        the 1D array
    :param min: (default = None)
        The min value to use for scaling.
        If None, then it automatically uses teh min of the array provided
    :param max:
        The max value to use for scaling
        If None, then it automatically uses the max of the array provided
    :return:
        An array with all the values scaled
    """
    x = np.array(x)
    xmax = x.max() if max is None else max
    xmin = x.min() if min is None else min
    denominator = xmax - xmin
    if denominator == 0:
        return x
    else:
        return (x - xmin) / float(denominator)

