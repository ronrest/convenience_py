import collections


def sentence_2_freq_vec(s, vocab_list):
    # TODO: compare the perfomrance of different methods of achieving this
    #       same task.

    tally = collections.Counter(s)
    return [tally[word] for word in vocab]

    # Alternative way of doing this task
    # pd.Series(collections.Counter(s), index=vocab).fillna(0, inplace=False)

