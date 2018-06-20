import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
deom sliding_windows import sliding_window_corelations


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


def column_correlate_heat_and_scatter(df, targetcol, title="Correlations", saveto=None):
    """ given a dataframe,  and a target column name, it shows the heatmap and
        scatter plots of that column against all the other variables in the
        dataframe.
    """
    fig = plt.figure(figsize=(8, 8))
    fig.suptitle(title, fontsize=15)
    # gridspec inside gridspec
    outer_grid = gridspec.GridSpec(1, 2, wspace=0.0, hspace=0.0, width_ratios=[1,3], height_ratios=[3])
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # LEFT PLOT
    ax = plt.Subplot(fig, outer_grid[0])
    df2 = df.copy()
    corr = df2.corr()[[targetcol]]
    # ax.set_title("left plot", fontdict={"style": "italic", "size": 10})
    ax = sns.heatmap(corr, annot=True, linewidths=2, square=False, center=0, vmax=1, vmin=-1, cmap=cmap, ax=ax, cbar=False)
    ax.axis("equal")
    plt.setp(ax.get_yticklabels(), rotation=0, ha="right")
    fig.add_subplot(ax)

    # RIGHT INNER GRID
    ncols = df.shape[1]
    width = int(np.ceil(np.sqrt(ncols)))
    inner_grid = gridspec.GridSpecFromSubplotSpec(width, width,
        subplot_spec=outer_grid[1], wspace=0.0, hspace=0.0,
        width_ratios=[1]*width, height_ratios=[1]*width)

    for i, colname in enumerate(df.columns):
        cmap = plt.get_cmap('viridis')
        indices = np.linspace(0, cmap.N, len(df))
        my_colors = [cmap(int(i)) for i in indices]

        ax = plt.Subplot(fig, inner_grid[i], adjustable='box') # , aspect='equal',
        # ax.axis("equal")
        ax.set_title(colname, fontdict={"style": "italic", "size": 10}, y=-0.0000005) # "y": -0.1
        ax.scatter(df[colname], df[targetcol],  label=colname, color=my_colors) # color="#307EC7"
        ax.set_xticks([])
        ax.set_yticks([])
        fig.add_subplot(ax)

    if saveto is not None:
        fig.savefig(saveto)
        plt.close()
    else:
        plt.show()


def multi_sliding_correlation_window_plots(df, target, columns, window=60, resolution="d", startdate=None, enddate=None, show=True, ax=None, colors=None, show_missing=True):
    # Missing data plot
    if show_missing:
        df2 = df[startdate:enddate].copy()
        missing = df2.isnull().any(axis=1).astype(np.int32)
        if ax is None:
            ax = plot_lines([missing], colors=["#978084"], labels=["missing"], title="Sliding Window ({w} {r}) Correlation".format(w=window, r=resolution), ylabel="correlation", xlabel="time", show=False)
        else:
            ax = plot_lines([missing], colors=["#978084"], labels=["missing"], ylabel="correlation", xlabel="time", show=False, ax=ax)

    for i, column in enumerate(columns):
        corrs = sliding_window_corelations(df[target], df[column], window=window, startdate=startdate, enddate=enddate, resolution=resolution)
        if (ax is None) and (i == 0) and not show_missing:
            ax = plot_lines([corrs], title="Sliding Window ({w} {r}) Correlation".format(w=window, r=resolution), labels=[column], ylabel="correlation", xlabel="time", show=False, colors=colors, color_offset=i)
        else:
            ax = plot_lines([corrs], labels=[column], show=False, ax=ax, color_offset=i, colors=colors)

        # ax.grid(True)
        ax.minorticks_on()
        ax.grid(b=True, which='major', color='#999999', linestyle='-', linewidth=1)
        ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.7, linewidth=0.5)

    fig = ax.get_figure()
    if show:
        fig.show()
    return fig


def lag_sliding_correlation_plot(df, target, column, lag=1, window=60, startdate=None, enddate=None):
    """ Given a dataframe and the name of two columns, and an amount to lag,
        it plots the correlation lineplot of a given sliding `window` of correaltions,
        so you can compare how the sliding window correlations change as one of
        the timeseries is lagged by a different ammount.
    """
    fig, ax = plt.subplots(figsize=(10, 6), sharex=True, sharey=True)
    fig.suptitle('Time Shifted Correlations (Window={w} Lag={lag})'.format(w=window, lag=lag), fontsize=15, fontdict={"fontweight": "extra bold"})
    fig = multi_sliding_correlation_window_plots(df=df, target=target, window=window, columns=[column], startdate=startdate, enddate=enddate, show=False, ax=ax)

    df2 = df.copy()
    df2["num_comments"] = df2["num_comments"].shift(lag)
    fig = multi_sliding_correlation_window_plots(df=df2, target=target, window=window, columns=[column], startdate=startdate, enddate=enddate, show=False, ax=ax, colors=["#FF0000", "#00FF00"])
    return fig




def timeseries_exploratory_plots(x, title="Plots", raw=True, change=True, change_type="adj",
                                 lag=1, autocorr=True, autocorr_changes=True,
                                 density=True, density_resolution=0.1,
                                 density_change=True, density_change_resolution=0.1,
                                 pacf=True, pacf_change=True,
                                 figsize=(10,20)):
    """ Given a pandas series, it plots up to three plots below each other.
        - the raw data
        - the percent changes
        - the autocorrelation plots

        NOTE: that currently it REQUIRES the data to NOT have any missing/NAN
        values, otherwise it will plot things incorrectly, so make sure data
        being fed in is cleaned up.

    Args:
        change_type:    (str)
            The type of changes to use. One of:
            - "diff" for raw differences in subsequent numbers
            - "pct"  to use pandas x.diff() function
            - "adj"  to use my adjusted percentage change function
        lag:    (int)(default = 1)
            How many timesteps to offset the change/diff by.
        density:    (bool) create plot of density?
        density_resolution: (float)(default=0.1)
            Resolution of the density estimation.

        density_change:    (bool) create plot of density for changes?
        density_change_resolution: (float)(default=0.1)
            Resolution of the density estimation.

        pacf: (bool) create partial auto correlation funciton plot on the raw data?
        pacf_change: (bool) create partial auto correlation funciton plot on the changes data?

    """
    nplots = sum([raw, change, autocorr, autocorr_changes, density, density_change, pacf, pacf_change])
    fig, axes = plt.subplots(nplots,1, figsize=figsize)
    axes = axes.flatten()
    fig.suptitle(title, fontsize=15)
    i = 0
    if raw:
        ax = plot_lines([x], axtitle="raw data",  xlabel="x", ylabel="raw value", ax=axes[i], show=False, minorgrid=True)
        i += 1

    if change or autocorr_changes:
        # percent_changes = pd.Series(x).pct_change()
        if change_type == "adj":
            percent_changes = adjusted_percent_change(x, lag=lag, epsilon=0.1)
        elif change_type == "pct":
            percent_changes = pd.Series(x).pct_change(lag)
        elif change_type == "diff":
            percent_changes = pd.Series(x).diff(lag)


    if change:
        ax = plot_lines([percent_changes], axtitle="Percent Change",
                        color_offset=1, ax=axes[i], xlabel="x",
            ylabel="percent change", minorgrid=True)
        i += 1

    if density:
        ax = plot_densities([x], ax=axes[i], labels=["Distribution of raw data"],
                            resolution=density_resolution, minorgrid=True)
        i += 1

    if density_change:
        ax = plot_densities([percent_changes], ax=axes[i], labels=["Distribution of changes"],
                            resolution=density_change_resolution, minorgrid=True)
        i += 1

    # Autocorrelation function plot
    if autocorr:
        ax = axes[i]
        fig = plot_acf(x, lags=50,
                       alpha=0.05, title="Autocorrelation plot", ax=ax)
        setgrid(axes[i], minor=True)
        ax.set_xlabel("lag amount")
        ax.set_ylabel("Correlation")
        i += 1

    # Autocorrelation function plot of the changes
    if autocorr_changes:
        ax = axes[i]
        fig = plot_acf(percent_changes[1:].fillna(method="backfill"), lags=50,
                       alpha=0.05, title="Autocorrelation of Percent Changes plot", ax=ax)
        setgrid(axes[i], minor=True)
        ax.set_xlabel("lag amount")
        ax.set_ylabel("Correlation")
        i += 1

    # partial Autocorrelation function plot
    if pacf:
        ax = axes[i]
        fig = plot_pacf(x, lags=50,
                       alpha=0.05, title="Partial Autocorrelation Function plot", ax=ax)
        setgrid(axes[i], minor=True)
        ax.set_xlabel("lag amount")
        ax.set_ylabel("Correlation")
        i += 1

    # partial Autocorrelation function plot on changes data
    if pacf_change:
        ax = axes[i]
        fig = plot_pacf(percent_changes, lags=50,
                       alpha=0.05, title="Partial Autocorrelation Function plot on changes", ax=ax)
        setgrid(axes[i], minor=True)
        ax.set_xlabel("lag amount")
        ax.set_ylabel("Correlation")
        i += 1


    # Give enough spacing between subplots x-axes and titles of plots
    fig.tight_layout(pad=1.10,  rect=[0, 0.03, 1, 0.95])

    return fig
