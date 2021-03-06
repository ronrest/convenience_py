import collections


# ==============================================================================
#                                                            SENTENCE_2_FREQ_VEC
# ==============================================================================
def sentence_2_freq_vec(s, vocab_list, ohv=False, thresh=1):
    """
    Given a list of words from a sentence, and a vocabulary list that specifies
    the order of the different words for the final output vector, it returns
    a list of integers representing a vector encoding of the word frequency
    counts.

    :param s: (list of strings)
        The sentence as a list of words.
    :param vocab_list: (list of strings)
        The ordered vocabulary as a list of words.
    :param ohv: (boolean) (default=False)
        Should it return as a one hot vector?
        True:  Any word occuring at least once gets a value of 1
        False  (default) the values in the vector will be word counts in s
    :param: thresh: (int) (default=1)
        If using one hot encoding (`ohv`=True), use this variable to set the
        threshold of how many times a word must occur as a minumum in the
        sentence for it gets assigned a value of 1.

        Default = 1 (word must occur at least once to get a value of 1)

    :return:(list of integers)
        The frequency counts

    :example:
        >>> vocab = ['the', 'a', 'is', 'it', 'best', 'good', 'bad']
        >>> s = "it is the best it is".split()
        >>> sentence_2_freq_vec(s, vocab_list=vocab)
        [1, 0, 2, 2, 1, 0, 0]

        >>> sentence_2_freq_vec(s, vocab_list=vocab, ohv=True)
        [1, 0, 1, 1, 1, 0, 0]

        >>> sentence_2_freq_vec(s, vocab_list=vocab, ohv=True, thresh=2)
        [0, 0, 1, 1, 0, 0, 0]
    """
    # ==========================================================================
    # TODO: compare the perfomrance of different methods of achieving this
    #       same task.

    tally = collections.Counter(s)
    if ohv:
        return [int(tally[word] >= thresh) for word in vocab_list]
    else:
        return [tally[word] for word in vocab_list]

    # Alternative way of doing this task
    # pd.Series(collections.Counter(s), index=vocab).fillna(0, inplace=False)

