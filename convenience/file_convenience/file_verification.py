import hashlib
from os import stat

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
        "bytes"   = File size in bytes.

    :param v_val: {string or int}
        - If `v_val` is one of the hash types,then this should be a string with
          the hash code that you expect the file to be.
        - If `v_val` is "bytes" then this value should be an integer with the
          filesize that you expect file to be.
    :return: {boolean}
        Return True if the file matches the expected verification value.
    """
    # ==========================================================================
    # TODO: do dummy proofing for input values.

    # Verify using file size
    if v_type.lower() == "bytes":
        return stat(file).st_size == int(v_val)

    # Verify using hash
    else:
        v_types = {"md5": hashlib.md5,
                   "sha1": hashlib.sha1,
                   "sha256": hashlib.sha256,
                   "sha512": hashlib.sha512
                   }
        with open(file, 'rb') as fileObj:
            content = fileObj.read()
        hash = v_types[v_type.lower()](content).hexdigest()

        return hash == v_val



