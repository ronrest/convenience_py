import collections


# ==============================================================================
#                                                            SENTENCE_2_FREQ_VEC
# ==============================================================================
def sentence_2_freq_vec(s, vocab_list):
    """
    Given a list of words from a sentence, and a vocabulary list that specifies
    the order of the different words for the final output vector, it returns
    a list of integers representing a vector encoding of the word frequency
    counts.

    :param s: (list of strings)
        The sentence as a list of words.
    :param vocab_list: (list of strings)
        The ordered vocabulary as a list of words.
    :return:(list of integers)
        The frequency counts

    """
    # ==========================================================================
    # TODO: compare the perfomrance of different methods of achieving this
    #       same task.

    tally = collections.Counter(s)
    return [tally[word] for word in vocab]

    # Alternative way of doing this task
    # pd.Series(collections.Counter(s), index=vocab).fillna(0, inplace=False)

