def grouped_tally(df=None, x=None, group=None):
    df2 = df.pivot_table(index=group,
                         columns=x,
                         aggfunc="size")
    return df2
