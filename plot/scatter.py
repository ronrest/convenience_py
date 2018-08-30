import matplotlib.pyplot as plt

def plot_scatter(x, y, ax=None, color=None, alpha=None, size=None, labels=None, title="Scatterplot", figsize=(10,6)):
    # TODO: Add x, and y labels
    # TODO: grid
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(title, fontsize=15)
    else:
        fig = ax.get_figure()
    ax.scatter(x=x, y=y, c=color, alpha=alpha, s=size)

    # LABEL - each of the points
    if labels is not None:
        for xx, yy, label in zip(x, y, labels):
            plt.annotate(label, xy=(xx, yy), xytext=(7, 0),
                         textcoords='offset points',
                         ha='left', va='center')
    return fig, ax
