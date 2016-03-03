from matplotlib import pyplot as plt
import numpy as np

__author__ = 'Ronny Restrepo'


def plot_grid_array(grid, cell_height, labels, title="", save=None, show=True):
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

