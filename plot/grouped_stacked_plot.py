from ..df.grouped_tally import grouped_tally


# ==============================================================================
#                                                           GROUPED_STACKED_PLOT
# ==============================================================================
def grouped_stacked_plot(df=None, x=None, group=None, normalize=False, **kwargs):
    """
    Given two columns of discrete data (one which you want to tally up, and
    another you want to group by), it returns a stacked bar plot
    where a column of data is created that is split up into the various discrete
    values for the column of data, and separate columns for each group.

    eg, in order to get a plot like the following, we group by lecture group,
    and use gender as the column we want to tally up.

        60-|    M
        50-| M  M     M
        40-| M  F     M
        30-| M  F  M  M
        20-| F  F  F  M
        10-| F  F  F  F
            --------------
             \  \  \  \
             A  B  C  D  Lecture Group


    NOTE: You can either pass it a dataframe as argument `df`, and select the
    `x`, and `group` columns by name. OR, you can leave `df` blank, and feed
    the actual columns of data as arguments `x` and `group`.

    :param df: {pandas dataframe}(optional)
        Dataframe that contains the columns of data you want to use.
    :param x: {String, or List-like object}
        This will be the column whose values we want to tally up from `df`.

        If you provided a dataframe for `df` then use a string to represent the
        name of the column in `df`.

        OTHERWISE

        Provide the data itself as a list-like object that can be converted by
        pandas into a dataframe.
        (It will accept a list, a 1D numpy array, or a Pandas Series)
    :param group: {String or List-like object}
        The column of data we want to group the values by.

        As with `x`, you specify the column name with a string if you provided
        a dataframe for `df`.

        OTHERWISE

        Provide the data for this column.

    :param normalize: {Boolean} (default=False)
        Do you want the values to be ratios that add up to 1 across each group?

    :param kwargs: (optional)
        Aditional key-word arguments to pass on to pandas
        dataframe.plot(kind='bar', stacked=True, **kwargs) method.

    :return: {Matplotlib plot}
        Returns a pyplot object.
    """
    # ==========================================================================
    df2 = grouped_tally(df=df, x=x, group=group, normalize=normalize)
    return df2.plot(kind='bar', stacked=True, **kwargs)

