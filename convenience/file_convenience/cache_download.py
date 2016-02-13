from __future__ import print_function
import os
from urllib import urlretrieve


def cache_download(url, out=("", "")):
    out_file = os.path.join(*out)

    print("Output file:"+out_file)
    print("downloaing from:", url)
    # --------------------------------------------------------------------------
    #                                                              Download File
    # --------------------------------------------------------------------------
    try:
        urlretrieve(url, out_file)
    except:
        raise Exception('failed to download from' + url)


