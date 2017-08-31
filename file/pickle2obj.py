import pickle

# ==============================================================================
#                                                                     PICKLE2OBJ
# ==============================================================================
def pickle2obj(file):
    """
    Takes a filepath to a picke object, and returns a python object specified
    by that pickle file.

    :param file: (str)
        File path to a pickle file.
    :return: (object)
        A python object specified by the pickle file.

    :example:
        myObject = pickle2obj("/tmp/myPickle.pkl")
    """
    # ==========================================================================
    with open(file, mode = "rb") as fileObj:
        obj = pickle.load(fileObj)
    return obj
