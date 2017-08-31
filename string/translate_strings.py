

# ==============================================================================
#                                                              TRANSLATE_STRINGS
# ==============================================================================
def translate_strings(s, d):
    """
    Takes a string and a dictionary of {substring: replacement} values and
    returns a copy of the string with all the replacements made on the
    original string.

    :param s: (string)
        The string you want to perform translation on.
    :param d: (dictionary)
        Dictionary of in which the keys are strings you want to look for in `s`
        and the values are strings you want to replace them with.

        eg:  d={"bananas": "mangoes",
                "apples" : "oranges"}

        will replace all occurences of "bananas" with "mangoes", and replace all
        "apples" with "oranges".

    :return: (string)
        The translated string.

    :example:
        >>> text = "i juggled apples while sitting in a chair"
        >>> translator = {"apples": "chainsaws",
        >>>               "chair": "snakepit"}
        >>> translate_strings(text, translator)
        'i juggled chainsaws while sitting in a snakepit'
    """
    # ==========================================================================
    for key, val in d.items():
        s = s.replace(key, val)

    return s

