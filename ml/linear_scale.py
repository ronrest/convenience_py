import numpy as np


# ==============================================================================
#                                                                   LINEAR_SCALE
# ==============================================================================
def linear_scale(x, new_range=(0.0, 1.0), old_range="auto"):
    """
    Takes an array x, and rescales the range of values to some new scale. By
    default it rescales teh values to be floats between 0 and 1.

    :param x: {array-like}
        The array whose values you want to scale.
    :param new_range: {tuple of two numbers} (default = (0.0, 1.0))
        A tuple of two numbers you want the elements of x to be scaled to.
        (min, max)
        NOTE: the range is inclusive of min and max.
    :param old_range: {tuple of two numbers, or "auto"} (default="auto")
        if "auto", then it automatically sets the min and max range of values
        based on the actual minimum and maximum values that occur in x.

        If a tuple of two numbers is provided (new_min, new_max) then it scales
        the values with the knowledge that the elements in x are values that
        come from a known range of values.

        NOTE: it is preferable to explicitly specify an old_range tuple. If
              x is composed of values that *could* range from 0-100, and you
              want to rescale to the range 0-1, then you might get unexpected
              results if there are no actual elements with the value 0 or 100
              in x.
    :return: {array}
        Returns a new array of same shape as x, which is rescaled.
    """
    # ==========================================================================
    if old_range is "auto":
        old_range = (x.min(), x.max())

    old_min = old_range[0]
    old_max = old_range[1]

    new_min = new_range[0]
    new_max = new_range[1]

    # The scaling ratio
    ratio = float(new_max - new_min) / (old_max - old_min)

    # Scale values to the new range of values
    return new_min + ratio*(np.array(x) - old_min)


def linear_scale_array(x, newmins, newmaxes, oldmins, oldmaxes):
    """ Given a 1D array it linearly scales each of the elements
        independently based on their corresponding old, and new min and max
        values.
    Example:
        >>> linear_scale_array([24, 145],
        >>>                     newmins=[0,-1],
        >>>                     newmaxes=[1, 1],
        >>>                     oldmins=[0,0],
        >>>                     oldmaxes=[100,200])
        array([ 0.24,  0.45])
    """
    # ensure values are numpy arrays
    newmins = np.array(newmins)
    newmaxes = np.array(newmaxes)
    oldmins = np.array(oldmins)
    oldmaxes = np.array(oldmaxes)
    x = np.array(x)

    # TODO: handle oldmaxes and oldmins being Nones
    #       find out min and max from x
    # TODO: handle scalar inputs to mins and maxes, and even x
    ratios = (newmaxes-newmins)/(oldmaxes-oldmins)
    return newmins + ratios*(x-oldmins)
