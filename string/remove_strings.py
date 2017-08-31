

# ==============================================================================
#                                                                 REMOVE_STRINGS
# ==============================================================================
def remove_strings(s, rem):
    """
    Takes a string `s` and a list of strings `rem` that you want to remove from
    `s` . Returns a copy of the string with all the desired substrings removed.

    :param s: (string)
        The string you want to process.
    :param rem: (list of strings)
        list of substrings you want to remove from s.

        eg:  rem=["nonsense", "gobbledigook"]

        will remove all occurences of "nonsense" and "gobbledigook"  from s.

    :return: (string)
        A copy of `s` with the deletions made.
    """
    # ==========================================================================
    for substring in rem:
        s = s.replace(substring, "")

    return s

