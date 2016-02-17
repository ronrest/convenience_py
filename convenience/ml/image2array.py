from scipy import ndimage


# ==============================================================================
#                                                                    IMAGE2ARRAY
# ==============================================================================
def image2array(f):
    """
    Takes a file path to an image file, and returns the pixel data as a numpy
    array of floats.

    :param f: {string}
        Filepath to the image file of interest.
    :return: {numpy array}
        Returns an array with the pixel data
    """
    # ==========================================================================
    return ndimage.imread(f).astype(float)


