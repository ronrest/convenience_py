from datetime import datetime, timedelta

# ==============================================================================
#                                                             NUM_WITH_EXTENSION
# ==============================================================================
def num_with_extension(n):
    """ Given a number, it returns a string of the number
        with its rank extension.

        eg: 1  -> "1st"
            23 -> "23rd"
    """
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
#                                                                       DATE_STR
# ==============================================================================
def date_str(date, mode="ymd"):
    """ Given a datetime object, it returns a nicely formatted
        string representation of the date.
        
        By default it returns it in the following format:
        
            2017_06_16

        But you can specify a different format if you wish
        by setting the mode.
        
        mode accepts any format the strftime() accepts, as well
        as the following:
        
        "ymd"     2017_07_21
        "dmy"     21_07_2017
        "formal"  21st July 2017
    """
    map = {"ymd": "%Y_%m_%d",
           "dmy": "%d_%m_%Y",
            "formal": "{} %B %Y".format(num_with_extension(date.day))}
    if mode in map.keys():
        format = map[mode]
    else:
        format = mode
    return date.strftime(format)


# ==============================================================================
#                                                                     N_DAYS_AGO
# ==============================================================================
def n_days_ago(n):
    """ Given an integer representing number of days, it returns
        the datetime object that was n number of days ago
    """
    return datetime.now() - timedelta(days=n)

