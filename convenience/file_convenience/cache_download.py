from __future__ import print_function
import os
from urllib import urlretrieve


def cache_download(url, out=("", "")):
    out_file = os.path.join(*out)

    print("Output file:"+out_file)
    print("downloaing from:", url)
    # --------------------------------------------------------------------------
    #                                                 Check if local file exists
    # --------------------------------------------------------------------------
    if os.path.exists(out_file):
        #TODO: check the local file is the correct file.

        # No need to download file again, so terminate here.
        print("File already exists, keeping cached copy")
        return None

    # --------------------------------------------------------------------------
    #                                                              Download File
    # --------------------------------------------------------------------------
    try:
        urlretrieve(url, out_file)
    except:
        raise Exception('failed to download from' + url)


