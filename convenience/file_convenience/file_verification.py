import hashlib

def file_verification(file, v_type, v_val):
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




