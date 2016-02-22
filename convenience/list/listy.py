

# ==============================================================================
#                                                                          LISTY
# ==============================================================================
def listy(l, search=""):
    """
    Takes a list `l` and a search term, and returns elements in the list that
    contain that search term.

    If the search term is a number, then it returns the elements that match
    that value exactly.

    If the list is composed of numbers and you want to return the elements that
    contain some digit or sequence of digits (as opposed to matching the exact
    value), then use a search term that is a number as a string.

    NOTE: the search term is not case sensitive.

    :param l: (iterable)
        list (or some other iterable) that you want to search through.
    :param search: (string, or int, long, float)
        The thing you want to search for in the list.
    :return: (list)
        Returns a list of the items that contained the search result.

    :example:
        >>> listy([3277, 932, 7, 234], "32")
        [3277, 932]

    :example:
        >>> listy(["science", "conscience", "patience"], "science")
        ['science', 'conscience']
    """
    # ==========================================================================
    if isinstance(search, str):
        return [item for item in l if search.lower() in str(item).lower()]
    elif isinstance(search, (int, float, long)):
        return [item for item in l if search == item]

