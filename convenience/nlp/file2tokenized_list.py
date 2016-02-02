from nltk import word_tokenize as tokenize


# ==============================================================================
#                                                            FILE2TOKENIZED_LIST
# ==============================================================================
def file2tokenized_list(files, lower=True, encoding="utf-8"):
    """
    Takes a filepath, or a list of filepaths and returns lists of tokenized
    strings.

    You can actually also feed it a dictionary of file path lists, where each
    key of the dictionary represents some category. If you chose to feed it a
    dictionary, then the output will be a tuple with 3 values.
        tokenized_list = the usual lists of tokenized strings.
        labels         = a list containing integer labels corresponding to the
                         category that each element of tokenized_list belongs to
        cats           = A list of the unique category names. Indices of the
                         names correspond to the integer values used in labels
                         such that cats[labels[i]] gives you the original name
                         for the category that the ith training example belongs
                         to.

    :param files: (str, or list of strings or dict)
        String of a single file path, or a list of file path strings.
    :param lower: (bool)(default = True)
        Convert all text to lowercase?
    :param encoding: (str)(default = "utf-8")
        Encoding used in the text files
    :return:
        A list of lists of tokenized strings (if files is a string or a list of
        strings)

        A tuple of 3 items if files is a dictionary containing lists of strings.
        (see the description section for more details about the 3 elements
        returned)
    """
    # ==========================================================================
    print("Generating a tokenised list from files")
    if isinstance(files, dict):
        return dict_file2tokenized_list(files, lower, encoding)
    if isinstance(files, str):
        files = [files]
    num_items = len(files)

    tokenized_list = ["MISSING"] * num_items    # Will store the tokenised text
    for i in range(num_items):
        with open(files[i], "r") as textFile:
            text = textFile.read()
        text = text.decode(encoding)
        if lower:
            text = text.lower()
        tokenized_list[i] = tokenize(text)
    print("---Done!")
    return tokenized_list

file2tokenised_list = file2tokenized_list           # Non-US English version

