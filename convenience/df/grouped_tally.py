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

    :param df: {pandas dataframe}
    :param x: {String}
        Name of the column whose values we want to tally up
    :param group: {String}
        Name of the colum we want to group the values by.
    :return: {Pandas Dataframe}
        Returns the grouped tally table as a pandas dataframe
    """
    # ==========================================================================
    df2 = df.pivot_table(index=group,
                         columns=x,
                         aggfunc="size")
    return df2

