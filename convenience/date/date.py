from datetime import datetime, timedelta

# ==============================================================================
#                                                                     N_DAYS_AGO
# ==============================================================================
def n_days_ago(n):
    """ Given an integer representing number of days, it returns
        the datetime object that was n number of days ago
    """
    return datetime.now() - timedelta(days=n)
