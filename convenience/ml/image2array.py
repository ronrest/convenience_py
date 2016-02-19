from scipy import ndimage


# ==============================================================================
#                                                                    IMAGE2ARRAY
# ==============================================================================
def image2array(f, flatten=False):
    """
    Takes a file path to an image file, and returns the pixel data as a numpy
    array of floats.

    :param f: {string}
        Filepath to the image file of interest.
    :param flatten: {boolean}(default = False)
        Should it flatten multiple color channels into one single channel?
        - If True, then it takes the average of the color channels
    :return: {numpy array}
        Returns an array with the pixel data
    """
    # ==========================================================================
    img = ndimage.imread(f).astype(float)

    # Flatten the image color channels if needed
    if flatten and len(img.shape) > 2:
        img = img.mean(axis=2)

    return img


