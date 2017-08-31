import matplotlib.pyplot as plt


# ==============================================================================
#                                                               LABELLED_SCATTER
# ==============================================================================
def labelled_scatter(points, labels, new_fig=True, color="#FF8000"):
    """
    Plots a scatterplot, with text labels right next to each of the scatter
    points labelling what that point represents.

    Is useful for things like visualising word embeddings in 2D space.

    :param points:
        An array like object, with 2 columns, the first one for x coordinate,
        and the second one for the y coordinate.
    :param labels:
        List of strings, with each element being the label for each
        corresponding row in the `points` array.
    :param new_fig: {boolean} (default = True)
        Plot as a new figure?
        If True (default) then it creates the plot in a new figure window.
        If False, then it creates the plot in the existing figure window.
    :param color: {str} (default="#FF8000")
        Color to use for the scatter points.
    """
    # ==========================================================================
    if new_fig:
        plt.figure()

    # Plot the scatter points
    plt.scatter(points[:,0], points[:,1], s=100, linewidths=0,
                c=color, alpha=0.7)

    # Attach labels to the scatter points
    for pos, label in zip(points, labels):
        plt.annotate(label, xy=(pos[0], pos[1]), xytext=(7, 0),
                     textcoords='offset points',
                     ha='left', va='center')
    plt.show()


