

def uncompress(file, method="tar"):
    #TODO: Add an output dir option.
    if method == "tar":
        import tarfile
        with tarfile.open(filename) as fileObj:
            #sys.stdout.flush()
            fileObj.extractall()

