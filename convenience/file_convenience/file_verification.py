import hashlib

# ==============================================================================
#                                                              FILE_VERIFICATION
# ==============================================================================
def file_verification(file, v_type, v_val):
    """
    Verify the file using one of several methods including SHA1, SHA256, MD5,
    filesize and others.

    :param file: {string}
        Filepath to the file
    :param v_type: {string}
        Method of verification to use.

        "md5"
        "sha1"
        "sha256"
        "sha512"
        "bytes" # Not yet implemented

    :param v_val: {string}
        The value that it should be.
    :return: {boolean}
    """
    # ==========================================================================
    # TODO: do dummy proofing for input values.
    v_types = {"md5": hashlib.md5,
               "sha1": hashlib.sha1,
               "sha256": hashlib.sha256,
               "sha512": hashlib.sha512
               }
    with open(file, 'rb') as fileObj:
        content = fileObj.read()
    hash = v_types[v_type](content).hexdigest()

    # TODO: filesize verification.
    # Check filesize
    # statinfo = os.stat(filename)
    # statinfo.st_size == expected_bytes

    return hash == v_val




