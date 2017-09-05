import os

# ==============================================================================
#                                                       HUMAN_FRIENDLY_FILESIZES
# ==============================================================================
def human_friendly_filesizes(size):
    """ Given an integer filesize in Bytes, it returns a human friendly string
        string that automatically determines the most appropriate scale

    Examples:
        >>> human_friendly_filesizes(4765)
        '4.765 KB'

        >>> human_friendly_filesizes(28535234)
        '28.535 MB'

        >>> human_friendly_filesizes(35023452322)
        '35.023 GB'
    """
    if size//1000000000 > 0:
        s = "{:0.3f} GB".format(size/1000000000.)
    elif size//1000000 > 0:
        s = "{:0.3f} MB".format(size/1000000.)
    elif size//1000 > 0:
        s = "{:0.3f} KB".format(size/1000.)
    else:
        s = "{} B".format(size)
    return s


# ==============================================================================
#                                                                PRETTY_FILESIZE
# ==============================================================================
def pretty_filesize(f):
    """ Given a filepath, it returns that files filesize as a human friendly
        string """
    return human_friendly_filesizes(os.stat(f).st_size)


