import numpy as np

__author__ = 'ronny'


# ==============================================================================
#                                                                EXCLUDE_INDICES
# ==============================================================================
def exclude_indices(x, excl):
    """
    Returns all the elements of the array except the ones whose index is in the
    set of excluded indices.

    :param x: {array-like}
        The array you want to filter.
    :param excl: {set, or 1-D array-like of integers}
        The indices you want to exclude frm x.
    :return:
        returns x with the selected indices removed.
    """
    # ==========================================================================
    return [x[i] for i in np.arange(len(x)) if i not in excl]

