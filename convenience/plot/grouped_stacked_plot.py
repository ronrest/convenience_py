from ..df.grouped_tally import grouped_tally


def grouped_stacked_plot(df=None, x=None, group=None, normalize=False, **kwargs):
    df2 = grouped_tally(df=df, x=x, group=group, normalize=normalize)
    return df2.plot(kind='bar', stacked=True, **kwargs)

