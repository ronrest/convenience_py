# ==============================================================================
#                                                                       FILE2STR
# ==============================================================================
def file2str(file):
    """
    Takes a file path and returns the contents of that file as a tring object.

    :param file: (string)
        The path to the file.
    :return:
    """
    # ==========================================================================
    with open(file, "r") as textFile:
        text = textFile.read()
    return text

