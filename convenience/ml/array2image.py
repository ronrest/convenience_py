from matplotlib import pyplot as plt

__author__ = 'ronny'

# ==============================================================================
#                                                                    ARRAY2IMAGE
# ==============================================================================
def array2image(x, cmap="gray"):
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
    """
    # ==========================================================================
    plt.figure()
    plt.imshow(x, cmap=cmap)

    plt.show()


