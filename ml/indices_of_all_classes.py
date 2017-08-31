__author__ = 'Ronny Restrepo'

import numpy as np

# ==============================================================================
#                                                         INDICES_OF_ALL_CLASSES
# ==============================================================================
def indices_of_all_classes(y):
    """
    Takes a 1D array containing the output labels used in training or testing,
    and returns a dictionary where the keys are the unique classes, and
    the dictionary values for each of those keys is the indices of all
    elements in the 1D array with that class as its value.

    :param y:{1D array}
        The 1D array contianing the class labels
    :return:
        A dictionary with the unique class labels as keys, and arrays of indices
        from y that contain each of those class labels

    :example
        >>> y = np.array([4,3,3,4])
        >>> indices_of_all_classes(y)
        {3: array([1, 2]), 4: array([0, 3])}
    """
    # ==========================================================================
    # Ensure that y is a 1D array
    y = np.array(y)
    dims = len(y.shape)
    assert (dims  == 1), "Expected a 1D array, got a {}D array".format(dims)

    # Create and return dictionary
    return {i: np.where(y == i)[0] for i in np.unique(y)}

