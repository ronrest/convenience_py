"""====================================================
                    DESCRIPTION

=======================================================
"""
__author__ = 'ronny'

import numpy as np

#===============================================================================
#                                                              NORMALISE COLUMNS
#===============================================================================
def normalise_columns(x, mean, sd):
    """
    Normalise the elements of a 2D array to be Z-scores (standard normal values)
    scaled by some consistent mean and sd for each column(which should be the
    mean and sd of the training data)

    :param x: (2D Array)
        A 2D array, whose columns we wish to normalise
    :param mean: (1D array)
        The means to be used to normalise each of the columns of x
    :param sd: (1D array)
        The standard deviations to be used to normalise each of the columns of x
    :return: (numpy array)
        Returns an array where the elements are normalised along the columns.
    """
    # ==========================================================================
    return (np.array(x) - mean) / sd



#===============================================================================
#                                                           UN_NORMALISE COLUMNS
#===============================================================================
def un_normalise_columns(z, mean, sd):
    """
    Takes a 2D array of Z-score values, along with the mean and standard
    deviations for each column used to calculate those z-scores. Returns the
    values in their original scale.

    :param z: (2D Array)
        A 2D array, containing z-score values
    :param mean: (1D array)
        The means that were used to normalise each of the columns of z
    :param sd: (1D array)
        The standard deviations that were used to normalise each of the columns
        of z
    :return: (numpy array)
        Returns an array where the elements are the values in their original
        scale. .
    """
    # ==========================================================================
    return z*sd + mean


