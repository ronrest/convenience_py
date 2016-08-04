import pickle
# ==============================================================================
#                                                                     OBJ2PICKLE
# ==============================================================================
def obj2pickle(obj, file, protocol=-1):
    """
    Saves an object as a binary pickle file to the desired file path.

    :param obj: (object)
        The python object you want to save.
    :param file: (str)
        File path of file you want to save as.  eg /tmp/myFile.pkl
    :param protocol: (int) (default = -1)
        0  = original ASCII protocol and is backwards compatible with earlier
             versions of Python.
        1  = old binary format which is also compatible with earlier versions
             of Python.
        2  = provides much more efficient pickling of new-style classes.
             compatible with Python >= 2.3
        -1 = uses the highest (latest) protocol available. This is the default
             value for this function.

    :example:
        s = "This is my super important object i want to cache"
        obj2pickle(s, "/home/fred/my_cached_object.pkl")
    """
    # ==========================================================================
    print("pickling object to {} ".format(file))
    with open(file, mode="wb") as fileObj:
        pickle.dump(obj, fileObj, protocol=protocol)
    print("---Done!")

