"""====================================================
                    DESCRIPTION

=======================================================
"""
__author__ = 'ronny'
import numpy as np

#===============================================================================
#                                                      Pairs of All Grid points
#===============================================================================
def grid_point_pairs(x_range=(-4,4), y_range=(-4,4), x_step=0.1, y_step=0.1):
    """
    generate all points of a grid within a range of values and step sizes.

    :param x_range: tuple of min and max values (inclusive)
    :param y_range: tuple of min and max values (inclusive)
    :param x_step: step size along x axis
    :param y_step: step size along y axis
    :return: 2D-Array, with each row being an x,y pair representing a point in
             the grid.
    """
    arrays = [np.arange(x_range[0], x_range[1] + x_step, x_step),
              np.arange(y_range[0], y_range[1] + y_step, y_step)]
    return all_element_combinations(arrays)


#===============================================================================
#                                                      all_element_combinations
#===============================================================================
def all_element_combinations(arrays, out=None):
    """
    code written by: pv.
    taken from http://stackoverflow.com/a/1235363

    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> all_element_combinations(([1,2,3], [10, 20]))
    array([[ 1, 10],
           [ 1, 20],
           [ 2, 10],
           [ 2, 20],
           [ 3, 10],
           [ 3, 20]])

    """
    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype                # to preserve same element datatype
    n = np.prod([x.size for x in arrays])  # Number of combinations

    # Initialise the output pairs to zeros
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype) # preserves element datatype

    m = n / arrays[0].size
    # populate the values for the very first axis
    out[:,0] = np.repeat(arrays[0], m)

    # recursively workout the values of the other axes.
    if arrays[1:]:
        all_element_combinations(arrays[1:], out=out[0:m,1:])
        for j in xrange(1, arrays[0].size):
            out[j*m:(j+1)*m,1:] = out[0:m,1:]
    return out
