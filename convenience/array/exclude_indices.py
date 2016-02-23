import numpy as np

__author__ = 'ronny'


def exclude_indices(x, excl):
    return [x[i] for i in np.arange(len(x)) if i not in excl]

