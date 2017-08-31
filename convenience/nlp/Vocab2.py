
# An alternative version of vocab that doesnt rely on dataframes. Perform tests
# to see which one performs better.


# w2i = a dictionary that maps from indices to words.
# i2w = a list that maps from indices to words.






# ==============================================================================
#                                                                     WORD2INDEX
# ==============================================================================
def word2index(words, unknown=0):
    """
    Takes a word, or list of words, and returns the index or list of indices
    for the corresponding word in the vocabulary.

    You can specify what value to return for words that are not in the
    vocabulary. By default it returns 0 for those elements.

    :param words: {string, or list of strings}
        A single word string, or a list of strings of words to find the indices
        for.
    :param unknown: (default = 0)
        What value should it return for words that are not in the vocabulary?
    :return:
        If words was a string, then it returns a single integer.

        If words was a list of strings, then it returns a list of integers.
    """
    # ==========================================================================
    if isinstance(words, (str, unicode)):
        return w2i.get(words, unknown)
    else:
        return [w2i.get(word, unknown) for word in words]


# ==============================================================================
#
# ==============================================================================
def index2word(index, unknown="UNK"):
    """
    Takes an index, or list of indices, and returns the word string, or list of
    word strings that the indices correspond to in the vocabulary.

    You can specify what value to return for indices that are not in the
    vocabulary. By default it returns "UNK" for those elements.

    :param index: {int, or list of ints}
        A single word index, or a list of word indices of interest.
        for.
    :param unknown: (default = "UNK")
        What value should it return for word indices that are not in the
        vocabulary?
    :return:
        If index is an integer, then it returns a single word string.

        If index is a list of integers, then it returns a list of word strings.
    """
    # ==========================================================================
    if isinstance(index, (int, long)):
        return i2w.get(index, unknown)
    else:
        return [i2w.get(i, unknown) for i in index]

