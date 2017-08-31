import numpy as np
import pandas as pd

#===============================================================================
#                                             Tally, and Ratios of Unique Values
#===============================================================================
def tally(x, as_df=True):
    """
    Takes an array, and returns a table where the first column gives the unique
    values. The second column gives the counts of each of those values. And the
    third column gives the ratio proportions of each of the values.

    :param x: the numpy array
    :param as_df: {boolean} {Default = True}

        If True, it returns a pandas Dataframe with labelled columns

        If False, it returns a 2D numpy array.

    :return: {2D array or pandas Dataframe}
    """
    # ==========================================================================
    cc =np.array(np.unique(x, return_counts=True))
    ratios = cc[1] / float(cc[1].sum())
    table = np.vstack((cc, ratios)).T
    if as_df:
        table = pd.DataFrame(table)
        table.columns = ["value", "count", "ratio"]
        return table
    else:
        return table


