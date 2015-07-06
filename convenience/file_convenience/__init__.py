# TODO: Add a function that creates a new directory if it has not been created.
#       SHould handle nested directories where more than one subdirectory does
#       not already exist.

# TODO: add function to cache multiple objects at once based on a list of
#       variable names as strings.

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
