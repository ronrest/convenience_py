# ==============================================================================
#                                                                       FILE2STR
# ==============================================================================
def file2str(file):
    """ Takes a file path and returns the contents of that file as a string.

    Args:
        file: (string)
            The path to the file.

    Returns: (string)
    """
    # ==========================================================================
    with open(file, "r") as textFile:
        text = textFile.read()
    return text
