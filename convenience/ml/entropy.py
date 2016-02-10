import numpy as np

# ==============================================================================
#                                                                        ENTROPY
# ==============================================================================
def entropy(x):
    """
    Takes a 1D numpy array containing the counts for items for different
    classes, and it returns the entropy.

    :param x: (1D array)
    :return: (float)
    """
    # ==========================================================================
    p = x/x.sum()                   # probability for each class
    return (-p*np.log2(p)).sum()    # return entropy

