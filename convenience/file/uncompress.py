

# ==============================================================================
#                                                                     UNCOMPRESS
# ==============================================================================
def uncompress(file, method="tar"):
    """ Uncompress packaged files such as zip and tarballs.
    
    Args:
        file: (string)
            filepath of compressed file
        method: (string)
            Method of uncompression to use.
    
            TODO: autodetect based on filename.
    
            "tar"  = for tar.gz files.
    """
    #TODO: Add an output dir option.
    if method == "tar":
        import tarfile
        with tarfile.open(filename) as fileObj:
            #sys.stdout.flush()
            fileObj.extractall()

