import datetime
import dateutil
import dateutil.tz

def timestamp2str(t, tz="Australia/Melbourne", format="%Y-%m-%d %H:%M:%S.f %Z"):
    tzinfo = dateutil.tz.gettz(tz)
    assert tzinfo is not None, "Could not get timezone data"
    return datetime.datetime.fromtimestamp(t, tz=tzinfo).strftime(format)

def str2datetime(t, format="%Y-%m-%d %H:%M:%S", tz="Australia/Melbourne"):
    tzinfo = dateutil.tz.gettz(tz)
    assert tzinfo is not None, "Could not get timezone data"
    dt = datetime.datetime.strptime(t, format).replace(tzinfo=tzinfo)
    return dt

def str2timestamp(t, format="%Y-%m-%d %H:%M:%S", tz="Australia/Melbourne"):
    tzinfo = dateutil.tz.gettz(tz)
    assert tzinfo is not None, "Could not get timezone data"
    dt = datetime.datetime.strptime(t, format).replace(tzinfo=tzinfo)
    return dt.timestamp()

def now_datetime(tz="Australia/Melbourne"):
    tzinfo = dateutil.tz.gettz(tz)
    assert tzinfo is not None, "Could not get timezone data"
    return datetime.datetime.now(tz=tzinfo)

def now_timestamp():
    tzinfo = dateutil.tz.gettz("UTC")
    assert tzinfo is not None, "Could not get timezone data"
    return datetime.datetime.now(tz=tzinfo).timestamp()

def now_string(format="%Y-%m-%d %H:%M:%S", tz="Australia/Melbourne"):
    tzinfo = dateutil.tz.gettz(tz)
    assert tzinfo is not None, "Could not get timezone data"
    return datetime.datetime.now(tz=tzinfo).strftime(format)



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
