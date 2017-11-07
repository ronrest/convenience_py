
# Data Exploration for Segmentation Task

## Label Distributions Violin Plot

```py
# ==============================================================================
#                                                   PLOT_SEG_LABEL_DISTRIBUTIONS
# ==============================================================================
def plot_seg_label_distributions(Y, id2label, colormap, saveto=None):
    """ Given an array of the segmentation labels in a dataset, it plots
        the relative distribution of each class label as violin plots.

        It shows the distribution of how much each class takes up as a
        proportion of the entire image (how many pixels are taken up by
        that class).

    Dependencies:
        seaborn, matplotlib, numpy, collections Counter

    Args:
        Y:          (np array) Array contianing the segmentation label images,
                    with integer vals representing the class ids for each pixel
        id2label:   (list) Map from label id to human readable string label
        colormap:   (list) List of the (R,G,B) values for each class.
        saveto:     (str or None)(default=None) optionally save the image
                    instead of displaying it.
    """
    rgb2hex = lambda x: "#"+"".join(["{:>02s}".format(hex(ch)[2:]) for ch in x])

    distributions = []
    n_classes = len(id2label)
    for img in Y:
        tally = Counter(img.flatten()) # counts for each class
        distributions.append([tally[i]/float(img.size) for i in range(n_classes)])
    distributions = np.array(distributions)

    sns.set(style="whitegrid", palette="pastel", color_codes=True)
    fig, ax = plt.subplots(1, 1, figsize=(10, 20))
    sns.violinplot(data=distributions,
                   scale="count",
                   ax=ax,
                   dodge=False,
                   fliersize=2,
                   linewidth=0.5,
                   inner="point",  #:“box”, “quartile”, “point”, “stick”, None
                   orient="h",
                   palette=[rgb2hex(code) for code in colormap],
                   )
    # fig.suptitle('Distribution of Space Taken up by Classes', fontsize=15)
    ax.set_title("Distribution of Space Taken up by Classes", fontdict={"weight": "bold", "size": 20})
    ax.set_xlabel("Proportion of Image", fontsize=20)
    ax.set_yticklabels(id2label)
    plt.setp(ax.get_xticklabels(), fontsize=20)
    plt.setp(ax.get_yticklabels(), fontsize=20)
    ax.set_xlim([0,0.7])
    fig.tight_layout()

    if saveto:
        plt.savefig(saveto)
        plt.close()
    else:
        plt.show()
```

![Image of violin plot](violin_plot.jpg)
