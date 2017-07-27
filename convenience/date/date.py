from datetime import datetime, timedelta

# ==============================================================================
def num_with_extension(n):
    if 10 <= n % 100 <= 20:  # special case of 11-13
        ext = "th"
    elif n % 10 == 1:
        ext = "st"
    elif n % 10 == 2:
        ext = "nd"
    elif n % 10 == 3:
        ext = "rd"
    else:
        ext = "th"
    return "{}{}".format(n, ext)


# ==============================================================================
#                                                                     N_DAYS_AGO
# ==============================================================================
def n_days_ago(n):
    """ Given an integer representing number of days, it returns
        the datetime object that was n number of days ago
    """
    return datetime.now() - timedelta(days=n)
