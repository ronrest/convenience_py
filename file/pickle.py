import pickle


# ==============================================================================
#                                                                     OBJ2PICKLE
# ==============================================================================
import os
def obj2pickle(obj, file, protocol=2):
    """ Saves an object as a binary pickle file to the desired file path.

    Args:
        obj: (object)
            The python object you want to save.
        file: (str)
            File path of file you want to save as.  eg /tmp/myFile.pkl
        protocol: (int) (default = 2)
            0  = original ASCII protocol and is backwards compatible with earlier
                 versions of Python.
            1  = old binary format which is also compatible with earlier versions
                 of Python.
            2  = provides much more efficient pickling of new-style classes.
                 compatible with Python >= 2.3.
                 (Use this value to be compatible between py2.7 and py3.x)
            3 = Python >= 3.x?
            4 = Python >= 3.4
            -1 = uses the highest (latest) protocol available.

    Examples:
        s = "This is my super important object i want to cache"
        obj2pickle(s, "/home/fred/my_cached_object.pkl")
    """
    # ==========================================================================
    print("pickling object to {} ".format(file))

    # Ensure parent directory and necesary file structure exists
    pardir = os.path.dirname(file)
    if pardir.strip() != "": # ensure pardir is not an empty string
        if not os.path.exists(pardir):
            os.makedirs(pardir)

    with open(file, mode="wb") as fileObj:
        pickle.dump(obj, fileObj, protocol=protocol)
    print("---Done!")


# ==============================================================================
#                                                                     PICKLE2OBJ
# ==============================================================================
def pickle2obj(file):
    """
    Takes a filepath to a picke object, and returns a python object specified
    by that pickle file.

    Args:
        file: (str) File path to a pickle file.

    Returns: (object)
        A python object specified by the pickle file.

    Examples:
        myObject = pickle2obj("/tmp/myPickle.pkl")
    """
    # ==========================================================================
    # NOTE: if you get a "UnicodeDecodeError: 'ascii' codec can't decode" try
    #       obj = pickle.load(fileObj, encoding="latin1")
    with open(file, mode = "rb") as fileObj:
        obj = pickle.load(fileObj)
    return obj
