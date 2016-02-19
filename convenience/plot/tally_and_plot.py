__author__ = 'Ronny Restrepo'

import numpy as np
from matplotlib import pyplot as plt

def tally_and_plot(a, labels=None, prop=False,
                   title="", xlabel="", ylabel="",
                   color="#04BAE3", alpha=0.9):
    tally = np.array(np.unique(a, return_counts=True)).astype(float)

    # Replace tally counts with proportions of values if `prop` is set to True
    if prop:
        tally[1] = tally[1] / float(tally[1].sum())

    # Populate default values for labels if none provided
    if labels is None:
        labels = tally[0]

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


