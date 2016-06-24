import matplotlib.pyplot as plt


def labelled_scatter(points, labels, new_fig=True, color="#FF8000"):
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


