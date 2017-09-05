import datetime

# ==============================================================================
#                                                                TIMESTAMP 2 STR
# ==============================================================================
def timestamp2str(t, pattern="%Y-%m-%d  %H:%M:%S"):
    """ Given a float timestamp it returns the date as a formatted string,
        based on the date `pattern` specified """
    return datetime.datetime.fromtimestamp(t).strftime(pattern)
