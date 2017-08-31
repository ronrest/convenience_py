__author__ = 'Ronny Restrepo'

import numpy as np
from matplotlib import pyplot as plt

# ==============================================================================
#                                                                 TALLY_AND_PLOT
# ==============================================================================
def tally_and_plot(a, labels=None, prop=False,
                   title="", xlabel="", ylabel="",
                   color="#04BAE3", alpha=0.9):
    """
    takes a 1-Dimensional array like object, and plots a bar graph of the
    tallies of the values in that array.

    You can specify if you want the tally counts, or if you want the proportions
    of each value (using the `prop` argument)

    :param a: {1D array}
    :param labels: {None or dictionary}{default=None}
        A dictionary that maps values to desired label names.
        eg:
            labels = {1: "basketball",
                      2: "soccer",
                      4: "karate"}

        This is used for the labels that appear in the x axis of the plot.

        If None (default), then it just used the unique values from `a`

    :param prop: {boolean} {default = False}
        If True, then it plots the proportions of each value, instead of tally
        counts

    :param title: {string}{defualt=""}
    :param xlabel:{string}{defualt=""}
    :param ylabel: {string}{defualt=""}
    :param color: {string"{default="#04BAE3"}
    :param alpha: {float between 0 and 1}{default=0.9}

    :example:
        a = np.array([4, 2, 2, 1, 2, 2, 4])
        tally_and_plot(a, labels={1: "basketball", 2: "soccer", 4: "karate"},
                       prop=True, xlabel="Sport", ylabel="Proportion of people",
                       title="Proportion of people playing each sport"
                       )
    """
    # ==========================================================================
    tally = np.array(np.unique(a, return_counts=True)).astype(float)

    # Replace tally counts with proportions of values if `prop` is set to True
    if prop:
        tally[1] = tally[1] / float(tally[1].sum())

    # Populate default values for labels if none provided
    if labels is None:
        labels = tally[0]
    else:
        labels = [labels[val] for val in tally[0]]

    plt.figure()
    plt.bar(range(len(tally[0])), tally[1],
            width=1, color=color, alpha=alpha)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axes().set_xticks(np.arange(len(labels)) + 0.5)
    plt.axes().set_xticklabels(labels)
    plt.minorticks_on()
    plt.grid(b=True, which='major', axis="y", color='#666666', linestyle='-',
             alpha=0.9)
    plt.grid(b=True, which='minor', axis="y", color='#999999', linestyle='-',
             alpha=0.6)
    plt.show()



