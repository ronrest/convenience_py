import pickle
# ==============================================================================
#                                                                     OBJ2PICKLE
# ==============================================================================
def obj2pickle(obj, file):
    """
    Saves an object as a binary pickle file to the desired file path.

    :param obj: (object)
        The python object you want to save.
    :param file: (str)
        File path of file you want to save as.  eg /tmp/myFile.pkl

    :example:
        s = "This is my super important object i want to cache"
        obj2pickle(s, "/home/fred/my_cached_object.pkl")
    """
    # ==========================================================================
    print("pickling object to {} ".format(file))
    with open(file, mode="wb") as fileObj:
        pickle.dump(obj, fileObj)
    print("---Done!")

