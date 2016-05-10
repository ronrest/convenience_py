import pandas as pd

# ==============================================================================
#                                                                  GROUPED_TALLY
# ==============================================================================
def grouped_tally(df=None, x=None, group=None):
    """
    Given two columns of discrete data (one which you want to tally up, and
    another you want to group by), it returns a dataframe where each row is the
    group, and each column is a tally of the desired values for that group.

    eg, in order to get a table like the follwoing, we group by treatment group,
    and use "improved" as the column we want to tally up.

                     Improved
                      no  yes
    treatment_group
            1         80  136
            2         97   87
            3        372  119


    NOTE: You can either pass it a dataframe as argument `df`, and select the
    `x`, and `group` columns by name. OR, you can leave `df` blank, and feed
    the actual columns of data as arguments `x` and `group`.

    :param df: {pandas dataframe}(optional)
        Dataframe that contains the columns of data you want to use.
    :param x: {String, or List-like object}
        Either the name of the column whose values we want to tally up from `df`
        OR
        A list-like object that can be converted by pandas into a dataframe.
        (It will accept a list, a 1D numpy array, or a Pandas Series)
    :param group: {String or List-like object}
        Either the name of the column we want to group the values by
        OR
        Like `x` it will also accept a list-like object of the data itself for
        this column.
    :return: {Pandas Dataframe}
        Returns the grouped tally table as a pandas dataframe
    """
    # ==========================================================================
    # --------------------------------------------------------------------------
    #                                              Make sure Arguments are Valid
    # --------------------------------------------------------------------------
    if x is group is None:
        msg = "\n    Cannot perform any grouping or tallying. " \
              "\n    Make sure that at least one of the " \
              "\n    arguments picks out a column of data" \
              "\n    that can be converted into a pandas " \
              "\n    dataframe"
        raise AssertionError(msg)
    # --------------------------------------------------------------------------
    #                                         Raw Column Data have been provided
    # --------------------------------------------------------------------------
    if df is None:
        df = pd.DataFrame({"x": x, "group": group})
        x = "x" if x is not None else None
        group = "group" if group is not None else None
    # --------------------------------------------------------------------------
    #                                              A Dataframe has been provided
    # --------------------------------------------------------------------------
    if isinstance(df, pd.core.frame.DataFrame):
        df2 = df.pivot_table(index=group,
                             columns=x,
                             aggfunc="size")
        return df2

