from nltk import word_tokenize as tokenize


# ==============================================================================
#                                                       DICT_FILE2TOKENIZED_LIST
# ==============================================================================
def dict_file2tokenized_list(files, lower=True, encoding="utf-8"):
    """
    Takes a dictionary of file path lists, where each key of the dictionary
    represents some category.

    The output will be a tuple with 3 values.
        tokenized_list = lists of tokenized strings.
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
        A tuple of 3 items if files is a dictionary containing lists of strings.
        (see the description section for more details about the 3 elements
        returned)
    """
    # ==========================================================================
    cats = files.keys()
    num_per_category  = {cat: len(files[cat]) for cat in cats}
    num_items = sum(num_per_category.values())

    tokenized_list = ["MISSING"] * num_items    # Will store the tokenised text
    labels = ["MISSING"] * num_items            # Will store the labels

    running_index = 0
    for cat_i, cat in enumerate(cats):
        #num_items_for_cat =
        for example_i in range(num_per_category[cat]):
            with open(files[cat][example_i], "r") as textFile:
                text = textFile.read()
            text = text.decode(encoding)
            if lower:
                text = text.lower()
            tokenized_list[running_index] = tokenize(text)
            labels[running_index] = cat_i
            running_index += 1
    print("---Done!")
    return (tokenized_list, labels, cats)


dict_file2tokenised_list = dict_file2tokenized_list # Non-US English version

