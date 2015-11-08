# TODO: Add a function that creates a new directory if it has not been created.
#       SHould handle nested directories where more than one subdirectory does
#       not already exist.

# TODO: add function to cache multiple objects at once based on a list of
#       variable names as strings.

import os

# ==============================================================================
#                                                             CACHE CALCULATIONS
# ==============================================================================
def cache_calc(filename, func, *args, **kwargs):
    """
    Cache calculations, so that the first call to this function performs the
    calculations, and caches them to a file. And future calls to this function
    simply load up the data from the cached file.

    :param filename:(str) the file path you want to save the cached file as
    :param func: The function to call to calculate the
    :param *args: ordered arguments to be passed on to func()
    :param **kwargs: keyword arguments to be passed on to func()
    :return: whatever func() returns.

    :examples:
        cache_calc("myCachedFile", myFunc)
    """
    # ==========================================================================
    from os.path import exists as file_exists
    from pickle import load as pickle_load
    from pickle import dump as pickle_dump

    if file_exists(filename):
        print("Loading the cached version of " + filename)
        with open(filename, mode="rb") as fileObj:
            x = pickle_load(fileObj)
    else:
        print("Caching the calculation to the file " + filename)
        x = func(*args, **kwargs)
        # Cache the calculation so future calls to this function load the cached
        # object instead.
        with open(filename, mode="wb") as fileObj:
            pickle_dump(x, fileObj)
    return x



# ==============================================================================
#                                                                 LIST DIR ITEMS
# ==============================================================================
def list_dir_items(d, relative=True, root=""):
    """
    Takes a string of a directory. And returns two lists.
    - dList =  List of all the child directories
    - fList =  List of all the child files
    :param d: (str)
        The full path to the directory you want to search in.
    :param relative: (optional)(boolean)
        if True, then it returns the listed items as directories relative to
        the direc directory.

        IF False, then it returns the FULL paths.
    :param root: (Optional)(str)
        A directory path that we want to use as the root for relative paths.
        If left blank, then it uses the directory set in d as the root directory.
    """
    # TODO: create a filter, so you can filter for certain types of files, or
    #       directories, using something like regex, or file extensions, or
    #       mime types
    # --------------------------------------------------------------------------
    #                                                                      Setup
    # --------------------------------------------------------------------------
    fList = []  # file List
    dList = []  # Directory List
    d = os.path.abspath(d)

    # --------------------------------------------------------------------------
    #       Set the ralative/absolute path to append to the output list of items
    # --------------------------------------------------------------------------
    if relative:
        root = root.strip()
        if  root == "":
            root = d
        outpath = os.path.relpath(d, root)
    else:
        outpath = d

    # if the root path is d, then remove the "." from path.
    if outpath == ".":
        outpath = ""

    # --------------------------------------------------------------------------
    #          Sort each item in the directory into either a directory or a file
    # --------------------------------------------------------------------------
    for item in os.listdir(d):
        full_item_path = os.path.join(d, item)      # Full path to the item
        out_item_path = os.path.join(outpath, item) # Path used in output list

        if os.path.isfile(full_item_path):
            fList.append(out_item_path)
        elif os.path.isdir(full_item_path):
            dList.append(out_item_path)
        else:
            print "WARNING: directoryItems found an item that is neither a \n"\
                  "         file, nor a directory"

    # --------------------------------------------------------------------------
    #                                                      Return the item lists
    # --------------------------------------------------------------------------
    return (dList, fList)
