import numpy as np

def minmax_scaling(x, min=None, max=None):
    x = np.array(x)
    xmax = x.max() if max is None else max
    xmin = x.min() if min is None else min
    denominator = xmax - xmin
    if denominator == 0:
        return x
    else:
        return (x - xmin) / float(denominator)

