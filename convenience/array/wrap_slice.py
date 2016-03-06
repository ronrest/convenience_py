

def wrap_slice_indices(array_len, start, slice_len):
    return [index % array_len for index in range(start, start+slice_len)]



# ==============================================================================
#                                                                     WRAP_SLICE
# ==============================================================================
def wrap_slice(x, start, slice_len):
    """
    Takes an array, and returns a slice of a particular size of consecutive
    elements.

    If the combination of starting position and length of the slice go beyond
    the boundaries of the array, then it automatically wraps around to the
    beginning of the array and continues from there.

    If the starting index is larger than the array length, then it calculates
    the index it would start at if it were to wrap around the array as many
    times as needed (Modular arithmetic)

    See the examples for a better intuition.

    :param x: {array}
        The array you want to slice.
    :param start: {int}
        The index you want to start at.
    :param slice_len: {int}
        How big do you want the slice?
    :return: {array}
        Sliced version of the array.

    :example:
    >>> import numpy as np
    >>> x = np.array([100, 101, 102, 103, 104, 105, 106, 107, 108, 109])
    >>> wrap_slice(x, start=8, slice_len=4)
    array([108, 109, 100, 101])


    >>> x = np.array([10, 11, 12, 13, 14])
    >>> wrap_slice(x, start=3, slice_len=10)
    array([13, 14, 10, 11, 12, 13, 14, 10, 11, 12])
    """
    # ==========================================================================
    return x[[index % x.shape[0] for index in range(start, start+slice_len)]]

