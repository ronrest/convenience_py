import datetime

# ==============================================================================
#                                                                TIMESTAMP 2 STR
# ==============================================================================
def timestamp2str(t, pattern="%Y-%m-%d  %H:%M:%S"):
    """ Given a float timestamp it returns the date as a formatted string,
        based on the date `pattern` specified """
    return datetime.datetime.fromtimestamp(t).strftime(pattern)
# import datetime
from dateutil import tz
def convert_timezone(time, a="UTC", b="local"):
    # TIMEZONE OBJECTS
    tza = tz.tzlocal(a) if (a=="local") else tz.gettz(a)
    tzb = tz.tzlocal(b) if (b=="local") else tz.gettz(b)

    # FORMAT TIME WITH FROM TIMEZONE
    time = time.replace(tzinfo=tza)

    # CHANGE TIME ZONE
    newtime = time.astimezone(tzb)
    return newtime
