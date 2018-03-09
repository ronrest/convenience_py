import datetime

# ==============================================================================
#                                                                TIMESTAMP 2 STR
# ==============================================================================
def timestamp2str(t, pattern="%Y-%m-%d  %H:%M:%S"):
    """ Given a float timestamp it returns the date as a formatted string,
        based on the date `pattern` specified """
    return datetime.datetime.fromtimestamp(t).strftime(pattern)


# ==============================================================================
#                                                                   STR2DATETIME
# ==============================================================================
# import datetime
from dateutil import tz
def str2datetime(s, f="%Y_%m_%d %H:%M:%S", tzone=None):
    """ Takes a string and converts to a datetime object given that it is
        formatted based on the pattern passed in as `f`.

        Optionally also set the timezone of the date by passing a timezone
        string. If no timezone is provided, it defailts to using the loceal
        timezone.

        Examples of `tzone`
        - "UTC"
        - "Australia/Melbourne"
    """
    t = datetime.datetime.strptime(s, f)
    if tz is not None:
        tza = tz.gettz(tzone)     # Timezone object
        t = t.replace(tzinfo=tza) # Set the timezone
    return t


# ==============================================================================
#                                                               CONVERT_TIMEZONE
# ==============================================================================
# import datetime
from dateutil import tz
def convert_timezone(time, a="UTC", b="local"):
    """ Given a datetime object, in timezone a, it changes it to timezone b.

    Args:
        time:   (datetime object)
        a:      (str) timezone code to set the from time as.
                eg:
                "UTC"
                "Australia/Melbourne"
                or..
                "local"
        b:      (str) timezone to set the to time as.
    """
    # TIMEZONE OBJECTS
    tza = tz.tzlocal(a) if (a=="local") else tz.gettz(a)
    tzb = tz.tzlocal(b) if (b=="local") else tz.gettz(b)

    # FORMAT TIME WITH FROM TIMEZONE
    time = time.replace(tzinfo=tza)

    # CHANGE TIME ZONE
    newtime = time.astimezone(tzb)
    return newtime
