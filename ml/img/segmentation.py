import numpy as np


# ==============================================================================
#                                                              PIXELS_WITH_VALUE
# ==============================================================================
def pixels_with_value(img, val):
    """ Given an image as a numpy array, and a value representing the
        pixel values, eg [128,255,190] in an RGB image, then it returns
        a 2D boolean array with a True for every pixel position that has
        that value.
    """
    return np.all(img==np.array(val), axis=2)


