from matplotlib import pyplot as plt

__author__ = 'ronny'


# ==============================================================================
#                                                                    ARRAY2IMAGE
# ==============================================================================
def array2image(x, cmap="gray", colorbar=False, save=None, show=True):
    """
    Takes a 2D array and converts it to an image.

    :param x: {2D array}
        The 2D array to create an image from.
    :param cmap: {string} (default="gray")
        Colormap to use. This value is passed on to  matplotlib.pyplot.imshow()
        So whatever values are valid for that function can be used here.
        Some possible values:
            "gray"     = grayscale (default)
            "spectral" = reverse rainbow heatmap from black to VIBGYOR to white
            "hot"      = heatmap (black, red, yellow, white)
    :param colorbar: {boolean}(default=False)
        Should it display a colorbar to interpret values of the image colors?
    :param save: {None or string} (default=None)
        Allows you to save the image to a file by specifying a filepath/filename
    :param show: {boolean} (default=True)
        Show the image in a window?
    """
    # ==========================================================================
    plt.figure()
    plt.imshow(x, cmap=cmap)

    # Show a colorbar if it was asked for.
    if colorbar:
        plt.colorbar()

    # Save the image if requested
    if save is not None:
        plt.savefig(save)

    # show image if it is requested
    if show:
        plt.show()


