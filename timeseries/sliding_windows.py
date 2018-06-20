

def sliding_window_corelations(a,b, window=30, startdate=None, enddate=None, resolution="d"):
    """ Given two pandas timeseries it performs correlations of thse timeseries
        over a chunk of time specified by window timesteps (in the past),
        and slides that window from `startdate` to `enddate`, getting a
        correlation at each timestep.

        Returns a pandas timeseries of correlation values over the
        time range.
    """
    resmap = {"d":"days", "h":"hours"}
    assert resolution in resmap.keys(), "Only accepting resolution {} currently".format(resmap.keys())

    if startdate is None:
        startdate = max(a.index.min(), b.index.min())
    if enddate is None:
        enddate = min(a.index.max(), b.index.max())

    corrs = pd.Series(index=pd.date_range(startdate, enddate, freq=resolution))

    delta = datetime.timedelta(**{resmap[resolution]:window})

    daterange_delta = enddate-startdate

    if resolution == "h":
        timesteps = int((enddate-startdate).total_seconds()/3600)
    elif resolution == "d":
        timesteps = daterange_delta.days

    for i in range(timesteps):
        offset = datetime.timedelta(**{resmap[resolution]:i})

        time_a = startdate + offset - delta
        time_b = startdate + offset

        corr = a[time_a:time_b].corr(b[time_a:time_b])
        corrs[time_b] = corr
    return corrs
