# ==============================================================================
#                                                                       list2str
# ==============================================================================
def list2str(a, sep=" "):
    """
    Takes a list and returns a string of all the string representation of the
    elements of the list concatenated together. By default it separates each
    element them with a single space, but you can specify a different separator.

    :param a: (list)
        The list, whose elements you want to concatenate together into a string
    :param sep: (string)(default = " ")
        The string you want to use to separate elements of the list with. By
        default it it just a space.
    :return: (string)
        The string composed of the elements of the list.
    """
    # ==========================================================================
    return sep.join(a)

