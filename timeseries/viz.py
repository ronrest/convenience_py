import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np
import pandas as pd
# Plot comparison lines
def compare_lines(lines, labels=None, title="plot"):
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.suptitle(title, fontsize=15)
    colors=["#307EC7", "#E65C00", "#73AD21", "#9621E2", "#2BB17C", "#FF4F40"]
    labels = labels if labels is not None else [chr(97+i) for i in range(len(lines))]
    for i in range(len(lines)):
        ax.plot(lines[i], color=colors[i],  label=labels[i])
    ax.legend(loc="lower right", title="", frameon=False,  fontsize=8)
    plt.show()

def lag_plot(a,b,lag=0):
    """ given two time series, and a lag value, it olots the two lines
        with the second one lagged by lag amount
    """
    b_shifted = b.shift(lag)
    compare_lines(
        [a,b_shifted],
        labels=["a", "b (lag {})".format(lag)],
        title="LAG {}  DOT: {:0.3f}".format(lag, (a * b_shifted).sum()))


def setgrid(ax, major=True, minor=False):
    """ Given an axis object, it sets the grids on """
    if major or minor:
        ax.grid(True)

    if major:
        ax.grid(b=True, which='major', color='#999999', linestyle='-', linewidth=1)

    if minor:
        ax.minorticks_on()
        ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.7, linewidth=0.5)


def plot_densities(datas, labels=None, resolution=0.1, title="Density plot", axtitle="", xtitle="", xlabel="x", ylabel="y", show=True, ax=None, colors=None, color_offset=0, legend_pos="lower right", figsize=(10, 6), majorgrid=True, minorgrid=False):
    """
        title:   title of the figure
        axtitle: title of the axis subplot
    """
    nplots = len(datas)
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(title, fontsize=15)

    if colors is None:
        colors=["#307EC7", "#E65C00", "#73AD21", "#9621E2", "#2BB17C", "#FF4F40", "#A2C4DA", "#F9E2AC", "#ECB9FF", "#AED7AC"]

    labels = labels if labels is not None else [chr(97+i) for i in range(nplots)]
    for i in range(nplots):
        sns.kdeplot(datas[i], bw=resolution, ax=ax, color=colors[i+color_offset],  label=labels[i])
        ax.set_title(axtitle, fontdict={"style": "italic", "size": 10})
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    setgrid(ax, major=majorgrid, minor=minorgrid)
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="left")
    ax.legend(loc=legend_pos, title="", frameon=False,  fontsize=8)
    if show:
        plt.show()
    else:
        plt.close()
    return ax


def plot_lines(lines, xvals=None, labels=None, title="plot", axtitle="", xlabel="x", ylabel="y", show=True, ax=None, colors=None, color_offset=0, legend_pos="lower right", figsize=(10, 6), majorgrid=True, minorgrid=False):
    """
        title:   title of the figure
        axtitle: title of the axis subplot
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        fig.suptitle(title, fontsize=15)

    if colors is None:
        colors=["#307EC7", "#E65C00", "#73AD21", "#9621E2", "#2BB17C", "#FF4F40", "#A2C4DA", "#F9E2AC", "#ECB9FF", "#AED7AC"]

    labels = labels if labels is not None else [chr(97+i) for i in range(len(lines))]
    for i in range(len(lines)):
        if xvals is not None:
            ax.plot(xvals, lines[i], color=colors[i+color_offset],  label=labels[i])
        else:
            ax.plot(lines[i], color=colors[i+color_offset],  label=labels[i])
        ax.set_title(axtitle, fontdict={"style": "italic", "size": 10})
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    setgrid(ax, major=majorgrid, minor=minorgrid)
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="left")
    ax.legend(loc=legend_pos, title="", frameon=False,  fontsize=8)
    if show:
        plt.show()
    else:
        plt.close()
    return ax

def plot_line_rows(lines, xvals=None, labels=None, title="plot",  xlabels=None, ylabels=None, show=True, colors=None,  figsize=(10, 6), majorgrid=True, minorgrid=False):
    """
        Plots each of the lines in separate axes, one below each other
        title:   title of the figure
        axtitle: title of the axis subplot
    """
    nplots = len(lines)
    color_offset = 0
    fig, axes = plt.subplots(nplots, 1, figsize=figsize)
    axes = np.array(axes).flatten()
    fig.suptitle(title, fontsize=15)

    if colors is None:
        colors=["#307EC7", "#E65C00", "#73AD21", "#9621E2", "#2BB17C", "#FF4F40", "#A2C4DA", "#F9E2AC", "#ECB9FF", "#AED7AC"]

    labels = labels if labels is not None else [chr(97+i) for i in range(len(lines))]

    xlabels = xlabels if xlabels is not None else ["x"]*nplots
    ylabels = ylabels if ylabels is not None else ["y"]*nplots

    for i in range(nplots):
        ax = axes[i]
        if xvals is not None:
            ax.plot(xvals, lines[i], color=colors[i+color_offset],  label=labels[i])
        else:
            ax.plot(lines[i], color=colors[i+color_offset])
        ax.set_title(labels[i], fontdict={"style": "italic", "size": 10})
        ax.set_xlabel(xlabels[i])
        ax.set_ylabel(ylabels[i])
        setgrid(ax, major=majorgrid, minor=minorgrid)
        plt.setp(ax.get_xticklabels(), rotation=-30, ha="left")
        # ax.legend(loc=legend_pos, title="", frameon=False,  fontsize=8)

    # Give enough spacing between subplots x-axes and titles of plots
    fig.tight_layout(pad=1.10,  rect=[0, 0.03, 1, 0.95])

    if show:
        plt.show()
    else:
        plt.close()
    return fig


def scatterplot(x,y, title="Scatter plot", xlabel="x", ylabel="y"):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.suptitle(title, fontsize=15)
    # ax.plot(, color="#307EC7",  label="")
    ax.scatter(x, y, c="#307EC7", s=100, alpha=0.7, linewidths=0, label="")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # ax.legend(loc="lower right", title="", frameon=False,  fontsize=8)
    plt.show()


