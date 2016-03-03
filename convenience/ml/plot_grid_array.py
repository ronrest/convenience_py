from matplotlib import pyplot as plt
import numpy as np

__author__ = 'Ronny Restrepo'


# ==============================================================================
#                                                                PLOT_GRID_ARRAY
# ==============================================================================
def plot_grid_array(grid, cell_height, labels, title="", save=None, show=True):
    """
    Takes a 2D array that can be thought of as a grid of images, like the one
    returned by the `sample_grid_of_arrays()` function, and plots it, with class
    labels along the y axis for each row of images that belong to some class.

    :param grid: {2D array}
        The 2D array we are treating as a grid of arrays
    :param cell_height: {int}
        Height of each individual row
    :param labels: {1D array-like}
        Class labels to use on the plot.
    :param title: {string}
        Title for the plot.
    :param save: {None of string}
        filepath and name to save the plotted image as.
    :param show:
    :return:
    """
    # ==========================================================================
    plt.figure()
    plt.imshow(grid, cmap="gray")

    # ----------------------------------------
    # Set the title and axis labels
    # ----------------------------------------
    plt.title(title)
    plt.axes().set_yticks(
            np.arange(len(labels)) * cell_height + (cell_height / 2.0))

    if labels is not None:
        plt.axes().set_yticklabels(labels)

    plt.axes().axes.get_xaxis().set_visible(False)
    plt.ylabel("Class")

    # ----------------------------------------
    # Save the image if requested
    # ----------------------------------------
    if save is not None:
        plt.savefig(save)

    # ----------------------------------------
    # Show the image if requested
    # ----------------------------------------
    if show:
        plt.show()

