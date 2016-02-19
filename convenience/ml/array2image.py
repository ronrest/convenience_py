from matplotlib import pyplot as plt

__author__ = 'ronny'

# ==============================================================================
#                                                                    ARRAY2IMAGE
# ==============================================================================
def array2image(x):
    """
    Takes a 2D array and converts it to an image.

    :param x: {2D array}
        The 2D array to create an image from.
    """
    # ==========================================================================
    plt.figure()
    plt.imshow(x, cmap="gray")

    plt.show()


